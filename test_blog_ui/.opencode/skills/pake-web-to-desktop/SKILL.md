---
name: pake-web-to-desktop
description: Package frontend web projects (React/Vue/Next/Vite) into native desktop apps using Pake CLI. Turn any web app into a lightweight, cross-platform desktop application with native performance and smaller file size (~5MB vs ~100MB for Electron).
---

# Pake Web-to-Desktop Packaging

Use Pake to convert frontend web projects into native desktop applications for macOS, Windows, and Linux.

## When to Use

- User wants to package a built web project as a desktop app
- User needs to convert a URL/web app to a standalone executable
- User wants smaller, faster desktop apps compared to Electron alternatives
- User needs to support macOS/Windows/Linux from the same source

## Prerequisites

### System Requirements

- **Node.js**: >= 22
- **Rust**: >= 1.85
- **pnpm**: Recommended package manager (or npm/yarn)

### Install Pake CLI

```bash
# Install globally via pnpm (recommended)
pnpm install -g pake-cli

# Or via npm
npm install -g pake-cli

# Or via yarn
yarn global add pake-cli
```

## Packaging Workflow

### Step 1: Build Your Web Project

Navigate to your frontend project and build for production:

**React/Vue/Vite projects:**
```bash
npm run build
# or
pnpm build
# Output typically in: dist/, build/, or .next/
```

**Next.js projects:**
```bash
npm run build
# Output in: .next/
```

### Step 2: Serve the Built Files

Pake needs your built files served via HTTP. Use a local server:

**Option A: Using npx serve (quickest)**
```bash
# Serve dist/ folder on port 3000
npx serve dist -l 3000
```

**Option B: Using Python**
```bash
# Python 3
python -m http.server 3000 --directory dist/

# Python 2
python -m SimpleHTTPServer 3000
```

**Option C: Using project dev server**
```bash
npm run preview
# or
pnpm preview
```

### Step 3: Package with Pake

In a new terminal, run Pake with your local URL:

```bash
# Basic packaging (auto-fetches icon)
pake http://localhost:3000 --name "MyApp"

# Advanced options
pake http://localhost:3000 \
  --name "MyApp" \
  --width 1200 \
  --height 800 \
  --hide-title-bar
```

## Common Options

| Option | Description | Default |
|--------|-------------|---------|
| `--name` | App name for the packaged application | Domain name |
| `--icon` | Path or URL to app icon (.icns/.png) | Auto-fetched |
| `--width` | Window width in pixels | 1200 |
| `--height` | Window height in pixels | 800 |
| `--hide-title-bar` | Hide window title bar for immersive experience | false |
| `--fullscreen` | Start in fullscreen mode | false |
| `--transparent` | Enable transparent window (macOS) | false |
| `--resizable` | Allow window resizing | true |
| `--title-bar-style` | macOS title bar style: standard/hidden | standard |

## Complete CLI Reference

```bash
pake [URL] [OPTIONS]

Options:
  -n, --name <string>          Application name
  -i, --icon <path>            Icon file path or URL
  -w, --width <number>         Window width (pixels)
  -h, --height <number>        Window height (pixels)
  --min-width <number>         Minimum window width
  --min-height <number>        Minimum window height
  --max-width <number>         Maximum window width
  --max-height <number>        Maximum window height
  --hide-title-bar             Hide title bar (immersive mode)
  --transparent                Enable transparency (macOS)
  --fullscreen                 Start in fullscreen
  --resizable                  Allow window resizing
  --borderless                  Borderless window
  --title-bar-style <style>    Title bar style (macOS)
  --always-on-top              Keep window always on top
  --debug                      Enable debug mode
  --platform <target>          Target platform: macos/windows/linux
  -c, --config <path>          Config file path
  -h, --help                   Show help
  -v, --version                Show version
```

## Quick Examples

### React App
```bash
cd my-react-app
npm run build
npx serve build -l 3000 &
pake http://localhost:3000 --name "MyReactApp"
```

### Vue App
```bash
cd my-vue-app
pnpm build
npx serve dist -l 3000 &
pake http://localhost:3000 --name "MyVueApp" --hide-title-bar
```

### Next.js App
```bash
cd my-next-app
npm run build
npx serve .next/static .next/pages public -l 3000 &
pake http://localhost:3000 --name "MyNextApp" --width 1400 --height 900
```

### With Custom Icon
```bash
pake http://localhost:3000 \
  --name "MyApp" \
  --icon ./assets/icon.icns \
  --width 1200 \
  --height 800 \
  --hide-title-bar
```

## Production Build

For final distribution, build targeting specific platforms:

```bash
# macOS
pake http://localhost:3000 --name "MyApp" --platform macos

# Windows  
pake http://localhost:3000 --name "MyApp" --platform windows

# Linux
pake http://localhost:3000 --name "MyApp" --platform linux
```

## Configuration File

Create `pake.config.json` for complex projects:

```json
{
  "name": "MyWebApp",
  "url": "http://localhost:3000",
  "icon": "./assets/icon.icns",
  "width": 1400,
  "height": 900,
  "hide-title-bar": true,
  "fullscreen": false,
  "shortcuts": {
    "refresh": "CmdOrCtrl+R"
  }
}
```

Run with config:
```bash
pake --config pake.config.json
```

## Troubleshooting

### Port Issues

Ensure your dev server runs on a stable port. Use `--port` flag:
```bash
npx serve dist -l 3001
pake http://localhost:3001 --name "MyApp"
```

### Icon Not Found

Provide icon explicitly:
```bash
pake http://localhost:3000 --name "MyApp" --icon ./public/icon.png
```

### Build Fails on Windows

Ensure Rust toolchain is installed:
```bash
# Install via rustup
winget install Rustlang.Rust.MSVC

# Then restart terminal and install Pake
pnpm install -g pake-cli
```

### macOS Notarization

For distribution outside App Store, see [Pake docs](https://github.com/tw93/Pake) for notarization setup.

## Output Location

Packaged apps are saved to:
- **macOS**: `.dmg` file
- **Windows**: `.msi` file  
- **Linux**: `.deb` file

Files typically appear in the current directory or `dist/` folder.

## Key Features

- **Lightweight**: ~5MB vs ~100MB for Electron apps
- **Fast**: Rust Tauri framework, lower memory usage
- **Native**: Real desktop app, not a wrapped browser
- **Cross-platform**: Single command for macOS/Windows/Linux
- **Immersive**: Hide title bar, fullscreen support
- **Keyboard shortcuts**: Built-in navigation and zoom controls

## See Also

- [Framework-Specific Build Commands](references/frameworks.md)
- [Configuration Examples](references/config-examples.md)
- [Icon Preparation Guide](references/icon-guide.md)
- [Pake GitHub](https://github.com/tw93/Pake)
- [CLI Usage Guide](https://github.com/tw93/Pake/blob/main/docs/cli-usage.md)
- [GitHub Actions Building](https://github.com/tw93/Pake/blob/main/docs/github-actions-usage.md)
