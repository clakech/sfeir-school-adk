<!-- .slide: class="transition" -->

# Outils Third-Party

##==##

<!-- .slide -->

# Écosystème Third-Party

Utilisation de serveurs MCP officiellements supportés par Google et la communauté

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
    <br>Search sémantique
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

Nécessitent généralement des API keys externes

<!-- .element: class="admonition warning" -->

Notes:
- Intégrations maintenues par Google + la communauté
- Chaque outil nécessite une inscription et API key
- Certains sont gratuits, d'autres payants
- Couvrent différents domaines : dev, docs, web, data
- Configuration simple une fois la clé obtenue

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
**Use cases :**
- 🤖 Code review automatisé
- 🐛 Triage et classification d'issues
- 📝 Génération de release notes
- 🔍 Recherche de code et documentation

Notes:
- Token GitHub avec les scopes appropriés requis
- L'agent peut interagir avec repos publics et privés
- Peut analyser le code et suggérer des améliorations
- Automatisation des tâches répétitives de dev
- Attention aux permissions : commencer en read-only
