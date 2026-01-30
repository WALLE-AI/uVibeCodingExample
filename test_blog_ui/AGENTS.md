<!-- OPENSPEC:START -->
# OpenSpec Instructions

These instructions are for AI assistants working in this project.

Always open `@/openspec/AGENTS.md` when the request:
- Mentions planning or proposals (words like proposal, spec, change, plan)
- Introduces new capabilities, breaking changes, architecture shifts, or big performance/security work
- Sounds ambiguous and you need the authoritative spec before coding

Use `@/openspec/AGENTS.md` to learn:
- How to create and apply change proposals
- Spec format and conventions
- Project structure and guidelines

Keep this managed block so 'openspec update' can refresh the instructions.

<!-- OPENSPEC:END -->

# AGENTS.md - Development Guidelines for AI Agents

This document provides guidelines for AI agents working on this codebase.

## Build, Lint, and Test Commands

### Core Commands
```bash
# Install dependencies
npm install

# Start development server
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview
```

### Linting and Formatting
```bash
# Run ESLint
npm run lint

# Fix ESLint errors automatically
npm run lint:fix

# Run Prettier check
npm run format:check

# Auto-format with Prettier
npm run format

# Type checking (if using TypeScript)
npm run typecheck
```

### Testing
```bash
# Run all tests
npm test

# Run tests in watch mode
npm run test:watch

# Run a single test file
npm test -- filename.test.ts

# Run a single test by name
npm test -- --testNamePattern="test name"

# Run tests with coverage
npm run test:coverage

# Run E2E tests
npm run test:e2e
```

### CI/CD
```bash
# Run full CI pipeline
npm run ci
```

## Code Style Guidelines

### General Principles
- Write clean, readable, and maintainable code
- Keep functions small and focused on a single responsibility
- Use descriptive names for variables, functions, and components
- Avoid code duplication; extract reusable logic

### TypeScript Guidelines
- Enable strict mode in `tsconfig.json`
- Prefer explicit types over `any`
- Use interfaces for object shapes, types for unions/primitives
- Avoid type assertions; use type guards when needed
- Export only what's necessary; prefer named exports
- Use generics for reusable components and utilities

### React/Component Guidelines
- Use functional components with hooks
- Name components with PascalCase
- Use `.tsx` extension for components, `.ts` for utilities
- Keep components under 200 lines; extract sub-components
- Use composition over inheritance
- Memoize expensive computations with `useMemo` and callbacks with `useCallback`
- Avoid `useEffect` when possible; prefer event handlers and derived state
- Place custom hooks in `hooks/` directory with `use` prefix

### Naming Conventions
- **Variables/functions**: camelCase (`getUserData`, `isLoading`)
- **Constants**: SCREAMING_SNAKE_CASE (`MAX_RETRIES`)
- **Classes/Components**: PascalCase (`UserProfile`)
- **Files**: kebab-case for non-components, PascalCase for components
- **Hooks**: `use` prefix (`useAuth`, `useDebounce`)
- **Booleans**: `is`/`has`/`can` prefix (`isValid`, `hasError`)

### Import Ordering
1. React imports
2. Third-party imports
3. Internal imports (relative paths)
4. CSS/style imports

Within each group, alphabetize by module name.

### Error Handling
- Use try-catch for async operations with user feedback
- Create custom error classes for domain-specific errors
- Never swallow errors silently; log appropriately
- Use error boundaries for React component trees
- Provide meaningful error messages for debugging

### File Structure
```
src/
├── components/     # Reusable UI components
├── hooks/          # Custom React hooks
├── utils/          # Helper functions
├── types/          # TypeScript type definitions
├── pages/          # Page-level components
├── services/       # API/client services
├── constants/      # Application constants
├── styles/         # Global styles
└── assets/         # Static assets
```

### Styling
- Use CSS modules or a CSS-in-JS solution
- Follow BEM naming for CSS classes if using plain CSS
- Keep styles co-located with components when possible
- Use design tokens for colors, spacing, and typography

### Git Commits
- Use conventional commits: `feat:`, `fix:`, `docs:`, `refactor:`
- Keep commits atomic and focused
- Write clear commit messages explaining the "why"

### Performance
- Lazy load routes and heavy components
- Optimize images and assets
- Avoid unnecessary re-renders in React
- Use production mode for benchmarking

## Project-Specific Configuration

### Environment Variables
```
VITE_API_URL=           # API endpoint
VITE_AUTH_ENABLED=      # Enable/disable auth
```

### Dependencies
- React, ReactDOM
- TypeScript
- ESLint + Prettier
- Vitest (testing)
- Vite (build tool)

### Browser Support
- Modern browsers (last 2 versions)
- No IE11 support required

## Cursor/Copilot Instructions

_Project-specific Cursor rules and Copilot instructions should be documented here once established._
