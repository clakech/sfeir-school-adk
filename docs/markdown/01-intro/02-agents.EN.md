<!-- .slide: class="transition"-->

# AI Agents

##==##

<!-- .slide -->

# What is an AI Agent?

<br>

### An agent = LLM + Action capabilities

<br>

<div style="display: flex; justify-content: center; align-items: center; gap: 40px; font-size: 1.2em;">
  <div style="text-align: center;">
    <div style="border: 3px solid #00c7ff; border-radius: 10px; padding: 30px 40px; background: rgba(0, 199, 255, 0.1);">
      🧠<br><strong>LLM</strong><br>(Brain)
    </div>
  </div>
  <div style="font-size: 2em; color: #00c7ff;">↔</div>
  <div style="text-align: center;">
    <div style="border: 3px solid #00c7ff; border-radius: 10px; padding: 30px 40px; background: rgba(0, 199, 255, 0.1);">
      🔧<br><strong>Tools</strong><br>(Actions)
    </div>
  </div>
</div>

<div style="text-align: center; margin-top: 20px; font-size: 1.2em; color: #00c7ff;">
  ↕<br>
  💾 <strong>Memory</strong>
</div>

<br>

**An agent can reason, decide and act autonomously**

Notes:
- Clear and visual definition
- The 3 key components: LLM + Tools + Memory
- Autonomy = ability to chain multiple actions

##==##

<!-- .slide -->

# Anatomy of an Agent

<br>

### The 4 essential components

<br>

1. **🧠 LLM** : The "brain" that reasons
2. **🔧 Tools** : The action capabilities
3. **💾 Memory** : Context and history
4. **📋 Instructions (System Prompt)** : Personality and rules

Notes:
- Detail each component
- Each is indispensable
- We'll explore them one by one

##==##

<!-- .slide -->

# 🧠 The LLM: The "brain"

**Popular models for agents (Dec 2025):**

<br>

| Model | Publisher | Strengths |
|--------|---------|--------------|
| GPT-5.2 | OpenAI | Advanced reasoning, more conversational |
| Claude Opus 4.5 | Anthropic | Excellence in code, autonomous agents |
| Gemini 3 Pro | Google | Coding and complex tasks, multi-modal |
| Gemini 2.5 Flash | Google | Fast performance, daily use |

<br>

The choice of model impacts the agent's capabilities
<!-- .element: class="admonition note"--> 

Notes:
- GPT-5.1: nov 2025, adaptive thinking and advanced personalization
- Claude 4.5: model optimized for agents and developers
- Gemini 2.5: recent family with Pro (complex tasks) and Flash (fast)
- Gemini 2.5 Flash Image: native image generation and editing
- Grok 4: july 2025, by xAI (Elon Musk), integrated into Twitter/X
- Grok 4 Fast: sept 2025, optimized version for speed

##==##

<!-- .slide -->

# 🔧 Tools (Functions)

**Tools allow agents to act in the real world**

<br>

```python
tools = [
    {
        "name": "search_web",
        "description": "Search the internet",
        "parameters": {"query": "string"}
    },
    {
        "name": "send_email",
        "description": "Send an email",
        "parameters": {"to": "string", "subject": "string", "body": "string"}
    }
]
```

<br>

The LLM decides when and how to use these tools

Notes:
- Function calling = native capability of modern LLMs
- The LLM chooses the tool based on context
- Standard format (OpenAI Functions, Anthropic Tools)

##==##

<!-- .slide -->

# 💾 Memory

**Different types of memory:**

<br>

| Type | Duration | Usage |
|------|-------|-------|
| **Short term** | One conversation | LLM context window |
| **Episodic** | Session/Day | Summaries, key events |
| **Long term** | Permanent | Knowledge base, RAG |

<br>

Notes:
- Memory enables continuity
- Short term = limited by context window
- Long term = requires techniques like RAG
- Agents can decide what to remember
