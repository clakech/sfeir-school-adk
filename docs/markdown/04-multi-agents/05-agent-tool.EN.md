<!-- .slide: class="transition" -->

# Agent-as-a-Tool

##==##

<!-- .slide -->

# Agent-as-a-Tool: Concept

## Call an Agent as a Tool

<br>

This feature allows using other agents' capabilities by **calling them as tools**. Agent-as-a-Tool allows invoking another agent to perform a specific task.

<br>

### Principle:
Agent A calls Agent B as a tool, retrieves its response, and **continues managing the conversation**.

Notes:
Conceptually similar to creating a Python function that calls another agent

##==##

<!-- .slide -->

# Sub-Agent vs Agent-as-a-Tool

## Key Differences

<br>

| Aspect | Sub-Agent | Agent-as-a-Tool |
|--------|-----------|-----------------|
| **Control** | Transfer to sub-agent | Parent keeps control |
| **Response** | Sub-agent responds | Parent processes result |
| **Interactions** | Sub-agent manages | Parent continues |
| **Relationship** | Permanent hierarchy | On-demand consultation |

<br>

### Analogy:
- **Sub-Agent** = Employee in your team
- **Agent-as-a-Tool** = External consultant you call if needed

Notes:
Agent-as-a-tool is invoked dynamically by the LLM if necessary

##==##

<!-- .slide: class="with-code max-height" -->

# Agent-as-a-Tool: Implementation

## Python Code

```python
from google.adk.agents import LlmAgent
from google.adk.tools import AgentTool

# Create a specialized agent
calculator_agent = LlmAgent(
    name="Calculator",
    model="gemini-2.0-flash",
    system_instruction="Performs precise mathematical calculations"
)

# Wrap as tool
calc_tool = AgentTool(agent=calculator_agent)

# Main agent with agent-tool
main_agent = LlmAgent(
    name="Assistant",
    model="gemini-2.0-flash",
    system_instruction="General assistant that can use a calculator",
    tools=[calc_tool]  # Agent as tool
)
```

Notes:
The assistant's LLM decides when to invoke calc_tool

##==##

<!-- .slide: class="with-code" -->

# Customization Options

## AgentTool Configuration

<br>

### `skip_summarization`

```python
tool = AgentTool(
    agent=specialist_agent,
    skip_summarization=True  # Disables LLM summarization
)
```

- **True** : Bypass summarization, use agent's response directly
- **False** (default) : LLM summarizes the agent-tool's response

<br>

### Other options:
- Custom tool name and description
- Configuration metadata

Notes:
skip_summarization is useful when agent-tool response is already well formatted

##==##

<!-- .slide -->

# When to Use Agent-as-a-Tool?

## Typical Use Cases

<br>

### 🎯 Dynamic Delegation Based on Input
Main agent intelligently decides which specialist to consult

### 🔧 Occasional Specialized Capabilities
Functionality needed occasionally, not permanently

### 💬 Maintaining Conversational Context
Parent agent keeps control of conversation

<br>

### Examples:
- **General assistant** with tools: legal, medical, technical
- **Customer support agent** with specialists: billing, technical, returns
- **Research agent** with thematic experts

Notes:
LLM chooses when and which tool to call based on context

##==##

<!-- .slide: class="with-code max-height" -->

# Practical Example: Customer Support

## Agent with Multiple Specialists

```python
# Define specialized agents
billing_agent = LlmAgent(
    name="BillingSpecialist",
    system_instruction="Expert in billing and payments"
)

technical_agent = LlmAgent(
    name="TechnicalSpecialist",
    system_instruction="Expert in technical support"
)

returns_agent = LlmAgent(
    name="ReturnsSpecialist",
    system_instruction="Expert in returns and refunds"
)

# Main agent with specialists as tools
support_agent = LlmAgent(
    name="CustomerSupport",
    system_instruction="Support agent that routes to specialists",
    tools=[
        AgentTool(agent=billing_agent),
        AgentTool(agent=technical_agent),
        AgentTool(agent=returns_agent)
    ]
)
```

Notes:
support_agent automatically decides which specialist to consult
