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
        # Audio only
        "format": "bestaudio/best",

        # Convert to MP3
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",

                # Medium quality.
                # 128K = smaller files
                # 160K = medium/balanced
                # 192K = higher quality
                "preferredquality": "160",
            }
        ],

        # Output filename
        "outtmpl": str(
            OUTPUT_DIR / "%(title)s.%(ext)s"
        ),

        # Do not download video
        "noplaylist": True,

        # Continue with the next URL if one fails
        "ignoreerrors": True,

        # Show normal download progress
        "quiet": False,
        "no_warnings": False,

        # Avoid overwriting an existing file
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