import os
from yt_dlp import YoutubeDL
import difflib
from logger import setup_logger

# ----------------------------------------------- #

URLS_FILE = 'urls.txt'
# OUTPUT_DIR = 'E:'
OUTPUT_DIR = 'downloads' # Debug only


logger = setup_logger()

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
    total_urls = len(urls)
    successful_downloads = 0

    logger.info(f"Iniciando download de {total_urls} músicas\n")

    for index, url in enumerate(urls, start=1):
        try:
            ydl_opts = {
                'format': 'bestaudio/best',  # Best audio quality
                'outtmpl': f'{output_dir}/%(title)s.%(ext)s',  # Output filename template
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

            # Add custom logger to redirect logs from yt-dlp
            opts_with_logger = ydl_opts.copy()
            opts_with_logger['logger'] = logger
            
            with YoutubeDL(opts_with_logger) as ydl:
                logger.info(f"({index}/{total_urls}) Convertendo e baixando: {url}")

                # Extract video info
                info_dict = ydl.extract_info(url, download=False)
                title = info_dict.get('title', 'Unknown Title').strip()

                file_name = f'{title}.mp3'
                file_path = os.path.join(output_dir, file_name)

                # Check if a similar file has already been downloaded
                similar_file_found = any(titles_are_similar(title, existing_title) for existing_title in downloaded_files)

                if similar_file_found:
                    logger.warning(f"({index}/{total_urls}) Arquivo MP3 semelhante já baixado: {file_name}\n")
                    continue

                if file_already_downloaded(file_path):
                    logger.info(f"({index}/{total_urls}) Arquivo MP3 já existe: {file_name}\n")
                    continue

                # Download and convert the video
                ydl.download([url])

                # Add title to downloaded list after successful download
                downloaded_files.append(title)
                
                successful_downloads += 1
                logger.info(f"({index}/{total_urls}) Download completo: {file_name}\n")
        except Exception as e:
            logger.error(f"Erro ao processar {url}: {e}\n")
            continue

    logger.info(f"Download concluído! {successful_downloads} / {total_urls}.\n")

# ----------------------------------------------- #

if __name__ == "__main__":
    # Ensure the output directory exists
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Read the URLs from the TXT file
    with open(URLS_FILE, 'r', encoding='utf-8') as file:
        urls = [url.strip() for url in file.readlines() if url.strip()]

    download_and_convert_urls(urls, OUTPUT_DIR)
