import yt_dlp
import os

OUTPUT_PATH = "downloads/"

def download_video(url):
    """
    Downloads a video from the given URL and returns the path to the downloaded file.
    """
    if not os.path.exists(OUTPUT_PATH):
        os.makedirs(OUTPUT_PATH)

    # Use a progress hook to capture the filename
    file_path = [None]

    def progress_hook(d):
        if d['status'] == 'finished':
            file_path[0] = d.get('filename') or d.get('info_dict', {}).get('_filename')
            print(f"\nFinished downloading, file path is: {file_path[0]}")

    ydl_opts = {
        'outtmpl': os.path.join(OUTPUT_PATH, '%(uploader)s/%(title)s.%(ext)s'),
        'format': 'best[ext=mp4]/best',
        'progress_hooks': [progress_hook],
        'quiet': True,
    }

    print(f"Starting download for: {url}")
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        if file_path[0]:
            print("Download successful.")
            return file_path[0]
        else:
            print("Download finished, but could not determine file path.")
            return None
    except Exception as e:
        print(f"An error occurred during download: {e}")
        return None

if __name__ == '__main__':
    # This part is for direct testing of the module
    import sys
    if len(sys.argv) > 1:
        test_url = sys.argv[1]
        print(f"Testing download module with URL: {test_url}")
        downloaded_file = download_video(test_url)
        if downloaded_file:
            print(f"\nTest successful. File downloaded to: {downloaded_file}")
            # Clean up the downloaded file
            os.remove(downloaded_file)
            print("Cleaned up downloaded file.")
    else:
        print("Usage: python youtube_downloader.py <YOUTUBE_URL_FOR_TESTING>")
