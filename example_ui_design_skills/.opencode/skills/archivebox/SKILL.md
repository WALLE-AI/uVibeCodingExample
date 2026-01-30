---
name: archivebox
description: Self-hosted web archiving via CLI. Archive URLs to HTML, PDF, PNG, WARC, and more using pip-installed ArchiveBox. Supports 20+ import sources.
---

# ArchiveBox Web Archiving

Use ArchiveBox to save and preserve web content locally. Archive websites in multiple formats for long-term storage, research, or backup purposes.

## When to Use

- **Bookmark preservation**: Save important articles and resources before they disappear
- **Research archiving**: Preserve academic papers, documentation, and reference materials
- **Evidence collection**: Capture web content for legal or journalistic purposes
- **Social media backup**: Archive posts from Twitter, Reddit, and other platforms
- **Offline access**: Create offline copies of frequently visited sites

## Quick Start

```bash
# Install ArchiveBox and dependencies
pip install archivebox yt-dlp playwright
playwright install --with-deps chromium

# Initialize your archive
mkdir -p ~/archivebox/data && cd ~/archivebox/data
archivebox init --setup

# Add URLs to archive
archivebox add https://example.com

# View archived items
archivebox list

# Start web interface (optional)
archivebox server 0.0.0.0:8000
```

Open `http://localhost:8000` to browse your archive via web UI.

## Installation

See [Installation Guide](references/installation.md) for detailed setup instructions including:
- Python and Node.js requirements
- Complete pip installation steps
- Initialization process
- Dependency verification

## CLI Commands

ArchiveBox provides a comprehensive CLI for managing your archive.

| Command | Description |
|---------|-------------|
| `archivebox init` | Initialize a new archive collection |
| `archivebox add` | Add URLs to the archive |
| `archivebox list` | List archived items |
| `archivebox status` | Check archive status |
| `archivebox remove` | Remove items from archive |
| `archivebox server` | Start the web interface |
| `archivebox help` | Show help information |

See [CLI Commands Reference](references/cli-commands.md) for detailed usage examples.

## Input Formats

ArchiveBox supports importing from multiple sources:

- **Single URL**: Add one URL directly
- **URL list**: Import from text files or stdin
- **Browser bookmarks**: Netscape HTML bookmark exports
- **Bookmark services**: Pinboard, Pocket, Shaarli, Wallabag
- **RSS feeds**: Import from RSS/Atom subscriptions
- **Browser history**: Chrome and Firefox history exports

See [Input Formats](references/input-formats.md) for all supported import methods.

## Output Formats

ArchiveBox saves each snapshot in multiple redundant formats:

| Format | Purpose |
|--------|---------|
| **HTML** | Original page source |
| **PDF** | Print-ready document |
| **PNG** | Screenshot of the page |
| **WARC** | Web archive format for replay |
| **JSON** | Metadata and extracted content |
| **TXT** | Full text extraction |
| **MP3/MP4** | Media files from YouTube, etc. |

## Configuration

ArchiveBox uses `ArchiveBox.conf` for settings. Key options:

```bash
# Key configuration variables
SAVE_ARCHIVE_DOT_ORG=False      # Disable archive.org backup
CHROME_BINARY=/usr/bin/chromium # Chrome executable path
MEDIA_TIMEOUT=300               # Media download timeout (seconds)
MAX_MEDIA_SIZE=0                # Max media file size (0=unlimited)
```

Configuration file location: `~/archivebox/data/ArchiveBox.conf`

## Troubleshooting

Common issues and solutions:

- **Chrome/Chromium not found**: Install browser and set CHROME_BINARY
- **Permission denied**: Ensure write access to data directory
- **Timeout errors**: Increase MEDIA_TIMEOUT for large downloads
- **Media extraction failed**: Install/update yt-dlp

See [Troubleshooting Guide](references/troubleshooting.md) for detailed solutions.

## See Also

- [Installation Guide](references/installation.md)
- [CLI Commands Reference](references/cli-commands.md)
- [Input Formats Guide](references/input-formats.md)
- [Troubleshooting Guide](references/troubleshooting.md)
- [Official Documentation](https://github.com/ArchiveBox/ArchiveBox/wiki)
