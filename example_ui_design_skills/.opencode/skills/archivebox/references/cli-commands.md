# ArchiveBox CLI Commands Reference

Complete reference for ArchiveBox command-line interface.

## Command Overview

| Command | Description |
|---------|-------------|
| `init` | Initialize a new archive collection |
| `add` | Add URLs to the archive |
| `list` | List archived items |
| `status` | Check archive status |
| `remove` | Remove items from archive |
| `server` | Start the web interface |
| `version` | Show version information |
| `help` | Show help for commands |

## init - Initialize Archive

Initialize a new archive collection in the current directory.

```bash
# Basic initialization
archivebox init

# Initialize with setup (recommended for first-time use)
archivebox init --setup
```

The `--setup` flag:
- Installs required JS dependencies
- Creates default configuration
- Sets up the SQLite database

**Options**:
```
--force         Re-initialize even if already configured
--no-input      Skip interactive prompts
```

## add - Add URLs

Add URLs to your archive. Supports single URLs, files, and stdin.

### Single URL

```bash
archivebox add https://example.com
archivebox add https://youtube.com/watch?v=...
archivebox add https://twitter.com/user/status/...
```

### Bulk Import from File

```bash
# Import from text file (one URL per line)
archivebox add < urls.txt

# Import from Netscape bookmark HTML export
archivebox add bookmarks.html

# Import from JSON file
archivebox add urls.json
```

### Stdin Pipeline

```bash
# Pipe URLs from another command
echo "https://example.com" | archivebox add

# Import from file
cat urls.txt | archivebox add

# Import from grep/curl results
grep "http" myfile.txt | archivebox add
```

### Import from Bookmark Services

```bash
# Import from Pinboard
archivebox add 'https://pinboard.in/export/json'

# Import from Pocket (requires API key)
archivebox add 'https://getpocket.com/users/YOUR_USER_ID/feed/YOUR_API_KEY'
```

**Options**:
```
--depth 1          Crawl depth (1 = single page)
--limit 10         Limit number of URLs to process
--timeout 60       Timeout per URL in seconds
```

## list - List Archived Items

View your archived items with various filtering and sorting options.

```bash
# List all items
archivebox list

# List with details (timestamp, title, URL)
archivebox list --verbose

# List as JSON
archivebox list --json

# Limit results
archivebox list --limit 20

# Filter by status
archivebox list --status=200
archivebox list --status=failed

# Filter by content type
archivebox list --type=article
archivebox list --type=video
```

**Output Fields**:
- ID: Unique identifier
- Title: Page title
- URL: Original URL
- Timestamp: When archived
- Status: HTTP status code
- Format: Types of files saved

**Options**:
```
--json          Output as JSON
--csv           Output as CSV
--limit N       Limit to N results
--offset N      Skip first N results
--filter STR    Filter by string
```

## status - Check Archive Status

Get an overview of your archive collection.

```bash
# Basic status
archivebox status

# Detailed status
archivebox status --details

# Include database info
archivebox status --db
```

**Status Information**:
- Total snapshots count
- Disk space used
- Database size
- Pending downloads
- Failed items

## remove - Remove Items

Delete items from your archive.

```bash
# Remove by ID
archivebox remove 12345678_12345678

# Remove multiple by ID
archivebox remove 12345678_12345678 87654321_87654321

# Remove from list output
archivebox list --json | jq '.[] | select(.title | contains("example"))' | archivebox remove
```

**Options**:
```
--delete-files    Also delete archived files
--force           Skip confirmation
```

## server - Start Web Interface

Start the ArchiveBox web UI for browsing and managing your archive.

```bash
# Start on default port (8000)
archivebox server

# Start on custom address and port
archivebox server 0.0.0.0:8000

# Start in background
archivebox server 0.0.0.0:8000 &
```

**Access**: Open `http://localhost:8000` in your browser

**Options**:
```
--debug              Enable debug mode
--reload             Auto-reload on file changes
```

## version - Version Information

```bash
# Show version
archivebox version

# Show extended version info
archivebox version --extended
```

## help - Get Help

```bash
# General help
archivebox help

# Command-specific help
archivebox help add
archivebox help list
```

## Configuration via CLI

Many settings can be overridden via command-line flags:

```bash
# Set Chrome binary path
archivebox add --chrome-binary /usr/bin/chromium https://example.com

# Set timeout
archivebox add --timeout 120 https://example.com

# Disable specific extractors
archivebox add --no-media --no-screenshot https://example.com
```

## Common Workflows

### Daily Bookmark Import

```bash
# Create a script for daily imports
#!/bin/bash
cd ~/archivebox/data
archivebox add < ~/bookmarks/new_bookmarks.txt
archivebox status
```

### Research Project Archiving

```bash
# Initialize project archive
mkdir -p ~/research/archives
cd ~/research/archives
archivebox init --setup

# Add papers and articles
archivebox add https://arxiv.org/pdf/2301.00000.pdf
archivebox add https://example.com/research-paper

# List all archived research
archivebox list --type=article
```

### YouTube Channel Backup

```bash
# Add playlist
archivebox add https://youtube.com/playlist?list=PL...

# Monitor progress
archivebox status

# List downloaded videos
archivebox list --filter youtube
```

## See Also

- [Installation Guide](installation.md)
- [Input Formats](input-formats.md)
- [Troubleshooting](troubleshooting.md)
- [Official CLI Documentation](https://github.com/ArchiveBox/ArchiveBox/wiki/Usage#CLI-Usage)
