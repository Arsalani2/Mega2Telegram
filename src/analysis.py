
# @title Requirements
# This software is licensed under the GNU GPL v3 or later.
# Installing required libraries
!sudo apt-get install megatools
!pip install telethon tqdm ffmpeg-python

# @title Download from Mega to Google Colab
# Creating the folder colab_download
!mkdir -p /content/colab_download
# Downloading files from Mega and saving them in the colab_download folder
!megadl --path /content/colab_download --reload 'Your_Link'

# Listing downloaded files in the folder
!ls -la /content/colab_download

# Removing specific downloaded files from the folder
!rm -i '/content/colab_download/Path'

# If needed, you can transfer the downloaded file to your Google Drive
!cp '/content/colab_download/Path' '/content/drive/MyDrive/Path'

# If needed, you can also transfer files from your Google Drive to your Colab environment
# @title Google Drive
from google.colab import drive
drive.mount('/content/drive')
!cp -r '/content/drive/MyDrive/Path' '/content/colab_download/Path'

# Main variables
api_id = 'API_ID'
api_hash = 'API_HASH'
bot_token = 'BOT_TOKEN'
chat_id = CHAT_ID # Just Int

# @title Code V 1.00
import os, asyncio, subprocess, uuid
from telethon import TelegramClient
from tqdm.notebook import tqdm
from telethon.tl.types import DocumentAttributeVideo, DocumentAttributeAudio

class TelegramUploader:
    def __init__(self, api_id, api_hash, bot_token, chunk_size=8*1024*1024):
        # Set up the Telegram client and file upload settings
        self.client = TelegramClient(None, api_id, api_hash)
        self.bot_token = bot_token
        self.chunk_size = chunk_size

    async def start(self):
        # Start the client using the bot token
        await self.client.start(bot_token=self.bot_token)
        print("Client started successfully!")

    def progress_callback(self, current, total, pbar):
        # Update the progress bar during file upload
        pbar.update(current - pbar.n)

    def get_media_info(self, file_path):
        # Extract basic media info (width, height, duration) using ffprobe
        try:
            result = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'stream=width,height,duration',
                                     '-of', 'default=noprint_wrappers=1', file_path],
                                    stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            media_info = {line.split('=')[0]: line.split('=')[1] for line in result.stdout.splitlines()}
            return int(media_info.get('width', 0)), int(media_info.get('height', 0)), float(media_info.get('duration', 0))
        except Exception as e:
            print(f"Error extracting media info: {e}")
            return None, None, None

    def generate_video_thumbnail(self, file_path):
        # Create a thumbnail image from the middle of the video
        thumbnail_path = f"/content/{uuid.uuid4()}.jpg"
        try:
            _, _, duration = self.get_media_info(file_path)
            if duration:
                cmd = ['ffmpeg', '-y', '-i', file_path, '-ss', str(duration / 2), '-vframes', '1', '-vf', 'scale=320:-1', thumbnail_path]
                if subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True).returncode == 0:
                    return thumbnail_path
        except Exception as e:
            print(f"Error generating thumbnail: {e}")
        return None

    async def send_file(self, file_path, file_name, chat_id):
        # Prepare and send a file to Telegram
        file_size = os.path.getsize(file_path)
        attributes, thumb_path, streaming = None, None, False

        # Handle video files
        if file_path.endswith(('.mp4', '.mkv', '.avi', '.mov')):
            width, height, duration = self.get_media_info(file_path)
            attributes = [DocumentAttributeVideo(duration=int(duration), w=width, h=height, supports_streaming=True)]
            streaming = True
            thumb_path = self.generate_video_thumbnail(file_path)
        # Handle audio files
        elif file_path.endswith(('.mp3', '.wav', '.ogg')):
            _, _, duration = self.get_media_info(file_path)
            attributes = [DocumentAttributeAudio(duration=int(duration), voice=False)]
            streaming = True

        # Upload the file with a progress bar
        with tqdm(total=file_size, unit='B', unit_scale=True, desc=file_name, leave=True) as pbar:
            await self.client.send_file(
                chat_id, file_path, caption=file_name, supports_streaming=streaming,
                attributes=attributes, thumb=thumb_path, chunk_size=self.chunk_size,
                progress_callback=lambda current, total: self.progress_callback(current, total, pbar)
            )

        # Clean up thumbnail file if it was generated
        if thumb_path and os.path.exists(thumb_path):
            os.remove(thumb_path)
        print(f"{file_name} uploaded successfully!")

    async def send_files_from_folder(self, folder_path, chat_id):
        # Upload all files from a folder
        for root, _, files in os.walk(folder_path):
            files.sort()  # Sort files for consistent order
            relative_path = os.path.relpath(root, folder_path) or ""
            if relative_path:
                await self.client.send_message(chat_id, f"📁Start Folder: {relative_path}")

            for file_name in files:
                await self.send_file(os.path.join(root, file_name), file_name, chat_id)

            if relative_path:
                await self.client.send_message(chat_id, f"📁End Folder: {relative_path}")

async def main():
    # Path to the folder containing files to upload
    folder_path = '/content/colab_download/'

    # Set up the uploader with your API credentials
    uploader = TelegramUploader(api_id, api_hash, bot_token, chunk_size=1024*1024)
    async with uploader.client:
        await uploader.start()
        await uploader.send_files_from_folder(folder_path, chat_id)

# Run the main function if not already in an event loop
if __name__ == '__main__':
    if not asyncio.get_event_loop().is_running():
        asyncio.run(main())
    else:
        await main()

# @title Delete All Mega Files
# Here we delete all files after uploading
import shutil

# Folder path
folder_path = '/content/colab_download/'

# Delete all files and contents in the folder
shutil.rmtree(folder_path)

# Recreate the empty folder
os.makedirs(folder_path)

print(f"All files inside the folder {folder_path} have been deleted.")