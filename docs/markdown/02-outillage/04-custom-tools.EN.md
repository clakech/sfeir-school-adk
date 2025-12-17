<!-- .slide: class="transition" -->

# Create Your Own Tools

##==##

<!-- .slide -->

# 3 Ways to Create Custom Tools

<br>

<div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px;">
  <div style="border: 3px solid #4285f4; border-radius: 10px; padding: 20px; background: rgba(66, 133, 244, 0.1);">
    <div style="font-size: 2em; margin-bottom: 10px;">🔧</div>
    <strong>Function Tools</strong>
    <div style="font-size: 0.85em; margin-top: 10px;">
      Python code directly in your agent
      <br><br>
      ⚡ Simple
      <br>⚙️ Flexible
    </div>
  </div>
  <div style="border: 3px solid #34a853; border-radius: 10px; padding: 20px; background: rgba(52, 168, 83, 0.1);">
    <div style="font-size: 2em; margin-bottom: 10px;">📋</div>
    <strong>OpenAPI Tools</strong>
    <div style="font-size: 0.85em; margin-top: 10px;">
      Generation from an OpenAPI spec
      <br><br>
      📄 Standard
      <br>🔄 Auto-generated
    </div>
  </div>
  <div style="border: 3px solid #fbbc04; border-radius: 10px; padding: 20px; background: rgba(251, 188, 4, 0.1);">
    <div style="font-size: 2em; margin-bottom: 10px;">🔌</div>
    <strong>MCP Tools</strong>
    <div style="font-size: 0.85em; margin-top: 10px;">
      Reusable MCP servers
      <br><br>
      🌐 Standard protocol
      <br>♻️ Reusable
    </div>
  </div>
</div>

<br>

### Each approach has its advantages depending on context

Notes:
- Function Tools = simplest to start
- OpenAPI = if you already have an API spec
- MCP = to share between agents and applications
- Can combine all 3 approaches in the same agent

##==##

<!-- .slide: class="with-code max-height"-->

# Function Tools: The Simplest
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
- Function Tools = wrapper around Python functions
- Docstring and type hints are important
- Parameter schema guides the LLM
- Implementation can be anything: API, DB, calculation...

##==##

<!-- .slide: class="with-code" -->

# Function Tools: Best Practices

### ✅ Complete description
```python
# ✅ GOOD: Clear and exhaustive description
def search_products(query: str, category: str = None, max_results: int = 10
) -> list[dict]:
    """Search products in the catalog.
    
    Args:
        query: Search keywords (e.g. "15 inch laptop")
        category: Filter by category (e.g. "electronics", "books")
        max_results: Maximum number of results to return (1-100)
        
    Returns:
        List of products with name, price, description, stock
    """
    pass
```
### ❌ Vague description
```python

def search(q: str) -> list:
    """Searches for stuff."""
    pass
```

Notes:
- Describe each parameter precisely
- Give value examples
- Document return format
- Specify constraints (ranges, enums...)
- Description quality = usage quality

##==##

<!-- .slide: class="with-code" -->

# Function Tools: Error Handling

⚠️ Always return a structure even in case of error

```python
def get_user_info(user_id: str) -> dict:
    """Retrieves user information.
    Args: user_id: Unique user ID
    Returns: Dictionary with name, email, role
    Raises:
        ValueError: If user_id is invalid
        PermissionError: If access is denied
    """
    try:
        if not user_id or not user_id.isdigit():
            return {
                "error": "Invalid user ID",
                "details": "ID must be a number"
            }
        
        return {"name": "John", "email": "john@example.com"}
        
    except Exception as e:
        return {"error": "Error during retrieval", "details": str(e)}
```

Notes:
- Don't raise exceptions directly
- Return JSON objects with "error" field
- LLM can understand and handle the error
- Provide explicit error messages
- Log errors for debugging

##==##

<!-- .slide: class="with-code" -->

# OpenAPI Tools: From a Spec

```python
from google.adk.tools.openapi_tool.openapi_spec_parser.openapi_toolset import OpenAPIToolset

# Example with a JSON string
openapi_spec_json = '...' # JSON string of the spec (retrieved from a file/url)
string_toolset = OpenAPIToolset(spec_str=openapi_spec_json, spec_str_type="json")

# Example with a dictionary
openapi_spec_dict = {...} 
dict_toolset = OpenAPIToolset(spec_dict=openapi_spec_dict)
```

**Advantages:**
- ✅ Automatic tool generation
- ✅ Synchronization with API (versioning)
- ✅ Automatic parameter validation
- ✅ Documentation included

Notes:
- OpenAPI = API documentation standard
- ADK parses the spec and generates tools
- Each endpoint becomes a potential tool
- Automatic authentication handling
- Ideal if your API is already documented in OpenAPI


##==##

<!-- .slide -->

# MCP (Model Context Protocol)

Open standard for connecting tools to LLMs

```text
┌─────────────┐
│   Client    │  (Your ADK agent)
│   (Host)    │
└──────┬──────┘
       │ MCP Protocol (JSON-RPC)
       │
┌──────┴──────┐
│ MCP Server  │  (Provides tools)
│             │
├─────────────┤
│  Tools:     │
│  - search   │
│  - read     │
│  - write    │
└─────────────┘
```

MCP = Standard created by Anthropic, now managed by the Linux foundation

<!-- .element: class="admonition note" -->

Notes:
- MCP = standard protocol for exposing tools
- Client-server architecture
- MCP server exposes tools via JSON-RPC
- Client (agent) calls these tools via the protocol
- Advantage: reusability between different agents/frameworks
- Growing ecosystem of MCP servers

##==##

<!-- .slide: class="with-code" -->

# MCP Tools in ADK

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

MCP allows reuse of existing servers whether in stdio or HTTP

Notes:
- Multiple connection modes: HTTP, WebSocket, stdio
- Dynamic discovery of exposed tools
- No need to redefine tools on client side
- MCP servers reusable between projects
- Growing community: filesystem, git, databases...

##==##

<!-- .slide -->

# MCP: Ecosystem

**Popular MCP servers available**

| Server | Description | Maintainer |
|---------|-------------|------------|
| `@modelcontextprotocol/server-filesystem` | Filesystem access | Anthropic |
| `@modelcontextprotocol/server-git` | Git operations | Anthropic |
| `mcp-server-fetch` | HTTP requests | Community |
| GenAI Toolbox | Databases | Google |

Different registries also exist, example with github: https://github.com/mcp

Notes:
- Anthropic maintains several official servers
- Active community creating new servers
- Simple installation via npm/pip
- Reusable in all frameworks supporting MCP
- ADK, Claude Desktop, etc.

##==##

<!-- .slide -->

# Comparison of the 3 Approaches

| Criterion | Function Tools | OpenAPI Tools | MCP Tools |
|---------|---------------|---------------|-----------|
| **Simplicity** | ⭐⭐⭐ | ⭐⭐ | ⭐⭐ |
| **Flexibility** | ⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ |
| **Reusability** | ⭐ | ⭐⭐ | ⭐⭐⭐ |
| **Documentation** | Manual | Auto | Auto |
| **Validation** | Manual | Auto | Auto |
| **Maintenance** | Code | Spec | Server |

Recommendations:
- 🔧 **Function Tools** : Prototypes, simple logic
- 📋 **OpenAPI** : Existing and documented REST API
- 🔌 **MCP** : Reuse, sharing between agents

Notes:
- Start with Function Tools to learn
- OpenAPI if your API is already documented
- MCP for multi-agent architecture or reuse
- Can mix all 3 in the same agent
- MCP is the future for interoperability
