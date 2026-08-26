# YouTube Audio Downloader

A simple Python program that reads YouTube URLs from a `links.txt` file and downloads their audio as MP3 files.

The program uses [`yt-dlp`](https://github.com/yt-dlp/yt-dlp) for downloading and FFmpeg for audio extraction/conversion.

## Features

* Downloads multiple YouTube URLs from a single `links.txt` file.
* Downloads **audio only**, without saving the video.
* Converts the downloaded audio to **MP3**.
* Uses **160 kbps** audio quality as a balance between file size and quality.
* Saves files in a `YTAudio_result` directory.
* Uses the **actual YouTube video title** as the filename.
* Automatically creates the output directory if it does not exist.
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

FFmpeg is required because yt-dlp uses it to extract and convert the downloaded audio.

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
youtube-audio-downloader/
│
├── links.txt
├── youtube_audio_downloader.py
├── README.md
│
└── YTAudio_result/
```

`YTAudio_result` is created automatically the first time the program runs, so you do not need to create it manually.

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
python youtube_audio_downloader.py
```

The program will process every URL in `links.txt`.

Example:

```text
Found 3 URL(s).
Saving audio to: C:\Projects\youtube-audio-downloader\YTAudio_result

============================================================
[1/3] Downloading:
https://www.youtube.com/watch?v=xxxxxxxxxxx
============================================================

...

============================================================
Finished.
Successful: 3/3
Output folder: C:\Projects\youtube-audio-downloader\YTAudio_result
============================================================
```

## Output

Audio files are saved in:

```text
YTAudio_result/
```

The filenames are based on the **actual YouTube titles**.

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

The program does **not** enumerate files as `Song 1`, `Song 2`, etc.

## Audio Quality

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
OUTPUT_DIR = Path("YTAudio_result")
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

Therefore, you do not need to:

* Create a Google Cloud project.
* Enable the YouTube Data API.
* Generate an API key.
* Pay for an API subscription.

There is no API payment requirement for this project.

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
py youtube_audio_downloader.py
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
youtube-audio-downloader/
├── links.txt
└── youtube_audio_downloader.py
```

Then run:

```bash
python youtube_audio_downloader.py
```

### Some videos fail while others work

This does not necessarily indicate a problem with the program. Individual YouTube videos can have different restrictions or extraction requirements.

First, update yt-dlp:

```bash
python -m pip install -U yt-dlp
```

Then try the URL again.

## Full Script

The complete program is:

```python
from pathlib import Path
import yt_dlp


LINKS_FILE = Path("links.txt")
OUTPUT_DIR = Path("YTAudio_result")


def read_links():
    if not LINKS_FILE.exists():
        print(f"ERROR: {LINKS_FILE} was not found.")
        return []

    links = []

    with LINKS_FILE.open("r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            if line.startswith("#"):
                continue

            links.append(line)

    return links


def main():
    links = read_links()

    if not links:
        print("No YouTube URLs found in links.txt.")
        return

    OUTPUT_DIR.mkdir(exist_ok=True)

    print(f"Found {len(links)} URL(s).")
    print(f"Saving audio to: {OUTPUT_DIR.resolve()}")
    print()

    ydl_opts = {
        "format": "bestaudio/best",

        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "160",
            }
        ],

        "outtmpl": str(
            OUTPUT_DIR / "%(title)s.%(ext)s"
        ),

        "noplaylist": True,
        "ignoreerrors": True,
        "quiet": False,
        "no_warnings": False,
        "nooverwrites": True,
    }

    successful = 0

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        for index, url in enumerate(links, start=1):
            print("=" * 60)
            print(f"[{index}/{len(links)}] Downloading:")
            print(url)
            print("=" * 60)

            try:
                result = ydl.download([url])

                if result == 0:
                    successful += 1

            except Exception as error:
                print(f"Failed: {error}")

            print()

    print("=" * 60)
    print("Finished.")
    print(f"Successful: {successful}/{len(links)}")
    print(f"Output folder: {OUTPUT_DIR.resolve()}")
    print("=" * 60)


if __name__ == "__main__":
    main()
```

## License

This project does not include a specific license by default.

If you publish it publicly, consider adding an open-source license such as the MIT License.

## Summary

The basic workflow is:

```text
1. Install Python
       ↓
2. Install yt-dlp
       ↓
3. Install FFmpeg
       ↓
4. Put YouTube URLs in links.txt
       ↓
5. Run youtube_audio_downloader.py
       ↓
6. MP3 files appear in YTAudio_result/
```

No YouTube API key is required, and no paid API or subscription is required.
