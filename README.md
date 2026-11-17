# YouTube Audio/Video Downloader

A simple Python program that reads YouTube URLs from a `links.txt` file and downloads them as MP3/MP4 files.

The program uses [`yt-dlp`](https://github.com/yt-dlp/yt-dlp) for downloading and FFmpeg for media extraction/conversion.

## Features

* Downloads multiple YouTube URLs from a single `links.txt` file.
* Downloads **audio only**, without saving the video.
* Downloads **video + audio** in the desired quality
* Converts the downloaded audio to **MP3** or **MP4**, respectively.
* Uses **160 kbps** (default) audio quality as a balance between file size and quality.
* Saves files in a `YT_result` directory.
* Uses the YouTube video title as the filename.
* Skips blank lines and comments in `links.txt`.
* Continues downloading the remaining URLs if one download fails.
* Does not require a YouTube API key.
* Does not require any paid service or subscription.

## Requirements

You need the following software installed:

* Python 3.9 or newer
* `yt-dlp`
* FFmpeg

## Installation

### 1. Install Python

Download Python from:

https://www.python.org/downloads/

During installation on Windows, make sure to enable:

```text
Add Python to PATH
```

You can verify the installation with:

```bash
python --version
```

### 2. Install yt-dlp

Open a terminal in the project directory and run:

```bash
python -m pip install -U yt-dlp
```

Verify it with:

```bash
yt-dlp --version
```

### 3. Install FFmpeg

FFmpeg is required because yt-dlp uses it to extract and convert the downloaded media.

Official website:

https://ffmpeg.org/download.html

After installing FFmpeg, verify that both commands work:

```bash
ffmpeg -version
```

and:

```bash
ffprobe -version
```

If either command is not recognized, FFmpeg is probably not correctly configured in your system `PATH`.

## Project Structure

The project can be organized like this:

```text
youtube-url-downloader/
│
├── links.txt
├── youtube_url_downloader.py
├── README.md
│
└── YT_result/
```

`YT_result` is created automatically the first time the program runs, so you do not need to create it manually.

## Using `links.txt`

Create a file called:

```text
links.txt
```

Put one YouTube URL on each line:

```text
https://www.youtube.com/watch?v=xxxxxxxxxxx
https://www.youtube.com/watch?v=yyyyyyyyyyy
https://www.youtube.com/watch?v=zzzzzzzzzzz
```

You can also add blank lines or comments beginning with `#`:

```text
# Music

https://www.youtube.com/watch?v=xxxxxxxxxxx

# Another video
https://www.youtube.com/watch?v=yyyyyyyyyyy
```

Only the actual URLs will be processed.

## Running the Program

Open a terminal in the project directory and run:

```bash
python youtube_url_downloader.py
```

The program will process every URL in `links.txt`.

Example:

```text
Found 3 URL(s).
Saving audio to: C:\Projects\youtube-url-downloader\YT_result

============================================================
[1/3] Downloading:
https://www.youtube.com/watch?v=xxxxxxxxxxx
============================================================

...

============================================================
Finished.
Successful: 3/3
Output folder: C:\Projects\youtube-url-downloader\YT_result
============================================================
```

## Output

Files are saved in:

```text
YT_result/
```


For example, if YouTube has these video titles:

```text
Minecraft - Sweden
My Favorite Song
Example Song (Official Audio)
```

the resulting files will be:

```text
YTAudio_result/
├── Minecraft - Sweden.mp3
├── My Favorite Song.mp3
└── Example Song (Official Audio).mp3
```

## Media Quality

The program converts audio to:

```text
MP3 — 160 kbps
```

This setting was chosen as a compromise between audio quality and storage space.

The relevant configuration is:

```python
"preferredquality": "160",
```

You can change it if necessary.

For example:

```python
"preferredquality": "128",
```

uses less storage, while:

```python
"preferredquality": "192",
```

uses more storage and generally provides higher audio quality.

## Configuration

The main configuration is located near the beginning of the Python script:

```python
LINKS_FILE = Path("links.txt")
OUTPUT_DIR = Path("YT_result")
```

You can change these paths if necessary.

The output filename template is:

```python
"outtmpl": str(
    OUTPUT_DIR / "%(title)s.%(ext)s"
),
```

`%(title)s` is replaced by the YouTube video's actual title.

The MP3 conversion is configured with:

```python
"postprocessors": [
    {
        "key": "FFmpegExtractAudio",
        "preferredcodec": "mp3",
        "preferredquality": "160",
    }
]
```

## YouTube API Key

This project **does not require a YouTube API key**.

It uses `yt-dlp` to handle the media extraction instead of the YouTube Data API.

## Handling Failed Downloads

The program is configured to continue when an individual URL fails:

```python
"ignoreerrors": True,
```

This means that if one video cannot be downloaded, the program will move on to the next URL instead of stopping the entire process.

A failed download can happen for reasons such as:

* The video was deleted.
* The video is private.
* The video is unavailable in your region.
* YouTube changed something that temporarily affects extraction.
* The URL is invalid.
* The content requires authentication.

## Existing Files

The program uses:

```python
"nooverwrites": True,
```

so an existing file will not normally be overwritten.

This is useful when running the downloader repeatedly with the same `links.txt`.

## Important Notes

Only download content that you are legally permitted to download and use. YouTube's terms, copyright law, and the rights of the content owner may apply to downloaded material.

This program is intended as a simple personal-use downloader and is not affiliated with YouTube.

YouTube can change its systems at any time. Because `yt-dlp` relies on extracting publicly available media information from YouTube, some videos may occasionally stop working until yt-dlp receives an update.

Keeping yt-dlp updated is therefore recommended:

```bash
python -m pip install -U yt-dlp
```

## Troubleshooting

### `python` is not recognized

Try:

```bash
py --version
```

On some Windows installations, Python is invoked using `py` instead of `python`.

In that case, you can install yt-dlp with:

```bash
py -m pip install -U yt-dlp
```

and run the program with:

```bash
py youtube_url_downloader.py
```

### `No module named 'yt_dlp'`

Install yt-dlp:

```bash
python -m pip install -U yt-dlp
```

### `ffmpeg is not recognized`

FFmpeg is either not installed or its executable directory is not in your `PATH`.

Verify with:

```bash
ffmpeg -version
```

and:

```bash
ffprobe -version
```

### `links.txt was not found`

Make sure `links.txt` is in the same directory from which you are running the program.

For example:

```text
youtube-url-downloader/
├── links.txt
└── youtube_url_downloader.py
```

Then run:

```bash
python youtube_url_downloader.py
```

### Some videos fail while others work

This does not necessarily indicate a problem with the program. Individual YouTube videos can have different restrictions or extraction requirements.

First, update yt-dlp:

```bash
python -m pip install -U yt-dlp
```

Then try the URL again.

## License

This project does not include a specific license by default.
