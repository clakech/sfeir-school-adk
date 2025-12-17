<!-- .slide: class="transition" -->

# Best Practices & Advanced Patterns

##==##

<!-- .slide: class="with-code" -->

# Principle of Least Privilege

```python
# ❌ BAD: Give everything to the agent
agent = client.agents.create(
    model='gemini-2.0-flash',
    tools=[
        all_database_tools,
        all_admin_tools,
        all_user_management_tools
    ]
)

# ✅ GOOD: Context-specific tools
agent = client.agents.create(
    model='gemini-2.0-flash',
    tools=[
        read_orders_tool,      # Read only
        search_products_tool    # Search
    ]
    # NO write or admin tools
)
```

Many tools = More risks and more difficulty choosing the right tool

<!-- .element: class="admonition warning" -->

Notes:
- Agent may choose wrong tool
- Risk of unintended side-effects
- Harder to debug
- Degraded performance (too many choices)
- Fundamental security principle

##==##

<!-- .slide: class="with-code max-height" -->

# Read/Write Separation
```python
# Read-only tools
read_tools = [
    get_user_info_tool,
    list_products_tool
]
# Tools with side effects
write_tools = [
    create_order_tool,
    delete_product_tool
]
# Read-only agent by default
assistant_agent = client.agents.create(
    instructions="Client assistant - consultation only",
    tools=read_tools
)
# Admin agent with all privileges
admin_agent = client.agents.create(
    instructions="Admin agent - complete management",
    tools=read_tools + write_tools,
    # + confirmation mechanisms for critical actions
)
```

Notes:
- Clearly separate read vs write
- Most agents only need read
- Write tools = higher risk
- Implement confirmations for critical actions
- Enhanced audit and logging on write operations

##==##

<!-- .slide: class="with-code max-height" -->

# Validation and Sanitization

```python
def update_user_email(user_id: str, new_email: str) -> dict:
    """Updates a user's email."""
    
    # 1. Input validation
    if not user_id or not user_id.isdigit():
        return {"error": "invalid user_id"}
    
    # 2. Email format validation
    import re
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_pattern, new_email):
        return {"error": "Invalid email format"}
    
    # 3. Sanitization (injection protection)
    user_id = int(user_id)  # Secure conversion
    new_email = new_email.strip().lower()
    
    # 4. Permission check
    if not has_permission(user_id, "update_email"):
        return {"error": "Permission denied"}

    except Exception as e:
        log_error(e)
        return {"error": "Error during update"}
```

Notes:
- Always validate agent inputs
- Never trust blindly
- Protection against SQL/XSS injection
- Check permissions
- Log errors for audit
- Return explicit but not too verbose errors

##==##

<!-- .slide: class="with-code max-height" -->

# Observability: Logging and Tracing

```python
def get_user_info(user_id: str) -> dict:
    """Retrieves user info with complete logging."""
    start_time = datetime.now()
    logger.info(f"Tool call: get_user_info", extra={"tool_name": "get_user_info",
        "user_id": user_id, "timestamp": start_time.isoformat()
    })
    
    try:
        result = database.query(f"SELECT * FROM users WHERE id = {user_id}")
        duration = (datetime.now() - start_time).total_seconds()
        logger.info(f"Tool success: get_user_info", extra={"tool_name": "get_user_info",
            "user_id": user_id, "duration_ms": duration * 1000, "result_size": len(result)
        })
        return result
        
    except Exception as e:
        duration = (datetime.now() - start_time).total_seconds()
        logger.error(f"Tool error: get_user_info", extra={"tool_name": "get_user_info",
            "user_id": user_id, "error": str(e),
            "duration_ms": duration * 1000
        })
        return {"error": "Internal error"}
```

Notes:
- Log all tool calls
- Include: timestamp, parameters, duration, result/error
- Use structured logging (JSON)
- Integrate with Cloud Logging, Datadog, etc.
- Essential for debugging and monitoring
- Analyze tool usage patterns

##==##

<!-- .slide: class="with-code max-height" -->

# Pattern: Tool Chaining

```python
# Agent can chain automatically
agent_instructions = """
You are a research assistant. When searching for information:

1. First, use search_web to find sources
2. Then, use extract_content to retrieve content
3. Next, use analyze_content to analyze
4. Finally, use generate_summary to synthesize

Chain these tools in this order to provide a complete answer.
"""
# The tools
tools = [
    search_web_tool,       # 1. Search
    extract_content_tool,  # 2. Extraction
    analyze_content_tool,  # 3. Analysis
    generate_summary_tool  # 4. Synthesis
]
agent = client.agents.create(
    model='gemini-2.0-flash',
    instructions=agent_instructions,
    tools=tools
)
```

Notes:
- LLM can learn to chain tools
- Guide via system instructions
- Pipeline pattern: output of one tool → input of next
- Agent can adjust workflow based on context
- Alternative: create explicit orchestrator

##==##

<!-- .slide: class="with-code" -->

# Pattern: Conditional Tool Selection

```python
agent_instructions = """
You have several search tools. Choose based on context:

- search_internal_docs : For questions about our internal products/processes
- search_web : For public information and news
- query_database : For numerical data on our clients/products
- ask_expert : For complex questions requiring human expertise

Selection rules:
1. Always start with search_internal_docs if related to company
2. Use query_database for metrics, stats, KPIs
3. search_web only for external info not available internally
4. ask_expert as last resort if strong uncertainty

Explain which tool you use and why.
"""
```

<br>

### LLM learns to choose the optimal tool

Notes:
- Guide selection via clear instructions
- Preference hierarchy
- Explain selection criteria
- LLM can learn patterns
- Reduce costs by prioritizing cheaper tools
- Improve quality by choosing best source

##==##

<!-- .slide -->

# Summary: ADK Tooling

**What we've seen:**

1. ✅ **Concepts** : Why tools are essential
2. ✅ **Gemini Tools** : Google Search, Code Execution
3. ✅ **Google Cloud** : BigQuery, Spanner, Vertex AI, GKE...
4. ✅ **Third-party** : GitHub, Notion, Tavily, Exa...
5. ✅ **Custom Tools** : Function, OpenAPI, MCP
6. ✅ **Best Practices** : Security, observability

You are now ready to create powerful agents! 🚀

Notes:
- Complete coverage of tooling ecosystem
- From simplest to most advanced
- Concepts applicable beyond ADK
- Practice will come with labs
- Don't hesitate to experiment
