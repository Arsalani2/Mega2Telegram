# Mega2Telegram

![M2T_Logo](img\M2T_Logo.jpg)

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
  - [Contribution](#contribution)
  - [Donate](#donate)
  - [License](#license)

## Features
- Direct file transfer from Mega.nz to Telegram
- Support for large file sizes
- Compatible with all file formats
- No need for VPS or virtual server
- Simple and easy-to-use interface

## Prerequisites
1. A Google account to use "Google Colab" and "Google Drive"
2. Mega.nz account
   - It's recommended to use a temporary email to create an account
   - Each free Mega account provides about 20GB of storage space
   - [Create a Mega.nz account](https://mega.nz/register)
   - [Temporary email](https://temp-mail.org/)
3. A Telegram bot
   - Create and configure through [@Botfather](https://t.me/botfather)
4. Telegram API ID and API Hash
   - Obtain from the [Telegram website](https://my.telegram.org/apps)
   - If you encounter any issues, get help from [@RailBot](https://t.me/RailBot)

## Installation and Setup
1. Import the project's `main.ipynb` file into Google Colab.

2. In the first cell, install the required libraries:
   ```
   !sudo apt-get install megatools
   !pip install telethon tqdm ffmpeg-python
   ```

3. Place your Mega.nz link in the second cell and run the cell.
   - The link should contain the link + encryption key
   - For public links, first transfer the content to your account

4. Manage files in the `colab_download` folder:
   - Cell 3: View folder contents
   - Cell 4: Delete selected files

5. Transfer files between Google Colab and Google Drive (optional):
   - Cells 5 and 6: Set input and output paths

6. Initial setup:
   - In cell 7, replace the required values:
     - API ID and API Hash (from Telegram website or @RailBot)
     - Bot Token (from @BotFather)
     - Your Telegram account's numeric ID (from @userinfobot)

7. Run the main code:
   - In cell 8, execute the main code
   - Re-enter the Bot Token
   - Google Colab settings:
     - Set Runtime to CPU
     - Don't abandon the system
     - After completion, click on Disconnect Runtime

8. Delete files after upload (optional):
   - Run cell 9

## How to Use
1. Run the code cells in order.
2. Wait for the files to download from Mega.nz.
3. After the download is complete, the files will be automatically sent to your Telegram bot.
4. After finishing, delete the temporary files using the ninth cell.

## Troubleshooting
1. Mega.nz download limit error:
   - Wait for a while and try again
   - Stop the cell and then Run it again
   - In Google Colab, Disconnect the Runtime once and Connect again

2. To prevent Google Colab from disconnecting, keep the browser page open.

## Contribution
Your contributions to improving this project are highly valuable. Please open an Issue for any suggestions or bug reports, or submit a Pull Request.


## Donate
If this project has been useful to you, you can support us in its development and improvement through financial contributions:

- TRX wallet address: `TKXusugL4Ju4iTdRdvUJZ6LWVH1vdo7Zkt`

## License
This project is published under the GNU license. For more information, please read the [LICENSE file](LICENSE).

---

Made with love by Arsalan# Test
# Test
# Test
# test2
