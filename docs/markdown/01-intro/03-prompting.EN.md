<!-- .slide: class="transition" -->

# Prompting

##==##

<!-- .slide -->

# 📋 The System Prompt

<br>

**The instructions that define your agent:**

<br>

```text
You are an expert Python developer assistant.
You help developers debug their code.

Rules:
- Always explain your reasoning
- Provide tested and commented code
- Ask for clarifications if needed
- Use the "run_code" tool to test
- Never execute destructive code (DROP, DELETE)
- Do not access sensitive system files

Your style: professional but accessible
```

<br>

The system prompt is your "contract" with the agent

<!-- .element: class="admonition note"-->

Notes:
- This is the agent's identity and rules
- Clearly define expected behavior
- Include examples if needed
- Can contain security constraints

##==##

<!-- .slide -->

# Fundamental Pattern: ReAct

<br>

**Re**asoning + **Act**ing = Thought/action cycle

<br>

<div style="font-size: 0.95em;">

**1. 💭 Thought (Reasoning)** → The agent analyzes and plans

**2. 🎬 Action** → Call a tool (API, search, calculation...)

**3. 👀 Observation** → Receive and analyze the result

**4. 💭 New thought** → Continue or respond?

</div>

<br>

### ↻ Loop until complete resolution

Notes:
- ReAct = Google/Princeton research paper 2022
- Most used pattern in modern agents
- Each step is explicit and traceable
- The agent can do multiple cycles before responding
- Avoids hallucinations by verifying through actions

##==##

<!-- .slide -->

# ReAct: Detailed Example

<br>

**❓ Question: "What's the weather in Paris and should I take an umbrella?"**

<br>

```text
💭 Thought 1: "I need to search for current weather in Paris"
🎬 Action 1: search_web("weather Paris real-time")
👀 Observation 1: "18°C, clear sky, wind 10 km/h"

💭 Thought 2: "I need to check rain forecasts"
🎬 Action 2: get_weather_forecast("Paris", hours=6)
👀 Observation 2: "0% precipitation expected in the next 6h"

💭 Thought 3: "I have all the info, I can respond"
✅ Response: "It's 18°C in Paris with clear skies. 
   No rain expected, you don't need an umbrella!"
```

Notes:
- The agent does 2 cycles before responding
- Each action brings complementary information
- Reasoning is transparent and verifiable
- Factual response based on real data
