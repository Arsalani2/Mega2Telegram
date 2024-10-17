# Mega2Telegram

![M2T_Logo](img\logo.png)

Version 1.00

Mega2Telegram is a powerful tool for automatically transferring files from Mega.nz to Telegram using Google Colab. This project allows you to easily transfer your files without the need for a VPS or virtual server.

## Table of Contents
- [Mega2Telegram](#mega2telegram)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Prerequisites](#prerequisites)
  - [Installation and Setup](#installation-and-setup)
  - [How to Use](#how-to-use)
  - [Troubleshooting](#troubleshooting)
  - [Contributing](#contributing)
  - [Donate](#donate)
  - [License](#license)

## Features
- Direct file transfer from Mega.nz to Telegram
- Support for large files
- Compatible with all file formats
- No VPS or virtual server required
- Simple and easy-to-use interface

## Prerequisites
1. A Google account to use "Google Colab" and "Google Drive"
2. Mega.nz account
   - It is recommended to use a temporary email to create an account
   - Each free Mega account provides about 20GB of storage space
   - [Create Mega.nz Account](https://mega.nz/register)
   - [Temporary Email](https://temp-mail.org/)
3. A Telegram bot
   - Create and configure through [@Botfather](https://t.me/botfather)
4. Telegram API ID and API Hash
   - Get from [Telegram website](https://my.telegram.org/apps)
   - If you have issues, get help from [@RailBot](https://t.me/RailBot)

## Installation and Setup
1. Import the project's `main.ipynb` file to Google Colab.

2. Install required libraries in the first cell:
   ```
   !sudo apt-get install megatools
   !pip install telethon tqdm ffmpeg-python
   ```

3. Place your Mega.nz link in the second cell and run it.
   - The link must contain "link + encryption key"
   - In this library to download content from a public link, you first need to transfer the content to your account, click on the three dots of your folder or file and click "Save to Cloud Drive", then click on the three dots of the saved content in your account and click "Share Link" copy the link and place it in the first cell field
   - This library doesn't support progress bar, so when the file name is printed in the console, it means your file has been downloaded
   - If your file is not completely downloaded or you stop the cell, "temp" or temporary files remain in the folder, you must delete these manually (cells 3 and 4 are provided for this purpose) if you don't, we will encounter errors in the continuation of the code
   - I suggest not to download a large folder during one cell but step by step, because after a while you will be limited by Mega.nz and Google Colab servers

4. Managing files in the `colab_download` folder (optional):
   - Cell 3: View folder contents completely and accurately
   - Cell 4: Delete files selected by you

5. File transfer between Google Colab and Google Drive (optional):
   - Cells 5 and 6: In this cell, you can transfer files downloaded from Mega.nz to Google Drive if needed
   You can also transfer a file from Google Drive to Google Colab and then send it to Telegram, just set the input and output paths

6. Initial setup:
   - In cell 7, replace the required values:
     - API ID and API Hash (from Telegram website or @RailBot)
     - Bot Token (from @BotFather)
     - Your Telegram account's numeric ID (from @userinfobot)

7. Running the main code:
   - In cell 8, run the main code
   - Enter Bot Token again
   - Google Colab settings:
     - Set Runtime to CPU
     - Google Colab constantly checks your presence, so don't abandon the system
     - After finishing work, click on Disconnect Runtime

8. Complete deletion of files after upload (optional):
   - Run cell 9

## How to Use
1. Run the code cells in order.
2. Wait for files to download from Mega.nz.
3. After download completion, files will automatically be sent to your Telegram bot.

## Troubleshooting
1. Mega.nz download limit error:
   - Wait for a while and try again
   - Stop the cell and Run again
   - In Google Colab, Disconnect Runtime once and Connect again

2. To prevent Google Colab connection from dropping, keep the browser page open.

## Contributing
Your contributions to improving this project are highly valuable. Please open an Issue for any suggestions or bug reports, or submit a Pull Request.

## Donate
If this project has been useful for you, you can help us develop and improve it through financial support:

- TRX wallet address: `TKXusugL4Ju4iTdRdvUJZ6LWVH1vdo7Zkt`

## License
This project is released under the GNU license. For more information, read the [LICENSE](LICENSE) file.

---

Made with love by Arsalan2# Mega2Telegram
