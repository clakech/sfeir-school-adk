<!-- .slide: class="transition" -->

# State

## Dynamic Contextualization

##==##

<!-- .slide -->

# State: Overview

## The Session Notebook

<br>

**State** is a key-value dictionary attached to each session.
It stores **metadata** that are not messages.

<br>

```python
session.state = {
    "user_name": "Alice",
    "current_step": "payment",
    "cart_total": 125.50
}
```

<br>

### Characteristics:
- 📝 Structured data (not free text)
- 🔄 Accessible and modifiable by agent and code
- 💉 Automatically injected into prompts

Notes:
Think of State as application variables

##==##

<!-- .slide -->

# When to Use State?

## Typical Use Cases

<br>

### 🎯 Multi-step Workflows
```
Tracking: current_step = "payment"
```

### 👤 User Preferences
```
Language, theme, expertise level
```

### 🛒 Transactional Data
```
Shopping cart, active filters
```

<br>

Use State for any **structured** data that influences agent behavior

<!-- .element: class="admonition important" -->

Notes:
If it's a boolean, number or structured object → State
If it's free conversation text → Event/Message

##==##

<!-- .slide: class="with-code" -->

# Scopes: Prefixes

## Control Data Scope

<br>

ADK uses **prefixes** to define scope and persistence.

| Prefix | Scope | Persistence | Example |
|---------|-------|-------------|---------|
| `None` | Session | Yes (if DB) | `current_step` |
| `user:` | User (Cross-session) | Yes | `user:theme` |
| `app:` | App (Global) | Yes | `app:api_key` |
| `temp:` | Invocation | No | `temp:debug` |

<br>

```python
# User preference (persistent across sessions)
session.state["user:preferred_language"] = "en"

# Temporary data (lost after invocation)
session.state["temp:raw_api_response"] = {...}
```

Notes:
user: is very powerful: even if user starts a new conversation, preferences are preserved

##==##

<!-- .slide: class="with-code max-height" -->

# Injection into Prompts

## Dynamic Templating with {key}

```python
from google.adk.agents import LlmAgent

# Define agent with placeholders
agent = LlmAgent(
    name="PersonalAssistant",
    model="gemini-2.0-flash",
    instruction="""
You are a personal assistant.
The user's name is: {user:name}.
Their expertise level is: {user:expertise}.
Preferred language is: {user:language}.
"""
)

# At runtime, these values are automatically injected
session.state["user:name"] = "Alice"
session.state["user:expertise"] = "Beginner"
session.state["user:language"] = "English"

# Agent receives complete instruction with values
```

<div style="font-size: 0.8em;">
This is the recommended method to personalize the agent without rewriting its prompt.
<!-- .element: class="admonition tip" -->
</div>

Notes:
ADK automatically replaces {user:name} with "Alice" before calling the LLM

##==##

<!-- .slide: class="with-code" -->

# State Modification: Pitfalls

## ❌ Absolutely Avoid


<div style="font-size: 1.3em;">

```python
# BAD PRACTICE
session = await service.get_session("abc")
session.state["key"] = "value"  # ❌ No event, no save
```

</div>

<br>

### Why it's dangerous:
- No `Event` created → No traceability
- No automatic save → Data lost
- `last_update_time` not updated

##==##

<!-- .slide: class="with-code" -->

# State Modification: Best Practice

## ✅ The Right Method


<div style="font-size: 1.2em;">

```python
from google.adk.tools import Tool

# In a Tool
class UpdatePreferenceTool(Tool):
    def run(self, ctx: ToolContext, language: str):
        # ✅ Modification via context
        ctx.session.state["user:language"] = language
        return f"Language updated: {language}"

# In a Callback
async def my_callback(ctx: CallbackContext):
    # ✅ Modification via context
    ctx.session.state["processed"] = True
```

</div>

<br>

<div style="font-size: 0.8em;">

Context (`ToolContext`, `CallbackContext`) automatically handles event creation and persistence

</div>

<!-- .element: class="admonition tip" -->

Notes:
Always go through a context to modify State

##==##

<!-- .slide: class="with-code max-height" -->

# Practical Example: Multi-step Wizard

## Managing a Sequential Process

<div style="font-size: 1.2em;">

```python
# Initialize wizard
session.state["wizard_step"] = 1
session.state["user_data"] = {}

# Step 1: Name
if session.state["wizard_step"] == 1:
    session.state["user_data"]["name"] = user_input
    session.state["wizard_step"] = 2

# Step 2: Email
elif session.state["wizard_step"] == 2:
    session.state["user_data"]["email"] = user_input
    session.state["wizard_step"] = 3

# Step 3: Finalization
elif session.state["wizard_step"] == 3:
    # All data collected
    complete_data = session.state["user_data"]
    # Final processing...
```

</div>

Notes:
State allows tracking progress without polluting message history
