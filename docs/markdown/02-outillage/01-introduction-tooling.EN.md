<!-- .slide -->

# Why Tools Are Essential

### An agent without tools = A brain without hands

| ❌ **LLM alone**           | ✅ **Agent with tools**        |
|---------------------------|---------------------------------|
| Generates text           | Search the web              |
| Reasons                  | Access data                 |
| Responds                    | Execute code                 |
|                           | Call APIs                |
|                           | Act in the real world         |


Tools transform words into actions

<!-- .element: class="admonition note" -->

Notes:
- Without tools, the agent can only talk
- Tools are the interface between AI and the real world
- This is the fundamental difference between a chatbot and an agent
- Tools enable factual verification

##==##

<!-- .slide: class="with-code" -->

# What is a Tool?

A tool => code that the agent will be able to call

```python
def get_weather(city: str, unit: str):
    """
    Retrieves the weather for a city in the specified unit.

    Args:
        city (str): The city name.
        unit (str): The temperature unit, either 'Celsius' or 'Fahrenheit'.
    """
    # ... function logic ...
    return {"status": "success", "report": f"Weather for {city} is sunny."}
```

The LLM doesn't call tools directly, it asks the agent to do it

<!-- .element: class="admonition warning" -->

Notes:
- A tool has a name, a description and parameters
- The description is crucial: it guides the LLM
- The LLM uses native tool calling to call the function
- The agent receives the result and can use it in its response

##==##

<!-- .slide -->

# How Does the Agent Execute Tools?

ReAct Pattern

- Reasoning -> The LLM analyzes the user's request and detects the need for a tool
- Action -> The agent calls the tool and makes another LLM call with the result in context
- Observation -> The LLM analyzes the need for use + the tool result to generate the response

Example:

```text
1. 👤 User: "What's the weather in Paris?"
         ↓
2. 🧠 LLM: Analysis → Need to call get_weather("Paris")
         ↓
3. 🤖 Agent: Executes API call → Returns {"temp": 18, "sky": "clear"}
         ↓
4. 🧠 LLM: Receives result + initial request → Formulates response
         ↓
5. 💬 Response: "It's 18°C in Paris with clear skies"
```

Notes:
- The cycle can repeat multiple times
- The agent can call multiple tools before responding
- Each call enriches the context
- Orchestration is managed automatically by the framework

##==##

<!-- .slide -->

# How Does the Agent Choose?

The LLM analyzes 3 elements to choose the right tool:
<br>

1. **User request** : Intent and context
2. **Tool description** : Name + description + parameters
3. **Conversation history** : Previous results

<br>

```python
# ❌ Bad description
name="tool1"
description="Does things"

# ✅ Good description
name="search_company_database"
description="Search employees in the company database by name, department or email"
```

The quality of descriptions directly impacts selection quality

<!-- .element: class="admonition note" -->

Notes:
- The LLM doesn't have access to code, only metadata
- A good description = better selection
- Be specific and clear about the tool's purpose
- Include examples in the description if necessary
- Avoid ambiguity between similar tools

##==##

<!-- .slide -->

# Best Practices: Tool Naming

| ✅ **GOOD: Verb + Object + Context** | ❌ **BAD: Too vague or generic** |
|--------------------------------------|-----------------------------------------|
| get_weather_forecast                 | weather                                 |
| search_customer_orders               | search                                  |
| create_support_ticket                | data                                    |
| update_user_profile                  | function1                               |

<br>

**Golden rules:**
- Start with an action verb (`get`, `search`, `create`, `update`, `delete`)
- Be explicit about the object being manipulated
- Use snake_case
- Avoid obscure abbreviations

Notes:
- The name is the first indicator for the LLM
- A good name = less ambiguity
- Follow a consistent convention in your codebase
- The name should be self-explanatory

##==##

<!-- .slide -->

# Tools vs Prompting: When to Use What?

| Situation | Solution | Why |
|-----------|----------|----------|
| Text generation | **Prompting** | LLM excels naturally |
| Logical reasoning | **Prompting** | Native LLM capability |
| Data retrieval | **Tool** | Factual, up-to-date data |
| Complex calculations | **Tool** | Guaranteed precision |
| External API calls | **Tool** | System interaction |
| State modification | **Tool** | Secure and traceable action |


Notes:
- Don't overuse tools
- The LLM can already do a lot natively
- Tools = for interaction with the real world
- Overhead of tool calling vs direct generation
- Find the right balance

##==##

<!-- .slide -->

# The 3 Categories of ADK Tools

<br>

<div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; margin: 20px 0;">
  <div style="border: 3px solid #4285f4; border-radius: 10px; padding: 20px; background: rgba(66, 133, 244, 0.1);">
    <div style="font-size: 2em; margin-bottom: 10px;">🔷</div>
    <strong>Gemini/Google Tools</strong>
    <div style="font-size: 0.9em; margin-top: 10px;">
      Native to the model
      <br>• Google Search
      <br>• Code Execution
      <br>• Bigquery
      <br>• ...
    </div>
  </div>
  <div style="border: 3px solid #fbbc04; border-radius: 10px; padding: 20px; background: rgba(251, 188, 4, 0.1);">
    <div style="font-size: 2em; margin-bottom: 10px;">🔌</div>
    <strong>Third-party</strong>
    <div style="font-size: 0.9em; margin-top: 10px;">
      External integrations
      <br>• GitHub
      <br>• Notion
      <br>• Gitlab
      <br>• ...
    </div>
  </div>
  <div style="border: 3px solid #34a853; border-radius: 10px; padding: 20px; background: rgba(52, 168, 83, 0.1);">
    <div style="font-size: 2em; margin-bottom: 10px;">☁️</div>
    <strong>Custom</strong>
    <div style="font-size: 0.9em; margin-top: 10px;">
      Code functions
      <br>• External libraries
      <br>• Custom code
    </div>
  </div>
</div>

Notes:
- 3 main families of tools in ADK
- Gemini tools = native, no external config
- Google Cloud = requires GCP credentials
- Third-party = often requires API keys
- Custom tools = for your specific needs
