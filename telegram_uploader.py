#!/usr/bin/env python
# -*- coding: utf-8 -*-

import telegram
import argparse
import os

def send_file(token, chat_id, file_path):
    """
    Sends a file to a Telegram chat using a bot.

    Args:
        token (str): The Telegram bot token.
        chat_id (str): The ID of the chat to send the file to.
        file_path (str): The path to the file to send.
    """
    if not os.path.exists(file_path):
        print(f"Error: File not found at '{file_path}'")
        return

    try:
        bot = telegram.Bot(token=token)
        with open(file_path, 'rb') as f:
            bot.send_document(chat_id=chat_id, document=f, filename=os.path.basename(file_path))
        print(f"File '{file_path}' sent successfully to chat '{chat_id}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Upload a file to Telegram.")
    parser.add_argument("token", help="Your Telegram Bot Token")
    parser.add_argument("chat_id", help="The Chat ID to send the file to")
    parser.add_argument("file_path", help="The path to the file you want to upload")

    args = parser.parse_args()

    send_file(args.token, args.chat_id, args.file_path)
