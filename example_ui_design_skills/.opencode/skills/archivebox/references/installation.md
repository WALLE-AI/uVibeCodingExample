# ArchiveBox Installation Guide

Complete guide to installing ArchiveBox via pip on Linux, macOS, and Windows.

## System Requirements

### Python
- **Version**: Python 3.10 or higher
- **Check installed version**:
  ```bash
  python3 --version
  ```

### Node.js
- **Version**: Node.js 18 or higher
- **Check installed version**:
  ```bash
  node --version
  ```

### Chrome/Chromium
- Required for rendering JavaScript-heavy pages
- Must be installed and accessible in PATH
- Or specify path via `CHROME_BINARY` configuration

## Installation Steps

### Step 1: Install Python and Node.js

**macOS (using Homebrew)**:
```bash
brew install python@3.11 node
```

**Ubuntu/Debian**:
```bash
sudo apt update
sudo apt install python3.11 python3-pip nodejs npm
```

**Windows**:
- Download from [python.org](https://www.python.org/downloads/)
- Download from [nodejs.org](https://nodejs.org/)

### Step 2: Install ArchiveBox and Dependencies

```bash
# Install ArchiveBox with required dependencies
pip install --upgrade archivebox yt-dlp playwright

# Install Chromium browser and system dependencies
playwright install --with-deps chromium
```

### Step 3: Initialize ArchiveBox

```bash
# Create and enter archive directory
mkdir -p ~/archivebox/data
cd ~/archivebox/data

# Initialize the archive (this creates config files and installs JS dependencies)
archivebox init --setup
```

The `init --setup` command:
- Creates `ArchiveBox.conf` configuration file
- Sets up SQLite database
- Installs JS dependencies (singlefile, readability, mercury)

## Verify Installation

```bash
# Check ArchiveBox version
archivebox version

# Verify dependencies
archivebox doctor

# View help
archivebox help
```

## Directory Structure

After initialization, your archive directory contains:

```
~/archivebox/data/
├── ArchiveBox.conf          # Configuration file
├── archive.db              # SQLite database
├── log.txt                # Activity log
└── archive/
    └── (archived snapshots)
```

## Docker Alternative (Not Recommended)

For Docker-based installation (not covered in this skill):
```bash
mkdir -p ~/archivebox/data && cd ~/archivebox
curl -fsSL 'https://docker-compose.archivebox.io' > docker-compose.yml
docker compose run archivebox init --setup
```

## Next Steps

- Add URLs to your archive: `archivebox add <URL>`
- Import bookmarks or URL lists
- Start web interface: `archivebox server 0.0.0.0:8000`

## See Also

- [CLI Commands](cli-commands.md)
- [Input Formats](input-formats.md)
- [Troubleshooting](troubleshooting.md)
