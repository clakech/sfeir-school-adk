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

## Slide Verification Workflow

**MANDATORY:** After modifying any slide content (Markdown files in `docs/markdown/` or presentation structure in `docs/scripts/slides.js`), you MUST verify the slides using chrome-dev-tools by following these steps:

1. **Start the dev server** (if not already running): `npm start` from the `docs/` directory
2. **Open the presentation** in Chrome: Navigate to `http://localhost:5001` (or the appropriate port)
3. **Navigate to modified slides**: Use chrome-dev-tools to navigate to the specific slides that were modified
4. **Take snapshots**: Use `chrome-dev-tools_take_snapshot` to capture the current state of modified slides
5. **Visual verification**: Use `chrome-dev-tools_take_screenshot` if visual inspection is needed
6. **Check for errors**: Use `chrome-dev-tools_list_console_messages` to verify there are no JavaScript errors
7. **Verify rendering**: Ensure that:
   - All content is properly displayed
   - Images load correctly
   - Code blocks are properly formatted
   - Transitions work as expected
   - No layout issues are present

This verification step is critical to ensure slide modifications render correctly before considering the task complete.

