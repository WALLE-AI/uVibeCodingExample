---
name: yt-dlp-downloader
description: Download videos from 1000+ sites using yt-dlp on Windows. Supports batch download, 1080p MP4 format, playlist URLs. Optimized for fast download with JS runtime (Deno) and FFmpeg.
---

# Video Downloader (yt-dlp)

## Quick Start

1. First run `scripts/install.bat` to install yt-dlp + Deno (JS runtime) + FFmpeg
2. Run `scripts/download.bat "URL1" "URL2" ...` to download videos

## Workflow

1. **Install dependencies** (first time only):
   ```
   scripts/install.bat
   ```
   Installs: yt-dlp, Deno (for faster YouTube extraction), FFmpeg (for merging video/audio)

2. **Download videos**:
   ```
   scripts/download.bat "https://youtube.com/watch?v=..." "https://vimeo.com/..."
   ```

3. **Download playlist**:
   ```
   scripts/download.bat "https://youtube.com/playlist?list=..."
   ```

## Output

- Files saved to current directory
- Naming format: `title_id.ext`
- Format: 1080p MP4 (best available quality)

## Features

- **Fast download**: Deno JS runtime for optimized extraction
- **Batch download**: Multiple URLs in one command
- **Playlist support**: Automatically downloads all videos
- **Auto-merge**: FFmpeg merges video and audio tracks
- **1000+ sites**: YouTube, Vimeo, Bilibili, etc.

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Slow download | Run `scripts/install.bat` to install Deno |
| Missing formats | Update yt-dlp: `pip install -U yt-dlp` |
| No audio | Install FFmpeg via `scripts/install.bat` |
