<!-- .slide: class="transition" -->

# What is a Multi-Agent System?

##==##

<!-- .slide -->

# Multi-Agent Systems: Definition

## An Autonomous Collaboration System

<br>

A **multi-agent system** is a collection of individual and autonomous agents that collaborate to achieve a common goal.

<br>

### Three Fundamental Principles:

- **Decentralized Control** : No "boss" agent controls everything
- **Local Views** : Each agent only has a partial view of the system
- **Emergent Behavior** : Complex behaviors emerge from simple interactions

Notes:
Analogy: A flock of birds - no leader, but coordinated patterns

##==##

<!-- .slide -->

# Why Multi-Agent Systems?

## Advantages of the Collaborative Approach

<br>

- 🎯 **Robustness** : If one agent fails, others continue
- 📈 **Scalability** : Add specialized agents as needed
- 🔄 **Flexibility** : Adapt architecture to complex problems
- 🧩 **Specialization** : Each agent excels in its domain

<br>

Agents working together can solve tasks that no single agent could easily accomplish.

<!-- .element: class="admonition note" -->

Notes:
Example: Customer support system with specialized agents (billing, technical, returns)

##==##

<!-- .slide -->

# ADK Agent Types

## ADK Provides Three Main Agent Types

<br>

| Type | Role | Usage |
|------|------|-------------|
| **LLM Agents** | The "brain" 🧠 | Reasoning with LLM |
| **Workflow Agents** | The "manager" 📋 | Execution flow orchestration |
| **Custom Agents** | The "specialist" 🔧 | Complex custom logic |

<br>

Notes:
- LLM Agents : Use language models to understand and reason
- Workflow Agents : Sequential, Parallel, Loop - don't do the work but direct
- Custom Agents : When you need total control over logic

##==##

<!-- .slide -->

# Agent Hierarchy

## Structured Organization of Agents

<br>

### Two Simple Rules:

1. **Parent & Sub-agents** : A parent agent can manage one or more sub-agents
2. **Single Parent Rule** : Each agent can only have one parent

<br>

```
    RootAgent (CEO)
    ├── Agent A (VP)
    │   ├── Agent A1 (Director)
    │   └── Agent A2 (Director)
    └── Agent B (VP)
        └── Agent B1 (Manager)
```

Notes:
Analogy: Company org chart - clear chain of command and data flow

##==##

<!-- .slide -->

# Communication Between Agents

## Three Main Mechanisms

<br>

### 1. **Shared Session State** 📝
Common state accessible by all agents in the hierarchy

### 2. **LLM-Driven Delegation** 🤖
Parent agent intelligently decides which sub-agent to call

### 3. **Explicit Invocation (AgentTool)** 🔧
One agent calls another agent as a tool/function

<br>

Notes:
- Shared state : Like a common whiteboard
- LLM delegation : Intelligent routing based on context
- AgentTool : On-demand expert consultation
