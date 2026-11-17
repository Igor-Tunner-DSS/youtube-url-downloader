from pathlib import Path
import yt_dlp


LINKS_FILE = Path("links.txt")
OUTPUT_DIR = Path("YT_result")
CHOSEN_FORMAT = "video"

print("="*60)
print("Choose a format: [A]udio | [V]ideo")
print()
ans = input().lower().strip()
if ans in ["a", "audio"]:
    CHOSEN_FORMAT = "audio"
elif ans in ["v", "video"]:
    ...
else:
    print("Not an option. Quitting program")
    exit()


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
    print(f"Saving {'video(s)' if CHOSEN_FORMAT == 'video' else 'audio(s)'} to: {OUTPUT_DIR.resolve()}")
    print()

    ydl_audio_opts = {
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
    ydl_video_opts = {
        # Prefer H.264 video + AAC audio.
        # Fall back to the best single-file MP4 if necessary.
        "format": "bv*[vcodec^=avc1]+ba[acodec^=mp4a]/b[ext=mp4]",

        "outtmpl": str(OUTPUT_DIR / "%(title)s.%(ext)s"),

        "ignoreerrors": True,
        "quiet": True,
        "no_warnings": False,
        "nooverwrites": True,

        # Tell yt-dlp to use MP4 when it has to merge
        # separate video/audio streams.
        "merge_output_format": "mp4",

        "js_runtimes": {"node": {}},
    }

    successful = 0

    ydl_opts = ydl_video_opts if CHOSEN_FORMAT == 'video' else ydl_audio_opts

    with yt_dlp.YoutubeDL(ydl_opts) as ydl: # type: ignore
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