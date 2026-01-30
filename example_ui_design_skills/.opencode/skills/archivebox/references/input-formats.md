# ArchiveBox Input Formats Guide

Guide to importing URLs and content into ArchiveBox from various sources.

## Input Methods Overview

| Method | Command | Use Case |
|--------|---------|----------|
| **Single URL** | `archivebox add <URL>` | Quick single-page archive |
| **Text File** | `archivebox add < file.txt` | Bulk import from text |
| **Netscape HTML** | `archivebox add bookmarks.html` | Browser bookmark exports |
| **JSON** | `archivebox add data.json` | Structured URL lists |
| **RSS/Atom** | `archivebox add feed.xml` | Subscribe feed archive |
| **Pinboard** | `archivebox add https://pinboard.in/export/json` | Pinboard import |
| **Pocket** | `archivebox add https://getpocket.com/...` | Pocket import |
| **Stdin** | `echo "<URL>" \| archivebox add` | Pipeline integration |

## Single URL Import

The simplest way to archive a single page.

```bash
archivebox add https://example.com
archivebox add https://youtube.com/watch?v=dQw4w9WgXcQ
archivebox add https://twitter.com/user/status/1234567890
```

**Features**:
- Automatic title extraction
- Content type detection (article, video, image)
- Screenshot and PDF generation
- Media extraction (YouTube, SoundCloud, etc.)

## Text File Import

Import multiple URLs from plain text files.

### Format Requirements
- One URL per line
- Blank lines are ignored
- Lines starting with # are comments

### Example File (urls.txt)
```
# My research bookmarks
https://arxiv.org/abs/2301.00001
https://example.com/paper-1
https://github.com/user/repo

# News articles
https://news.example.com/article-1
https://blog.example.com/post
```

### Import Command
```bash
archivebox add < urls.txt

# Or specify file path
archivebox add ./path/to/urls.txt
```

## Netscape Bookmark Import

Import browser bookmarks exported as HTML.

### Export Bookmarks

**Chrome**:
1. Bookmarks Manager (Ctrl+Shift+O)
2. Export bookmarks

**Firefox**:
1. Library > Bookmarks > Export Bookmarks

### Import Command
```bash
archivebox add bookmarks_1_15_2024.html
```

ArchiveBox extracts:
- URL
- Title (from bookmark name)
- Add date (if available)
- Folder structure (as tags)

## JSON Import

Import URLs from structured JSON files.

### Format Options

**Simple array**:
```json
[
    "https://example.com/page1",
    "https://example.com/page2"
]
```

**Extended format** (with metadata):
```json
[
    {
        "url": "https://example.com/article",
        "title": "Article Title",
        "tags": ["research", "2024"],
        "timestamp": "2024-01-15T10:30:00Z"
    }
]
```

**Pinboard JSON export**:
```json
{
    "href": "https://example.com",
    "description": "Page Title",
    "tags": "tag1,tag2",
    "time": "2024-01-15T10:30:00Z"
}
```

### Import Command
```bash
archivebox add urls.json
archivebox add pinboard_export.json
```

## RSS/Atom Feed Import

Import and archive items from RSS or Atom feeds.

### Feed File Format (feed.xml)
```xml
<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
<channel>
    <title>My Feed</title>
    <item>
        <title>Article 1</title>
        <link>https://example.com/article1</link>
    </item>
    <item>
        <title>Article 2</title>
        <link>https://example.com/article2</link>
    </item>
</channel>
</rss>
```

### Import Command
```bash
archivebox add feed.xml
```

ArchiveBox will:
- Parse feed items
- Extract article links
- Queue each URL for archiving
- Preserve post timestamps

## Bookmark Services

### Pinboard

1. Export bookmarks from Pinboard:
   - Go to https://pinboard.in/export/
   - Select JSON format

2. Import:
   ```bash
   archivebox add pinboard_export.json
   ```

### Pocket

1. Get your RSS feed URL:
   - https://getpocket.com/users/YOUR_USER_ID/feed/YOUR_API_KEY

2. Import:
   ```bash
   archivebox add 'https://getpocket.com/users/user123/feed/abcdef123456'
   ```

### Wallabag

1. Export articles via Wallabag API or UI
2. Import JSON export

### Shaarli

1. Export links from Shaarli
2. Import JSON or HTML format

## Stdin Pipeline

Integrate ArchiveBox with other command-line tools.

```bash
# Echo single URL
echo "https://example.com" | archivebox add

# From file with filtering
cat urls.txt | grep "https://" | archivebox add

# From curl results
curl -s "https://example.com/links.json" | jq -r '.[]' | archivebox add

# From database query
sqlite3 archive.db "SELECT url FROM bookmarks WHERE archived=0" | archivebox add

# From grep output
grep -r "http" ./data/ | archivebox add
```

## Browser History Import

### Chrome

1. Export history to CSV (requires extension or SQLite query)
2. Extract URLs to text file
3. Import with ArchiveBox

### Firefox

1. Export history or use SQLite database
2. Extract unique URLs
3. Import

**Note**: Browser history imports may contain many duplicate or expired URLs.

## Advanced Import Patterns

### Filter and Import

```bash
# Import only HTTPS URLs
cat urls.txt | grep "^https://" | archivebox add

# Import only specific domain
cat urls.txt | grep "example.com" | archivebox add

# Exclude already archived
cat urls.txt | while read url; do
    if ! archivebox list --json | jq -r '.[].url' | grep -q "$url"; then
        echo "$url"
    fi
done | archivebox add
```

### Incremental Import

```bash
#!/bin/bash
# Add only new URLs since last import

cd ~/archivebox/data

# Get existing URLs
archivebox list --json > /tmp/existing_urls.json

# Filter new URLs from source
cat new_urls.txt | while read url; do
    if ! jq -r '.[].url' /tmp/existing_urls.json | grep -q "^$url$"; then
        echo "$url"
    fi
done > /tmp/new_only.txt

# Import new URLs
archivebox add < /tmp/new_only.txt
```

### Scheduled Import

Create a cron job for regular imports:

```bash
# Edit crontab
crontab -e

# Add line to import bookmarks daily at 2 AM
0 2 * * * cd ~/archivebox/data && archivebox add < ~/bookmarks/daily.txt
```

## Import Limits and Timeouts

```bash
# Limit import rate
archivebox add --limit 50 < urls.txt

# Increase timeout for slow sites
archivebox add --timeout 120 < urls.txt

# Depth control (crawling linked pages)
archivebox add --depth 1 < urls.txt
```

## Troubleshooting Imports

| Issue | Solution |
|-------|----------|
| URLs not importing | Check URL format (must start with http:// or https://) |
| Encoding errors | Ensure file is UTF-8 encoded |
| Import too slow | Use `--limit` and `--timeout` flags |
| Duplicates | Filter before importing |
| Special characters | Use proper JSON encoding |

## Supported URL Types

| Type | Example | Notes |
|------|---------|-------|
| **HTTP/HTTPS** | https://example.com | Standard web pages |
| **YouTube** | https://youtube.com/watch?v=... | Video + metadata |
| **Twitter/X** | https://twitter.com/user/status/... | Tweet + media |
| **GitHub** | https://github.com/user/repo | Repository + README |
| **PDF** | https://example.com/paper.pdf | Direct PDF archive |
| **RSS** | https://example.com/feed.xml | Feed items archived |

## See Also

- [CLI Commands](cli-commands.md)
- [Installation Guide](installation.md)
- [Troubleshooting](troubleshooting.md)
- [Official Input Documentation](https://github.com/ArchiveBox/ArchiveBox/wiki/Input-Formats)
