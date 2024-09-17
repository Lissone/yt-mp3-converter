import os
from yt_dlp import YoutubeDL
import difflib

# ----------------------------------------------- #

URLS_FILE = 'urls.txt'
OUTPUT_DIR = 'E:'
# OUTPUT_DIR = 'downloads' # Debug only

YDL_OPTS = {
    'format': 'bestaudio/best',  # Best audio quality
    'outtmpl': f'{OUTPUT_DIR}/%(title)s.%(ext)s',  # Output filename template
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'noplaylist': True,  # Do not download playlists
    'ignoreerrors': True,  # Ignore download errors
    'no_warnings': True,  # Suppress warnings
    # 'quiet': True,  # Suppress yt-dlp logs
}

# ----------------------------------------------- #

def file_already_downloaded(file_path):
    """Check if the file already exists in the output directory."""
    return os.path.exists(file_path) or os.path.isfile(file_path)


def titles_are_similar(title1, title2, threshold=0.8):
    """
    Compare two song titles and return True if they are similar enough
    based on the threshold (default is 80% similarity).
    """
    similarity = difflib.SequenceMatcher(None, title1.lower(), title2.lower()).ratio()
    return similarity >= threshold

# ----------------------

def download_and_convert_urls(urls, output_dir):
    downloaded_files = []

    for url in urls:
        try:
            with YoutubeDL(YDL_OPTS) as ydl:
                # Extract video info
                info_dict = ydl.extract_info(url, download=False)
                title = info_dict.get('title', 'Unknown Title').strip()
                mp3_file = os.path.join(output_dir, f'{title}.mp3')

                # Check if a similar file has already been downloaded
                similar_file_found = any(titles_are_similar(title, existing_title) for existing_title in downloaded_files)

                if similar_file_found:
                    print(f"Arquivo MP3 semelhante já baixado: {title}. Pulando...\n")
                    continue

                if file_already_downloaded(mp3_file):
                    print(f"Arquivo MP3 já existe: {mp3_file}. Pulando...\n")
                    continue

                # Download and convert the video
                print(f"\nBaixando e convertendo: {url}")
                ydl.download([url])

                # Add title to downloaded list after successful download
                downloaded_files.append(title)
                print(f"Download completo: {url}\n")
        except Exception as e:
            print(f"Erro ao processar {url}: {e}\n")
            continue

# ----------------------------------------------- #

if __name__ == "__main__":
    # Ensure the output directory exists
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Read the URLs from the TXT file
    with open(URLS_FILE, 'r') as file:
        urls = [url.strip() for url in file.readlines() if url.strip()]

    download_and_convert_urls(urls, OUTPUT_DIR)
