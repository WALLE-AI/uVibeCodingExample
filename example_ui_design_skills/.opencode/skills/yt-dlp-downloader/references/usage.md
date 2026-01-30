# yt-dlp Usage Reference

## Supported Sites

yt-dlp supports 1000+ sites including:
- YouTube, Vimeo, Bilibili, Dailymotion
- Twitter/X, TikTok, Reddit
- And many more...

## Download Options

### Best 1080p MP4 (Default)
```
yt-dlp --js-runtimes deno -f "bestvideo[height<=1080][ext=mp4]+bestaudio[ext=m4a]" URL
```

### Audio Only (MP3)
```
yt-dlp -x --audio-format mp3 URL
```

### Download with Subtitles
```
yt-dlp --write-subs --sub-langs en URL
```

### Specific Quality
```
yt-dlp -f "best[height=720]" URL
```

## Performance Optimization

| Component | Benefit |
|-----------|---------|
| Deno | 3-5x faster YouTube extraction |
| FFmpeg | Faster video/audio merging |
| Concurrent downloads | Use `-N 4` for parallel fragments |

## Troubleshooting

### "No supported JavaScript runtime"
Install Deno: Run `scripts/install.bat` or manually install from deno.land

### "Unable to extract video data"
Update yt-dlp: `pip install -U yt-dlp`

### "ffmpeg not found"
Install FFmpeg: `winget install FFmpeg` or download from ffmpeg.org

### Slow downloads
1. Install Deno (enables faster extraction)
2. Use `--js-runtimes deno` flag
3. Check network connection

### Download fails
- Check URL accessibility in browser
- Some sites block automated downloads
- Try with `--cookies-from-browser chrome`
