import argparse
import os
from youtube_downloader import download_video
from telegram_uploader import send_file

def main():
    parser = argparse.ArgumentParser(description="Download a YouTube video and upload it to Telegram.")
    parser.add_argument("youtube_url", help="The URL of the YouTube video to download.")
    parser.add_argument("token", help="Your Telegram Bot Token.")
    parser.add_argument("chat_id", help="The Chat ID to send the file to.")

    args = parser.parse_args()

    # Step 1: Download the video
    print("--- Starting YouTube Download ---")
    downloaded_file_path = download_video(args.youtube_url)

    if downloaded_file_path and os.path.exists(downloaded_file_path):
        # Step 2: Upload the video to Telegram
        print("\n--- Starting Telegram Upload ---")
        send_file(args.token, args.chat_id, downloaded_file_path)

        # Step 3: Clean up the downloaded file
        print("\n--- Cleaning Up ---")
        try:
            os.remove(downloaded_file_path)
            print(f"Successfully removed local file: {downloaded_file_path}")
        except OSError as e:
            print(f"Error removing file {downloaded_file_path}: {e}")
    else:
        print("\n--- Error ---")
        print("Could not proceed with Telegram upload because the download failed or the file path was not found.")

if __name__ == '__main__':
    main()
