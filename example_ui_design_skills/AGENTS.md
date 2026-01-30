# AGENTS.md

This repository contains opencode skill packages. Skills are reusable capabilities for AI agents.

## Project Structure

```
.opencode/
├── skills/
│   ├── skill-creator/         # Tooling for creating new skills
│   │   └── scripts/
│   │       ├── init_skill.py      # Initialize a new skill from template
│   │       ├── package_skill.py    # Package skill into .skill file
│   │       └── quick_validate.py  # Validate skill structure
│   ├── yt-dlp-downloader/     # Video downloading capability
│   │   └── scripts/
│   │       ├── download.bat       # Batch download videos
│   │       └── install.bat        # Install dependencies
│   ├── pake-web-to-desktop/  # Web-to-desktop packaging
│   │   └── scripts/
│   │       ├── package.sh         # Shell script for Unix
│   │       └── package.ps1        # PowerShell for Windows
│   ├── ui-ux-pro-max/         # UI/UX design intelligence
│   └── archivebox/             # Web archiving capability
└── package.json
```

## Commands

### Running Scripts

**Python scripts (skill-creator):**
```bash
python3 .opencode/skills/skill-creator/scripts/init_skill.py <skill-name> --path <path>
python3 .opencode/skills/skill-creator/scripts/package_skill.py <skill-path> [output-dir]
python3 .opencode/skills/skill-creator/scripts/quick_validate.py <skill-directory>
```

**Bash scripts (pake-web-to-desktop):**
```bash
./.opencode/skills/pake-web-to-desktop/scripts/package.sh [build-dir] [port] [app-name]
```

**PowerShell scripts (pake-web-to-desktop):**
```powershell
.\.opencode\skills\pake-web-to-desktop\scripts\package.ps1 [-BuildDir <string>] [-Port <int>] [-AppName <string>]
```

**Batch scripts (yt-dlp-downloader):**
```cmd
.opencode\skills\yt-dlp-downloader\scripts\install.bat
.opencode\skills\yt-dlp-downloader\scripts\download.bat "URL1" "URL2"
```

### Testing and Validation

**Validate skill structure:**
```bash
python3 .opencode/skills/skill-creator/scripts/quick_validate.py <skill-directory>
```

No automated test suite exists. Skills are manually validated through the quick_validate.py script which checks:
- SKILL.md exists with proper YAML frontmatter
- Frontmatter has required fields (name, description)
- Name follows hyphen-case convention (lowercase, hyphens only)
- No unexpected frontmatter properties
- Description length limits (max 1024 chars)

## Code Style Guidelines

### Python (skill-creator scripts)

**Imports:** Standard library only when possible. Use `pathlib.Path` for file operations.

**Formatting:** PEP 8 style guide
- 4-space indentation
- Max 100 character line length
- One blank line between functions
- Two blank lines before top-level functions

**Docstrings:** Google-style docstrings for functions with Args/Returns sections
```python
def example_function(arg1, arg2):
    """
    Brief description of function.

    Args:
        arg1: Description of argument
        arg2: Description of argument

    Returns:
        Description of return value
    """
```

**Error Handling:** Use try/except blocks with informative error messages
```python
try:
    skill_dir.mkdir(parents=True, exist_ok=False)
    print(f"✅ Created skill directory: {skill_dir}")
except Exception as e:
    print(f"❌ Error creating directory: {e}")
    return None
```

**Naming Conventions:**
- Functions: snake_case (e.g., `init_skill`, `validate_skill`)
- Variables: snake_case (e.g., `skill_name`, `output_dir`)
- Constants: UPPER_CASE (e.g., `SKILL_TEMPLATE`, `ALLOWED_PROPERTIES`)

**Functions:** Keep functions focused and single-purpose. Use helper functions for reusable logic.

**Return Values:** Return None for errors, valid values for success. Use tuples `(success, message)` for validation.

**Shebang:** Use `#!/usr/bin/env python3` for portability.

### Bash Scripts

**Shebang:** `#!/bin/bash` with `set -e` for error handling

**Output formatting:** Use ANSI color codes for status messages
```bash
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'
echo -e "${GREEN}==>${NC} $1"
echo -e "${RED}ERROR:${NC} $1"
```

**Functions:** Use snake_case names with clear, descriptive purposes. Create helper functions for:
- Prerequisite checking (`check_prerequisites`)
- Build operations (`build_project`)
- Service management (`start_server`, `kill_server`)
- Cleanup (`cleanup`)

**Variables:** Use UPPER_CASE for constants, snake_case for variables

**Error handling:** Check command existence before use, exit on critical failures

**Traps:** Always set cleanup traps for graceful shutdown
```bash
trap cleanup EXIT INT TERM
```

### PowerShell Scripts

**Shebang:** `#!/usr/bin/env pwsh`

**Parameters:** Use named parameters with defaults
```powershell
param(
    [string]$BuildDir = "dist",
    [int]$Port = 3000,
    [string]$AppName = "MyApp"
)
```

**Error handling:** Set `$ErrorActionPreference = "Stop"` at script start

**Functions:** Use Verb-Noun naming (PascalCase) with hyphenated names
```powershell
function Test-Prerequisites { }
function Invoke-Package { }
function Write-Step { param([string]$Message) }
```

**Output formatting:** Use `Write-Host` with `-ForegroundColor` for colored output

### Batch Files (Windows)

**Error checking:** Check errorlevel after each command
```cmd
pip install -U yt-dlp
if errorlevel 1 (
    echo [ERROR] Failed to install
    exit /b 1
)
```

**Output format:** Use consistent prefixes `[OK]`, `[ERROR]`, `[INFO]`, `[WARNING]`

**Echo commands:** Use `setlocal enabledelayedexpansion` for variable expansion in loops

## SKILL.md Requirements

All skills must have a `SKILL.md` file with YAML frontmatter:

```yaml
---
name: hyphen-case-name
description: Brief, informative description of when to use this skill
---
```

**Frontmatter rules:**
- `name`: Hyphen-case, max 64 chars, lowercase letters/digits/hyphens only
- `description`: Max 1024 chars, no angle brackets (`<`, `>`)
- Optional fields: `license`, `allowed-tools`, `metadata`

**Naming conventions:**
- Skill names: hyphen-case (e.g., `skill-creator`, `yt-dlp-downloader`)
- Directory names: Must match skill name exactly
- SKILL.md filename: Exactly `SKILL.md` (uppercase)

## Resource Directory Guidelines

### scripts/
Executable code that performs operations directly. May be executed without loading into context.

### references/
Documentation to be loaded into context. Use for API docs, detailed guides, complex workflows.

### assets/
Files for output (templates, images, fonts). NOT loaded into context.

## Notes

- No build/lint commands are configured in package.json
- No automated test framework is used
- All scripts are executable with shebang headers
- Dependencies are minimal: Python standard library + yaml for skill validation
- Package uses bun as runtime (see bun.lock)
