# Framework-Specific Build Commands

## React (Create React App / Vite)

```bash
# Build
npm run build
# Output: build/ folder

# Serve
npx serve build -l 3000
```

## Vue 3 (Vite)

```bash
# Build
npm run build
# Output: dist/ folder

# Serve
npx serve dist -l 3000
```

## Vue 2 (Vue CLI)

```bash
# Build
npm run build
# Output: dist/ folder

# Serve
npx serve dist -l 3000
```

## Next.js (Static Export)

First, configure `next.config.js`:
```javascript
/** @type {import('next').NextConfig} */
const nextConfig = {
  output: 'export',
  images: { unoptimized: true }
}

module.exports = nextConfig
```

Then:
```bash
# Build
npm run build
# Output: out/ folder

# Serve
npx serve out -l 3000
```

## Next.js (SSR Mode)

For Next.js with SSR, use the development server:
```bash
# Start dev server
npm run dev
# Runs on http://localhost:3000

# Then package with Pake
pake http://localhost:3000 --name "MyNextApp"
```

## Vite (Vanilla JS)

```bash
# Build
npm run build
# Output: dist/ folder

# Serve
npx serve dist -l 3000
```

## Svelte/SvelteKit

```bash
# Static adapter
npm run build
# Output: build/ folder (adapter-static)

# Serve
npx serve build -l 3000
```

## Angular

```bash
# Build
npm run build
# Output: dist/project-name/ folder

# Serve
npx serve dist/project-name/browser -l 3000
```

## Troubleshooting Frameworks

### CSS Assets Missing

Ensure assets are properly referenced. For Vite/React:
```bash
# Check build output exists
ls dist/
# Should contain index.html and assets/ folder
```

### 404 on Static Files

Some frameworks need base path configuration:
```bash
# Vite - ensure public assets are in place
ls public/

# Build with correct base path
vite build --base / ./index.html
```

### SPA Routing Issues

For SPAs using history API routing:
```bash
# Use serve with SPA fallback
npx serve dist -l 3000 --spa
```

This serves `index.html` for all 404 routes, enabling client-side routing to work.
