# 💻 YouTube Downloader & Telegram Uploader [![License: MIT][License-Badge]](LICENSE)

This project provides a simple, command-line workflow to download a video from YouTube and upload it directly to a Telegram chat.

## 🚀 Features

*   **Download & Upload:** Seamlessly download a YouTube video and upload it to Telegram with a single command.
*   **Automatic Cleanup:** The downloaded video file is automatically deleted after a successful upload to save space.
*   **Easy to Use:** Just provide the YouTube URL, your Telegram Bot Token, and your Chat ID.

## 🔧 How to Use

### Prerequisites

1.  **Python 3:** Make sure you have Python 3 installed on your system.
2.  **Required Libraries:** Install the necessary Python libraries by running:
    ```bash
    pip install python-telegram-bot yt-dlp
    ```

### Setup

1.  **Get a Telegram Bot Token:**
    *   Open Telegram and search for the `@BotFather` bot.
    *   Start a chat with `BotFather` and send the `/newbot` command.
    *   Follow the instructions to create a new bot.
    *   `BotFather` will give you a unique API token. **Keep this token secure!**

2.  **Get your Chat ID:**
    *   Search for the `@userinfobot` on Telegram.
    *   Start a chat with it, and it will immediately send you your user ID. This is your Chat ID for a private chat with your bot.
    *   If you want to send the file to a group, add the bot to the group and send a message. The bot will reply with the group's ID.

### Running the Script

Use the `main.py` script to run the entire download-and-upload process. Provide the YouTube URL, your bot token, and your chat ID as command-line arguments.

**Command Format:**
```bash
python main.py "YOUTUBE_URL" "YOUR_BOT_TOKEN" "YOUR_CHAT_ID"
```

**Example:**
```bash
python main.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ" "123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11" "987654321"
```

The script will first download the video to a local `downloads/` directory, then upload it to your specified Telegram chat, and finally, delete the local file.

---
## Connect with me <img src="https://media.giphy.com/media/iY8CRBdQXODJSCERIr/giphy.gif" width="30px">
<p align="center">
<a href="https://t.me/Opleech_WD"><img src="https://img.shields.io/badge/-𝐖𝐎𝐎𝐃𝐜𝐫𝐚𝐟𝐭 𝐌𝐢𝐫𝐫𝐨𝐫 𝐙𝐨𝐧𝐞™%20%20-0077B5?style=flat&logo=Telegram&logoColor=white"/></a>
<a href="https://t.me/Op_Topic_Group"><img src="https://img.shields.io/badge/-Wᴅ Tᴏᴘɪᴄ Gʀᴏᴜᴘ%20%20-0077B5?style=flat&logo=Telegram&logoColor=white"/></a>
<a href="https://t.me/WD_Request_Bot"><img src="https://img.shields.io/badge/-𝐖𝐎𝐎𝐃𝐜𝐫𝐚𝐟𝐭,𝐬 𝐁𝐨𝐭%20%20-0077B5?style=flat&logo=Telegram&logoColor=white"/></a>  
<a href="https://t.me/Opleech_WD"><img title="Telegram" src="https://img.shields.io/static/v1?label=WD.Zone&message=TG&color=blue-green"></a> 
</p>
 
-----
## Credits: [𝐖𝐎𝐎𝐃𝐜𝐫𝐚𝐟𝐭](https://t.me/Farooq_is_KING)

[License-Badge]:        https://img.shields.io/badge/License-MIT-blue.svg
