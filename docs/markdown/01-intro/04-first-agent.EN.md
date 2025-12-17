<!-- .slide: class="transition" -->

# My First Agent

##==##

<!-- .slide -->

# From Chat to Agent: Example

<br>

**❓ Question: "What's the weather in Paris and should I take an umbrella?"**

<br>

| 💬 Simple Chat | 🤖 Agent |
|---------------|---------|
| "I can't access real-time weather data..." | 1. 🔍 Search current weather |
| (Potentially hallucinates) | 2. 📊 Analyze data (rain?) |
| | 3. ✅ Respond with certainty: "18°C, no rain expected, no need for umbrella" |

<br>

### The agent can **verify** and **act** on real data

Notes:
- Fundamental difference: connection to the real world
- The agent doesn't guess, it verifies
- Reduces hallucinations about facts
- Increases reliability

##==##

<!-- .slide -->

# Common Agent Types

<br>

| Type | Description | Use Case |
|------|-------------|----------|
| **Conversational** | Natural dialogue + actions | Personal assistant, customer support |
| **Task-based** | Executes a specific task | Automation, workflows |
| **Multi-agent** | Multiple agents collaborate | Complex systems, simulation |
| **Autonomous** | Works without supervision | Monitoring, alerts |

<br>

We start simple: conversational agent with a few tools

<!-- .element class="admonition note"-->

Notes:
- Different types for different needs
- We'll start with the simplest
- Complexity comes progressively
- Multi-agent = advanced level (later in the training)

##==##

<!-- .slide -->

# When NOT to use an agent?

<br>

| ❌ Avoid agents | ✅ Prefer |
|---------------------|-------------|
| Simple and deterministic tasks | Classic script, business rules |
| Need for 100% predictable results | Traditional algorithms |
| Critical latency (< 100ms) | Direct API, cache |
| Very limited token budget | Smaller model, fine-tuning |
| Highly sensitive data | Local processing, fixed rules |

<br>

An agent adds complexity - use it when it brings value

<!-- .element class="admonition note"-->

Notes:
- Agents are not always the solution
- Latency cost: each LLM call takes time
- Token cost: reasoning = additional tokens
- Unpredictability: the LLM can vary its responses
- Security: more attack surface with tools
- Rule: if an if/else is enough, no need for an agent

##==##

<!-- .slide -->

# Agent Frameworks

<br>

**Most popular in 2025:**

| Framework | GitHub Stars | Main Strengths |
|-----------|----------------|-------------------|
| **LangChain** | 120k+ ⭐ | Complete platform (LangGraph + LangSmith) |
| **CrewAI** | 40k+ ⭐ | Multi-agents, production deployment |
| **Google ADK** | 15k+ ⭐ | Python code-first toolkit, simplified GCP integration |

<br>

This training: concepts applicable to all frameworks

<!-- .element class="admonition note"-->

Notes:
- LangChain: most complete ecosystem (120k+ stars, platform + observability)
- CrewAI: specialized multi-agent orchestration with deployment UI
- Google ADK: new official Google toolkit, code-first
- We teach fundamental concepts, not a specific framework

##==##

<!-- .slide -->

# Real Use Cases

<br>

**Where agents excel:**

<br>

- 🔍 **Augmented search** : Agents that search and synthesize
- 📊 **Data analysis** : Query databases, generate reports
- 🤖 **Automation** : Intelligent workflows with decisions
- 💬 **Customer support** : Autonomous ticket resolution
- 👨‍💻 **Dev assistants** : Review code, generate tests, debug
- 📝 **Content creation** : Research + writing + fact-checking

Notes:
- Concrete applications today
- Measurable ROI in these domains
- We'll build several during the training
- Think about your own use cases
- Concrete ROI example: Klarna (2024) - their AI agent handles 2/3 of customer support conversations, equivalent to 700 full-time agents, resolution in 2min vs 11min before (source: Klarna press release, Feb 2024)
- Another example: GitHub Copilot - developers 55% faster on coding tasks (GitHub study 2022)

##==##

<!-- .slide -->

# Ready to build your first agent?

<br>

### 🎯 What you'll learn:

<br>

1. ✅ Configure and use the right tools
2. ✅ Create agents with memory and tools
3. ✅ Orchestrate multiple agents together
4. ✅ Manage advanced features (streaming, errors, security)

<br>

### 🚀 Let's build!

Notes:
- Training roadmap
- Progressive and practical approach
- Lots of labs to practice
- At the end, you'll know how to build production-ready agents
