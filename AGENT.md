# Agent Instructions

This file provides guidelines for AI agents interacting with this codebase.

## Commands

All commands should be run from the `docs/` directory.

- **Install dependencies:** `npm install`
- **Run checks:** `npm run test`
- **Start dev server:** `npm start`
- **Compile SASS:** `npm run sass`

There is no specific command for running a single test.

## Code Style

- **Formatting:** This project uses Prettier for code formatting. Adhere to the rules in `.prettierrc`.
- **JavaScript:**
    - Use ES Modules for imports/exports.
    - Follow existing naming conventions (e.g., camelCase for functions).
- **Slides:**
    - Slides are written in Markdown files under `docs/markdown/`.
    - The presentation structure is defined in `docs/scripts/slides.js`.
    - New slide sections should be added as new functions and included in the `formation` export in `docs/scripts/slides.js`.
