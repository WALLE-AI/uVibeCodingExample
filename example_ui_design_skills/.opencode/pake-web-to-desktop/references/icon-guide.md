# App Icon Preparation Guide

## Icon Requirements by Platform

### macOS
- **Format**: `.icns` (preferred) or `.png`
- **Size**: 512x512 pixels minimum (1024x1024 recommended for Retina)
- **Multiple sizes**: Include 16, 32, 64, 128, 256, 512, 1024px versions
- **Tools**: iconutil (macOS), IconComposer, or online converters

### Windows
- **Format**: `.ico` (preferred) or `.png`
- **Size**: 256x256 pixels minimum
- **Multiple sizes**: Include 16, 32, 48, 256px versions
- **Tools**:icotool, GIMP, or online converters

### Linux
- **Format**: `.png` (preferred) or `.svg`
- **Size**: 512x512 pixels minimum
- **Tools**: Inkscape, GIMP, or ImageMagick

## Quick Conversion Commands

### Using ImageMagick (Recommended)

Install ImageMagick first:
```bash
# macOS
brew install imagemagick

# Linux
sudo apt install imagemagick

# Windows
winget install ImageMagick
```

Convert PNG to ICNS (macOS):
```bash
convert icon.png -resize 1024x1024 icon.1024.png
png2icns icon.icns icon.16.png icon.32.png icon.64.png icon.128.png icon.256.png icon.512.png icon.1024.png
```

Convert PNG to ICO (Windows):
```bash
convert icon.png -resize 256x256 icon.ico
# Or combine multiple sizes
convert icon.png -resize 16x16 icon-16.png \
                 -resize 32x32 icon-32.png \
                 -resize 48x48 icon-48.png \
                 -resize 256x256 icon-256.png \
                 icon.ico
```

### Online Tools

- **macOS ICNS**: https://cloudconvert.com/png-to-icns
- **Windows ICO**: https://cloudconvert.com/png-to-ico
- **All formats**: https://convertio.co/png-ico/

## Example Icon Setup

```
project-root/
├── public/
│   ├── icon.png              # Source icon (1024x1024)
│   ├── icon.icns             # macOS icon
│   ├── icon.ico              # Windows icon
│   └── icon.png              # Linux icon (same file)
├── assets/
│   └── icon.icns
└── pake.config.json
```

With config:
```json
{
  "icon": "./public/icon.icns"
}
```

## Generating from SVG

If you have an SVG logo:

```bash
# Install rsvg-convert
brew install librsvg  # macOS

# Convert to PNG at various sizes
rsvg-convert -w 1024 -h 1024 logo.svg -o icon.1024.png
rsvg-convert -w 512 -h 512 logo.svg -o icon.512.png
rsvg-convert -w 256 -h 256 logo.svg -o icon.256.png
rsvg-convert -w 128 -h 128 logo.svg -o icon.128.png
```

## Common Issues

### Icon Not Appearing

1. Verify icon file exists and is readable
2. Check file format matches expected type
3. Ensure sufficient file size (not 0 bytes)
4. Try absolute path in config

### Blurry Icons

Use 1024x1024 for macOS and 256x256 for Windows as source.

### Transparency Issues

Ensure PNG has proper alpha channel transparency.
