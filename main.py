import os
import yt_dlp

def download_and_convert(url_list_file, output_dir):
    # Configurações do yt-dlp
    ydl_opts = {
        'format': 'bestaudio/best',  # Melhor qualidade de áudio
        'outtmpl': f'{output_dir}/%(title)s.%(ext)s',  # Modelo de nome de arquivo
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'noplaylist': True,  # Não baixar playlists
        'ignoreerrors': True,  # Ignora erros de download
    }

    # Certifique-se de que o diretório de saída exista
    os.makedirs(output_dir, exist_ok=True)

    with open(url_list_file, 'r') as file:
        urls = file.readlines()

    for url in urls:
        url = url.strip()
        if url:
            try:
                # Cria um objeto yt-dlp com as opções fornecidas
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    # Obtém o título do vídeo
                    info_dict = ydl.extract_info(url, download=False)
                    title = info_dict.get('title', 'Unknown Title')
                    mp3_file = os.path.join(output_dir, f'{title}.mp3')

                    # Verifica se o arquivo MP3 já existe
                    if os.path.isfile(mp3_file):
                        print(f"Arquivo MP3 já existe: {mp3_file}. Pulando...")
                        continue

                    # Download e conversão do vídeo
                    print(f"Baixando e convertendo: {url}")
                    ydl.download([url])

            except Exception as e:
                print(f"Erro ao processar {url}: {e}")
                continue

if __name__ == "__main__":
    download_and_convert('urls.txt', 'downloads')
