<!-- .slide: class="transition" -->

# Callbacks & Plugins

##==##

<!-- .slide -->

# Callbacks: Concept

## Intercept Lifecycle

<br>

**Callbacks** are anchor points ("hooks") that allow you to execute custom code at specific moments of agent execution.

### 3 Types of Hooks:

1. **Agent Callbacks** 🤖 : `before_agent` / `after_agent`
   - *Session management, initialization, cleanup.*
2. **Model Callbacks** 🧠 : `before_model` / `after_model`
   - *Prompt modification, token logging, audit.*
3. **Tool Callbacks** 🛠️ : `before_tool` / `after_tool`
   - *Argument validation, API cache, response transformation.*

They allow adding logic (logging, security, metrics) without polluting agent business code.

<!-- .element: class="admonition tip" -->

##==##

<!-- .slide: class="with-code max-height" -->

# Callback Implementation

## Example: Logging and Modification

<br>

```python
def log_start(agent_name, user_input):
    print(f"🏁 Agent {agent_name} started with: {user_input}")

def inject_security_context(model_input):
    # Add security directive before each LLM call
    model_input += "\nIMPORTANT: Never reveal passwords."
    return model_input

my_agent = LlmAgent(
    name="SecureAgent",
    model="gemini-2.0-flash",
    # Attach callbacks
    before_agent_callback=log_start,
    before_model_callback=inject_security_context
)
```

The `before_model` callback is powerful because it can silently modify what the model "sees", without the user having to write it.

<!-- .element: class="admonition note" -->

Notes:
Note that callbacks can return modified values or simply perform an action (side-effect) like logging.

##==##

<!-- .slide: class="with-code" -->

# Plugins

## Package and Reuse Callbacks

A **Plugin** is a class that groups several callbacks for a complete functionality (ex: BigQuery Logging, PII Filter).

```python
from google.adk.plugins import BasePlugin

class AuditPlugin(BasePlugin):
    def __init__(self, log_file):
        self.file = log_file
    def before_agent(self, agent, input):
        # Global log for all agents
        self.log(f"Session {agent.session_id} start")
    def after_model(self, agent, response):
        # Audit token consumption
        self.log(f"Tokens used: {response.usage_metadata}")
runner = DaprRunner(
    agents=[agent1, agent2],
    plugins=[AuditPlugin("audit.log")] # Applies to ALL agents
)
```

A Callback is attached to a specific Agent. A Plugin is attached to the Runner and applies to the entire system.

<!-- .element: class="admonition important" -->
##==##

<!-- .slide -->

# Callbacks vs Plugins

## Decision Matrix

<br>

| Criterion | Callbacks | Plugins |
|---------|--------------|------------|
| **Scope** | Local (Single Agent) | Global (Entire Runner) |
| **Complexity** | Simple function | Structured class (possible state) |
| **Reusability** | Low (Copy-paste) | High (Distributable package) |
| **Use Case** | Business-specific logic | Infrastructure (Log, Security, Monitoring) |

<br>

### Golden Rule:
- **Business Logic** (ex: validate a business rule) ➔ **Callback**
- **System Logic** (ex: Prompt Sanitization) ➔ **Plugin**

Don't reinvent the wheel: ADK comes with standard plugins (BigQuery, Model Armor, etc.). Check before coding your own.

<!-- .element: class="admonition tip" -->
