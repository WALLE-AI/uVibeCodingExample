# ArchiveBox Troubleshooting Guide

Solutions to common issues when using ArchiveBox.

## Dependency Issues

### Chrome/Chromium Not Found

**Error**:
```
Chrome executable not found at /usr/bin/google-chrome
```

**Solutions**:

1. **Install Chrome/Chromium**:
   ```bash
   # Ubuntu/Debian
   sudo apt install chromium chromium-driver

   # macOS (Homebrew)
   brew install --cask google-chrome

   # Fedora/RHEL
   sudo dnf install chromium
   ```

2. **Set Chrome binary path**:
   ```bash
   # Find Chrome location
   which google-chrome     # Google Chrome
   which chromium-browser  # Chromium

   # Set in ArchiveBox.conf
   echo "CHROME_BINARY=/usr/bin/chromium" >> ~/archivebox/data/ArchiveBox.conf
   ```

3. **Verify Chrome works**:
   ```bash
   chromium --version
   google-chrome --version
   ```

### Python Version Issues

**Error**:
```
ArchiveBox requires Python 3.10 or higher
```

**Solutions**:

1. **Check Python version**:
   ```bash
   python3 --version
   ```

2. **Install newer Python**:
   ```bash
   # Ubuntu/Debian
   sudo apt install python3.11 python3.11-venv python3.11-dev

   # macOS (Homebrew)
   brew install python@3.11

   # Using pyenv
   pyenv install 3.11.0
   pyenv local 3.11.0
   ```

### Node.js Not Found

**Error**:
```
Node.js is required but was not found
```

**Solutions**:

1. **Install Node.js**:
   ```bash
   # Ubuntu/Debian
   sudo apt install nodejs npm

   # macOS (Homebrew)
   brew install node

   # Using nvm
   curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
   nvm install 18
   ```

2. **Verify installation**:
   ```bash
   node --version
   npm --version
   ```

### Playwright Issues

**Error**:
```
playwright._impl.api_types.browser_browser_type.Error: 
Browser browser not found. Unable to connect.
```

**Solutions**:

1. **Install Chromium via Playwright**:
   ```bash
   playwright install --with-deps chromium
   ```

2. **If using system Chrome, set the path**:
   ```bash
   echo "CHROME_BINARY=/usr/bin/chromium" >> ~/archivebox/data/ArchiveBox.conf
   ```

3. **Reinstall Playwright browsers**:
   ```bash
   playwright install
   playwright install-deps
   ```

### yt-dlp Issues

**Error**:
```
ExtractorError: Failed to download video
```

**Solutions**:

1. **Update yt-dlp**:
   ```bash
   pip install --upgrade yt-dlp
   ```

2. **Install ffmpeg** (required for merging video/audio):
   ```bash
   # Ubuntu/Debian
   sudo apt install ffmpeg

   # macOS
   brew install ffmpeg
   ```

3. **Verify ffmpeg**:
   ```bash
   ffmpeg -version
   ```

## Permission Issues

### Write Permission Denied

**Error**:
```
PermissionError: [Errno 13] Permission denied: '/home/user/archivebox/data/log.txt'
```

**Solutions**:

1. **Fix directory permissions**:
   ```bash
   chmod -R 755 ~/archivebox/data
   chown -R $USER:$USER ~/archivebox/data
   ```

2. **Create directory with correct permissions**:
   ```bash
   mkdir -p ~/archivebox/data
   chmod 755 ~/archivebox/data
   cd ~/archivebox/data
   ```

3. **Run ArchiveBox as current user** (avoid sudo):
   ```bash
   archivebox init --setup
   archivebox add https://example.com
   ```

### Docker Permission Issues

If using Docker, ensure user is in docker group:
```bash
sudo usermod -aG docker $USER
newgrp docker
```

## Network Issues

### Timeout Errors

**Error**:
```
ExtractorError: Timed out
```

**Solutions**:

1. **Increase timeout**:
   ```bash
   archivebox add --timeout 300 https://slow-site.com
   ```

2. **Set default timeout in config**:
   ```bash
   echo "TIMEOUT=300" >> ~/archivebox/data/ArchiveBox.conf
   ```

### Proxy Configuration

**Error**:
```
ConnectionError
```

**Solutions**:

1. **Set environment variables**:
   ```bash
   export HTTP_PROXY="http://proxy.example.com:8080"
   export HTTPS_PROXY="http://proxy.example.com:8080"
   archivebox add https://example.com
   ```

2. **Configure in ArchiveBox.conf**:
   ```bash
   echo "HTTP_PROXY=http://proxy.example.com:8080" >> ~/archivebox/data/ArchiveBox.conf
   echo "HTTPS_PROXY=http://proxy.example.com:8080" >> ~/archivebox/data/ArchiveBox.conf
   ```

### SSL/TLS Errors

**Error**:
```
SSLError: certificate verify failed
```

**Solutions**:

1. **Disable SSL verification (not recommended)**:
   ```bash
   echo "VERIFY_SSL=False" >> ~/archivebox/data/ArchiveBox.conf
   ```

2. **Update certificates**:
   ```bash
   # Ubuntu/Debian
   sudo apt update && sudo apt install ca-certificates

   # macOS
   brew install ca-certificates
   ```

## Archive Issues

### Duplicate URLs

**Error**:
```
URL already in archive
```

**Solutions**:

1. **Check existing URLs**:
   ```bash
   archivebox list --json | jq '.[].url'
   ```

2. **Filter before adding**:
   ```bash
   cat new_urls.txt | while read url; do
       if ! archivebox list --json | jq -r '.[].url' | grep -q "^$url$"; then
           archivebox add "$url"
       fi
   done
   ```

3. **Force re-archive (updates existing)**:
   ```bash
   archivebox add --force https://example.com
   ```

### Incomplete Archives

**Error**:
```
Snapshot incomplete: missing files
```

**Solutions**:

1. **Check snapshot status**:
   ```bash
   archivebox list --status=failed
   ```

2. **Re-download failed items**:
   ```bash
   archivebox add https://failed-url.com
   ```

3. **Check extraction logs**:
   ```bash
   tail -f ~/archivebox/data/log.txt
   ```

### Disk Space Issues

**Error**:
```
OSError: [Errno 28] No space left on device
```

**Solutions**:

1. **Check disk space**:
   ```bash
   df -h ~/archivebox/data
   ```

2. **Clean up old archives**:
   ```bash
   # Remove failed or old snapshots
   archivebox remove --status=failed

   # Clear media cache
   rm -rf ~/archivebox/data/archive/*/media
   ```

3. **Set size limits**:
   ```bash
   echo "MAX_MEDIA_SIZE=100" >> ~/archivebox/data/ArchiveBox.conf  # 100MB limit
   ```

## Web UI Issues

### Cannot Access Web UI

**Error**:
```
Connection refused on http://localhost:8000
```

**Solutions**:

1. **Start the server**:
   ```bash
   cd ~/archivebox/data
   archivebox server 0.0.0.0:8000
   ```

2. **Check if port is in use**:
   ```bash
   lsof -i :8000
   # or
   netstat -ano | findstr :8000
   ```

3. **Use different port**:
   ```bash
   archivebox server 0.0.0.0:9000
   ```

### Admin Login Issues

**Error**:
```
Authentication failed
```

**Solutions**:

1. **Reset admin password**:
   ```bash
   archivebox manage createsuperuser
   ```

2. **Recreate database with new admin**:
   ```bash
   rm ~/archivebox/data/archive.db
   archivebox init --setup
   ```

### Slow Web UI

**Solutions**:

1. **Check system resources**:
   ```bash
   htop
   df -h
   ```

2. **Limit archived items per page**:
   Configure in ArchiveBox settings

3. **Clear cache**:
   ```bash
   rm -rf ~/archivebox/data/__pycache__
   ```

## Performance Issues

### Slow Archiving

**Solutions**:

1. **Reduce extractors**:
   ```bash
   echo "ONLY_ARCHIVE_METHOD=html" >> ~/archivebox/data/ArchiveBox.conf
   ```

2. **Limit concurrent downloads**:
   ```bash
   echo "MAX_CONCURRENT_DOWNLOADS=2" >> ~/archivebox/data/ArchiveBox.conf
   ```

3. **Disable media downloads**:
   ```bash
   echo "SAVE_MEDIA=False" >> ~/archivebox/data/ArchiveBox.conf
   ```

### High Memory Usage

**Solutions**:

1. **Limit item size**:
   ```bash
   echo "MAX_TITLE_LENGTH=100" >> ~/archivebox/data/ArchiveBox.conf
   echo "MAX_TEXT_LENGTH=100000" >> ~/archivebox/data/ArchiveBox.conf
   ```

2. **Disable screenshot generation**:
   ```bash
   echo "SAVE_SCREENSHOT=False" >> ~/archivebox/data/ArchiveBox.conf
   ```

## Database Issues

### Corrupted Database

**Error**:
```
DatabaseError: database disk image is malformed
```

**Solutions**:

1. **Repair SQLite database**:
   ```bash
   sqlite3 ~/archivebox/data/archive.db ".recover" > ~/archivebox/data/archive_recovered.db
   mv ~/archivebox/data/archive.db ~/archivebox/data/archive.db.bak
   mv ~/archivebox/data/archive_recovered.db ~/archivebox/data/archive.db
   ```

2. **Rebuild from scratch** (last resort):
   ```bash
   mkdir ~/archivebox/backup
   cp -r ~/archivebox/data/archive/* ~/archivebox/backup/
   rm ~/archivebox/data/archive.db
   archivebox init --setup
   ```

### Database Locked

**Error**:
```
Database is locked
```

**Solutions**:

1. **Close other processes**:
   ```bash
   # Check for running ArchiveBox processes
   ps aux | grep archivebox
   ```

2. **Wait for background processes**:
   ```bash
   # If server is running, stop it
   pkill -f "archivebox server"
   ```

## Getting Help

### Check Logs

```bash
# View recent logs
tail -50 ~/archivebox/data/log.txt

# Search for errors
grep -i error ~/archivebox/data/log.txt

# Watch logs in real-time
tail -f ~/archivebox/data/log.txt
```

### Run Diagnostics

```bash
# Check system requirements
archivebox doctor
archivebox version --extended
```

### Common Error Messages

| Error Message | Quick Fix |
|---------------|-----------|
| Chrome not found | Install Chrome or set CHROME_BINARY |
| Node.js not found | Install Node.js 18+ |
| Database locked | Stop other ArchiveBox processes |
| Permission denied | Fix directory permissions |
| Connection timeout | Increase TIMEOUT value |
| SSL verification failed | Update certificates or set VERIFY_SSL=False |
| No space left on device | Clean up disk space |

### Community Support

- [ArchiveBox Wiki](https://github.com/ArchiveBox/ArchiveBox/wiki)
- [ArchiveBox Issues](https://github.com/ArchiveBox/ArchiveBox/issues)
- [ArchiveBox Discussions](https://github.com/ArchiveBox/ArchiveBox/discussions)

## See Also

- [Installation Guide](installation.md)
- [CLI Commands](cli-commands.md)
- [Input Formats](input-formats.md)
- [Official Troubleshooting](https://github.com/ArchiveBox/ArchiveBox/wiki/Troubleshooting)
