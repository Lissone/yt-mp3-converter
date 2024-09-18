<h1 align="center">
  Youtube MP3 Converter
</h1>

<p align="center">
  <a href="#description">Description</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#requirements">Requirements</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#technologies">Technologies</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#usage">Usage</a>
</p>
<br />
<p align="center">
  <img src="https://img.shields.io/static/v1?label=license&message=MIT" alt="License">
  <img src="https://img.shields.io/github/repo-size/Lissone/yt-mp3-converter" alt="Repo size" />
  <img src="https://img.shields.io/github/languages/top/Lissone/yt-mp3-converter" alt="Top lang" />
  <img src="https://img.shields.io/github/stars/Lissone/yt-mp3-converter" alt="Stars repo" />
  <img src="https://img.shields.io/github/forks/Lissone/yt-mp3-converter" alt="Forks repo" />
  <img src="https://img.shields.io/github/issues-pr/Lissone/yt-mp3-converter" alt="Pull requests" >
  <img src="https://img.shields.io/github/last-commit/Lissone/yt-mp3-converter" alt="Last commit" />
</p>

<p align="center">
  <a href="https://github.com/Lissone/yt-mp3-converter/issues">Report bug</a>
  ·
  <a href="https://github.com/Lissone/yt-mp3-converter/issues">Request feature</a>
</p>

<br />

## Description

A Python script that downloads YouTube videos and automatically converts them to MP3 using yt-dlp and FFmpeg. Simple to set up and use, with options for customization.

## Requirements

- [Python](https://www.python.org/downloads/)
- [FFmpeg](https://ffmpeg.org/download.html)
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)

## Technologies

- Python
  - yt-dlp
  - difflib
  - logging
- FFmpeg

## Usage

### 1. Install Python
Download and install Python from the [official website](https://www.python.org/downloads/), ensuring the option "Add Python to PATH" is checked during installation.

### 2. Install dependencies
Open the command prompt and install `yt-dlp`:
```bash
pip install yt-dlp
```

### 3. Install FFmpeg
1. Download FFmpeg from [here](https://ffmpeg.org/download.html) and extract the files to a directory (e.g., `C:\ffmpeg`).
2. Add `C:\ffmpeg\bin` to your system's `PATH` environment variable.

### 4. Prepare the `urls.txt` file
Create a `urls.txt` file in the same directory as the script and add the YouTube URLs you want to download, one per line.

### 5. Run the script
Run the script with the following command:
```bash
python main.py
```

### 6. Optional: Customize the output directory
By default, the script saves files in the `downloads` folder. You can modify this by changing the `output_dir` parameter in the script.

## License

Distributed under the MIT License. See `LICENSE` for more information.

<h4 align="center">
  Made with ❤️ by <a href="https://github.com/Lissone" target="_blank">Lissone</a>
</h4>

<hr />