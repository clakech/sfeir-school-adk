# SFEIR School ADK

<p align="center">
 <img style="display:block" width="20%" height="20%" src="./docs/assets/images/sfeir-school-logo.png" alt="SFEIR School logo">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/MCP-Enabled-blue?style=flat-square&logo=data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTEyIDJMMyA3VjE3TDEyIDIyTDIxIDE3VjdMMTIgMloiIHN0cm9rZT0id2hpdGUiIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIi8+Cjwvc3ZnPg==" alt="MCP Enabled">
  <img src="https://img.shields.io/badge/chrome--dev--tools-0.10.1-green?style=flat-square" alt="Chrome DevTools MCP">
  <img src="https://img.shields.io/badge/AI-OpenCode%20%7C%20Gemini%20%7C%20Copilot-orange?style=flat-square" alt="AI Assistants">
</p>

<br/>

[Discover the SFEIR Schools](https://www.sfeir.com/fr/le-contenus-dexperts-de-la-technologie-et-de-linnovation/formation-gratuite-avec-nos-experts/)

# Slides

You can view the slides [here](https://sfeir-open-source.github.io/sfeir-school-adk/).

## Develop

To run docs locally, go in directory `docs` and run `npx serve` of if you don't have node, you can use docker `docker-compose up`, and open slides on http://localhost:4242/.

## Workshop

Workshops are in directory `steps` :

- two directories per workshop :
  - one with a README.md with workshop steps and source file to complete
  - a second directory suffixed with `-solution` which contains source file with solutions.

## AI Assistant Configuration

This project includes Model Context Protocol (MCP) configurations for enhanced AI coding assistance:

- **OpenCode** - `opencode.json` (auto-detected)
- **Gemini CLI** - `.gemini-mcp.json`
- **GitHub Copilot** - `.copilot-mcp.json`

All configurations include the `chrome-dev-tools` MCP server for automated slide verification and testing.

See [MCP-CONFIG.md](./MCP-CONFIG.md) for detailed setup instructions and [AGENT.md](./AGENT.md) for AI agent guidelines.

## Contributing

### Contributing Guidelines

Read through our [contributing guidelines][contributing] to learn about our submission process, coding rules and more.

### Want to Help?

Want to file a bug, contribute some code, or improve documentation? Excellent! Read up on our guidelines for [contributing][contributing] and then check out one of our issues labeled as <kbd>help wanted</kbd> or <kbd>good first issue</kbd>.

### Code of Conduct

Help us keep Angular open and inclusive. Please read and follow our [Code of Conduct][codeofconduct].

[contributing]: CONTRIBUTING.md
[codeofconduct]: https://github.com/sfeir-open-source/code-of-conduct/blob/master/CODE_OF_CONDUCT.md
