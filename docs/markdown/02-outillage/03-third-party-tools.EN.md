<!-- .slide: class="transition" -->

# Third-Party Tools

##==##

<!-- .slide -->

# Third-Party Ecosystem

Using MCP servers officially supported by Google and the community

<div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 15px; font-size: 0.8em;">
  <div style="border: 2px solid #6e5494; padding: 12px; border-radius: 8px;">
    <strong>GitHub</strong>
    <br>Code, Issues, PRs
  </div>
  <div style="border: 2px solid #000; padding: 12px; border-radius: 8px;">
    <strong>Notion</strong>
    <br>Docs, Tasks, DBs
  </div>
  <div style="border: 2px solid #ff6b00; padding: 12px; border-radius: 8px;">
    <strong>Hugging Face</strong>
    <br>Models, Datasets
  </div>
  <div style="border: 2px solid #5469d4; padding: 12px; border-radius: 8px;">
    <strong>Tavily</strong>
    <br>Search, Crawl
  </div>
  <div style="border: 2px solid #00d4ff; padding: 12px; border-radius: 8px;">
    <strong>Exa</strong>
    <br>Semantic search
  </div>
  <div style="border: 2px solid #ff4600; padding: 12px; border-radius: 8px;">
    <strong>Firecrawl</strong>
    <br>Web scraping
  </div>
  <div style="border: 2px solid #1e90ff; padding: 12px; border-radius: 8px;">
    <strong>Browserbase</strong>
    <br>Browser automation
  </div>
  <div style="border: 2px solid #ff6b35; padding: 12px; border-radius: 8px;">
    <strong>Bright Data</strong>
    <br>Web data
  </div>
  <div style="border: 2px solid #00b8d4; padding: 12px; border-radius: 8px;">
    <strong>AgentQL</strong>
    <br>Web extraction
  </div>
</div>

<br>

Generally require external API keys

<!-- .element: class="admonition warning" -->

Notes:
- Integrations maintained by Google + the community
- Each tool requires registration and API key
- Some are free, others paid
- Cover different domains: dev, docs, web, data
- Simple configuration once the key is obtained

##==##

<!-- .slide: class="with-code" -->
# GitHub 

```python[5-14]
root_agent = Agent(
    [...]
    tools=[
        McpToolset(
            connection_params=StreamableHTTPServerParams(
                url="https://api.githubcopilot.com/mcp/",
                headers={
                    "Authorization": f"Bearer {GITHUB_TOKEN}",
                    "X-MCP-Toolsets": "all",
                    "X-MCP-Readonly": "true"
                },
            ),
        )
    ],
)
```
**Use cases:**
- 🤖 Automated code review
- 🐛 Issue triage and classification
- 📝 Release notes generation
- 🔍 Code and documentation search

Notes:
- GitHub token with appropriate scopes required
- Agent can interact with public and private repos
- Can analyze code and suggest improvements
- Automation of repetitive dev tasks
- Pay attention to permissions: start in read-only
