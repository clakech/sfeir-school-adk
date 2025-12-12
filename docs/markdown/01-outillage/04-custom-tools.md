<!-- .slide: class="transition" -->

# Créer vos propres Tools

##==##

<!-- .slide -->

# 3 façons de créer des custom tools

<br>

<div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px;">
  <div style="border: 3px solid #4285f4; border-radius: 10px; padding: 20px; background: rgba(66, 133, 244, 0.1);">
    <div style="font-size: 2em; margin-bottom: 10px;">🔧</div>
    <strong>Function Tools</strong>
    <div style="font-size: 0.85em; margin-top: 10px;">
      Code Python directement dans votre agent
      <br><br>
      ⚡ Simple
      <br>⚙️ Flexible
    </div>
  </div>
  <div style="border: 3px solid #34a853; border-radius: 10px; padding: 20px; background: rgba(52, 168, 83, 0.1);">
    <div style="font-size: 2em; margin-bottom: 10px;">📋</div>
    <strong>OpenAPI Tools</strong>
    <div style="font-size: 0.85em; margin-top: 10px;">
      Génération depuis une spec OpenAPI
      <br><br>
      📄 Standard
      <br>🔄 Auto-généré
    </div>
  </div>
  <div style="border: 3px solid #fbbc04; border-radius: 10px; padding: 20px; background: rgba(251, 188, 4, 0.1);">
    <div style="font-size: 2em; margin-bottom: 10px;">🔌</div>
    <strong>MCP Tools</strong>
    <div style="font-size: 0.85em; margin-top: 10px;">
      Serveurs MCP réutilisables
      <br><br>
      🌐 Protocole standard
      <br>♻️ Réutilisable
    </div>
  </div>
</div>

<br>

### Chaque approche a ses avantages selon le contexte

Notes:
- Function Tools = le plus simple pour commencer
- OpenAPI = si vous avez déjà une spec API
- MCP = pour partager entre agents et applications
- On peut combiner les 3 approches dans un même agent

##==##

<!-- .slide: class="with-code max-height"-->

# Function Tools : Le plus simple
```python [1-10,15]
def get_weather(city: str, unit: str):
    """
    Retrieves the weather for a city in the specified unit.

    Args:
        city (str): The city name.
        unit (str): The temperature unit, either 'Celsius' or 'Fahrenheit'.
    """
    # ... function logic ...
    return {"status": "success", "report": f"Weather for {city} is sunny."}

weather_agent = LlmAgent(
    name="weather_agent",
    model="gemini-2.0-flash",
    tools=[get_weather],
    instruction="""You are a weather agent
    When asked for the weather you can use the get_weather tool with unit and city to answer the user
    """,
    description="Get the actual weather",
)
```

Notes:
- Function Tools = wrapper autour de fonctions Python
- La docstring et les type hints sont importants
- Le schéma de paramètres guide le LLM
- L'implémentation peut être n'importe quoi : API, DB, calcul...

##==##

<!-- .slide: class="with-code" -->

# Function Tools : Best Practices

### ✅ Description complète
```python
# ✅ BON : Description claire et exhaustive
def search_products(query: str, category: str = None, max_results: int = 10
) -> list[dict]:
    """Recherche des produits dans le catalogue.
    
    Args:
        query: Mots-clés de recherche (ex: "laptop 15 pouces")
        category: Filtrer par catégorie (ex: "electronics", "books")
        max_results: Nombre maximum de résultats à retourner (1-100)
        
    Returns:
        Liste de produits avec nom, prix, description, stock
    """
    pass
```
### ❌ Description vague
```python

def search(q: str) -> list:
    """Cherche des trucs."""
    pass
```

Notes:
- Décrire précisément chaque paramètre
- Donner des exemples de valeurs
- Documenter le format de retour
- Spécifier les contraintes (ranges, enums...)
- La qualité de la description = qualité de l'usage

##==##

<!-- .slide: class="with-code" -->

# Function Tools : Gestion d'erreurs

⚠️ Toujours retourner une structure même en cas d'erreur

```python
def get_user_info(user_id: str) -> dict:
    """Récupère les informations d'un utilisateur.
    Args: user_id: ID unique de l'utilisateur
    Returns: Dictionnaire avec nom, email, role
    Raises:
        ValueError: Si l'user_id est invalide
        PermissionError: Si l'accès est refusé
    """
    try:
        if not user_id or not user_id.isdigit():
            return {
                "error": "ID utilisateur invalide",
                "details": "L'ID doit être un nombre"
            }
        
        return {"name": "John", "email": "john@example.com"}
        
    except Exception as e:
        return {"error": "Erreur lors de la récupération", "details": str(e)}
```

Notes:
- Ne pas lever d'exceptions directement
- Retourner des objets JSON avec champ "error"
- Le LLM peut comprendre et gérer l'erreur
- Fournir des messages d'erreur explicites
- Logger les erreurs pour debugging

##==##

<!-- .slide: class="with-code" -->

# OpenAPI Tools : Depuis une spec

```python
from google.adk.tools.openapi_tool.openapi_spec_parser.openapi_toolset import OpenAPIToolset

# Exemple avec une chaine de caractère JSON
openapi_spec_json = '...' # La chaine de caractère JSON de la spec (récupérée depuis un fichier/une url)
string_toolset = OpenAPIToolset(spec_str=openapi_spec_json, spec_str_type="json")

# Exemple avec un dictionnaire
openapi_spec_dict = {...} 
dict_toolset = OpenAPIToolset(spec_dict=openapi_spec_dict)
```

**Avantages :**
- ✅ Génération automatique des tools
- ✅ Synchronisation avec l'API (versioning)
- ✅ Validation automatique des paramètres
- ✅ Documentation incluse

Notes:
- OpenAPI = standard de documentation d'API
- ADK parse la spec et génère les tools
- Chaque endpoint devient un tool potentiel
- Gestion automatique de l'authentification
- Idéal si votre API est déjà documentée en OpenAPI


##==##

<!-- .slide -->

# MCP (Model Context Protocol)

Standard ouvert pour connecter des outils aux LLMs

```text
┌─────────────┐
│   Client    │  (Votre agent ADK)
│   (Host)    │
└──────┬──────┘
       │ MCP Protocol (JSON-RPC)
       │
┌──────┴──────┐
│ MCP Server  │  (Fournit des tools)
│             │
├─────────────┤
│  Tools:     │
│  - search   │
│  - read     │
│  - write    │
└─────────────┘
```

MCP = Standard créé par Anthropic, aujourd'hui géré par la Linux foundation

<!-- .element: class="admonition note" -->

Notes:
- MCP = protocole standard pour exposer des tools
- Architecture client-server
- Le serveur MCP expose des tools via JSON-RPC
- Le client (agent) appelle ces tools via le protocole
- Avantage : réutilisabilité entre différents agents/frameworks
- Écosystème grandissant de serveurs MCP

##==##

<!-- .slide: class="with-code" -->

# MCP Tools dans ADK

```python
root_agent = LlmAgent(
    model='gemini-2.0-flash',
    name='maps_assistant_agent',
    instruction='Help the user with mapping, directions, and finding places using Google Maps tools.',
    tools=[
        McpToolset(
            connection_params=StdioConnectionParams(
                server_params = StdioServerParameters(
                    command='npx',
                    args=["-y", "@modelcontextprotocol/server-google-maps"],
                    env={
                        "GOOGLE_MAPS_API_KEY": google_maps_api_key
                    }
                ),
            ),
        )
    ],
)
```

MCP permet de réutiliser des serveurs existants que ce soit en stdio ou en HTTP

Notes:
- Plusieurs modes de connexion : HTTP, WebSocket, stdio
- Découverte dynamique des tools exposés
- Pas besoin de redéfinir les tools côté client
- Serveurs MCP réutilisables entre projets
- Communauté grandissante : filesystem, git, databases...

##==##

<!-- .slide -->

# MCP : Écosystème

**Serveurs MCP populaires disponibles**

| Serveur | Description | Maintainer |
|---------|-------------|------------|
| `@modelcontextprotocol/server-filesystem` | Accès au filesystem | Anthropic |
| `@modelcontextprotocol/server-git` | Opérations Git | Anthropic |
| `mcp-server-fetch` | HTTP requests | Community |
| GenAI Toolbox | Bases de données | Google |

Différentes registry existent également, exemple avec github: https://github.com/mcp

Notes:
- Anthropic maintient plusieurs serveurs officiels
- Communauté active qui crée de nouveaux serveurs
- Installation simple via npm/pip
- Réutilisables dans tous les frameworks supportant MCP
- ADK, Claude Desktop, etc.

##==##

<!-- .slide -->

# Comparaison des 3 approches

| Critère | Function Tools | OpenAPI Tools | MCP Tools |
|---------|---------------|---------------|-----------|
| **Simplicité** | ⭐⭐⭐ | ⭐⭐ | ⭐⭐ |
| **Flexibilité** | ⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ |
| **Réutilisabilité** | ⭐ | ⭐⭐ | ⭐⭐⭐ |
| **Documentation** | Manuelle | Auto | Auto |
| **Validation** | Manuelle | Auto | Auto |
| **Maintenance** | Code | Spec | Serveur |

Recommandations :
- 🔧 **Function Tools** : Prototypes, logique simple
- 📋 **OpenAPI** : API REST existante et documentée
- 🔌 **MCP** : Réutilisation, partage entre agents

Notes:
- Commencer par Function Tools pour apprendre
- OpenAPI si votre API est déjà documentée
- MCP pour architecture multi-agents ou réutilisation
- Possibilité de mixer les 3 dans un même agent
- MCP est le futur pour l'interopérabilité
