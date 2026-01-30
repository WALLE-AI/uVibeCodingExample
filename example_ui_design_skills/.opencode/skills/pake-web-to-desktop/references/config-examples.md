# Pake Configuration Examples

## Minimal Config

```json
{
  "name": "MyApp",
  "url": "http://localhost:3000"
}
```

## Full Featured Config

```json
{
  "name": "MyWebApp",
  "url": "http://localhost:3000",
  "icon": "./assets/icon.icns",
  "width": 1400,
  "height": 900,
  "hide-title-bar": true,
  "fullscreen": false,
  "transparent": false,
  "resizable": true,
  "borderless": false,
  "title-bar-style": "hidden",
  "keyboard-shortcuts": [
    {
      "key": "CmdOrCtrl+R",
      "action": "reload"
    },
    {
      "key": "CmdOrCtrl+Shift+I",
      "action": "toggle-dev-tools"
    }
  ]
}
```

## macOS Specific

```json
{
  "name": "MacApp",
  "url": "http://localhost:3000",
  "icon": "./assets/icon.icns",
  "title-bar-style": "hidden",
  "transparent": true,
  "dock": {
    "persistent": true,
    "type": "dock"
  }
}
```

## Windows Specific

```json
{
  "name": "WindowsApp",
  "url": "http://localhost:3000",
  "icon": "./assets/icon.ico",
  "width": 1200,
  "height": 800,
  "hide-title-bar": false,
  "borderless": false,
  "theme": "dark"
}
```

## Linux Specific

```json
{
  "name": "LinuxApp",
  "url": "http://localhost:3000",
  "icon": "./assets/icon.png",
  "width": 1200,
  "height": 800,
  "hide-title-bar": false,
  "dock": {
    "type": "taskbar"
  }
}
```

## Immersive Mode (No Title Bar)

```json
{
  "name": "ImmersiveApp",
  "url": "http://localhost:3000",
  "icon": "./assets/icon.png",
  "width": 1920,
  "height": 1080,
  "hide-title-bar": true,
  "resizable": true,
  "always-on-top": false
}
```

## Kiosk Mode

```json
{
  "name": "KioskApp",
  "url": "http://localhost:3000",
  "icon": "./assets/icon.png",
  "fullscreen": true,
  "hide-title-bar": true,
  "always-on-top": true,
  "resizable": false
}
```

## With Custom Protocols

```json
{
  "name": "WebApp",
  "url": "http://localhost:3000",
  "protocols": ["myapp://"],
  "icon": "./assets/icon.png"
}
```

## Multi-Window Support

```json
{
  "name": "MultiWindowApp",
  "url": "http://localhost:3000",
  "icon": "./assets/icon.png",
  "multiple-windows": true,
  "windows": [
    {
      "label": "main",
      "title": "Main Window",
      "width": 1200,
      "height": 800
    },
    {
      "label": "settings",
      "title": "Settings",
      "width": 600,
      "height": 400
    }
  ]
}
```
