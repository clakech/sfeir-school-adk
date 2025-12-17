<!-- .slide: class="transition" -->

# Memory

## Persistence and Semantic Search

##==##

<!-- .slide -->

# Memory: Overview

## Beyond the Session

<br>

**Memory** allows the agent to remember information from **past sessions** or **external documents**.

<br>

<div style="font-size: 1.6em;">

```markdown
Session 1 (Yesterday) : "I love the Park Hyatt Tokyo"
Session 2 (Today) : "I want to return to my favorite hotel."
                           ↓
Agent : "Are you talking about the Park Hyatt Tokyo?"
```

</div>

<br>

### Characteristics:
- 🧠 Long-term knowledge
- 🔍 Semantic search (not just keywords)
- 🔄 Cross-session: retrieve info from other conversations

Notes:
Memory = Agent's RAM, State = Session working memory

##==##

<!-- .slide -->

# RAG: How Does It Work?

## Retrieval Augmented Generation

<br>

<div style="font-size: 1.1em;">


1. **Ingestion:** Sessions → Chunks → Embeddings → Vector DB

<br>
<br>

2. **Search:**   Query → Embedding → Similarity → Retrieval

<br>
<br>

3. **Augmentation:**   Context + Query → LLM → Response

</div>

<br>
<br>

### Pipeline Simplified by ADK:
1. **add_session_to_memory()** : Automatic ingestion
2. **search_memory()** : Vector search
3. **PreloadMemoryTool** : Context injection

Notes:
ADK abstracts all RAG complexity

##==##

<!-- .slide -->

# When to Use Memory?

## Typical Use Cases

<br>

### 🔄 Continuity Between Sessions

- Remember preferences from one visit to another

<br>
<br>

### 📚 Knowledge Base

- Documentation, FAQ, product catalog

<br>
<br>

### 🤝 Long-term Personalization

- Assistant that learns from each interaction


<br>
<br>

Use Memory when information must **survive the session**

<!-- .element: class="admonition important" -->

Notes:
If it's important for future conversations → Memory
If it's just for current conversation → State

##==##

<!-- .slide: class="with-code max-height" -->

# MemoryService: Implementation

## Python Code

<div style="font-size: 1.2em;">

```python
from google.adk.memory import InMemoryMemoryService

# Initialize the service
memory_service = InMemoryMemoryService()

# Ingestion: Save a completed session
await memory_service.add_session_to_memory(
    session,
    include_state=True  # Also index State
)

# Search: Retrieve information
results = await memory_service.search_memory(
    query="favorite hotel Tokyo",
    limit=3
)

for result in results:
    print(f"{result.text} (Score: {result.score})")
```

</div>

Notes:
include_state=True allows also retrieving preferences stored in State

##==##

<!-- .slide: class="with-code" -->

# Integration via Tools

## PreloadMemoryTool: The Automatic Pattern

<div style="font-size: 1.2em;">

```python
from google.adk.tools.preload_memory_tool import PreloadMemoryTool

# This tool executes BEFORE each turn
memory_tool = PreloadMemoryTool(
    memory_service=memory_service,
    max_results=2
)

agent = LlmAgent(
    name="TravelAgent",
    tools=[memory_tool],
    instruction="""
You are a travel agent.
Use the provided context to personalize responses.
"""
)
```

</div>


<div style="font-size: 0.75em;">

**Flow:** User Input → Memory Search → Context Injection → LLM → Response

</div>

<!-- .element: class="admonition tip" -->

Notes:
The agent doesn't even need to know it's using memory

##==##

<!-- .slide -->

# MemoryService Backends

## From Prototype to Production


| Backend | Search | Setup | Use Case |
|---------|-----------|-------|-------------|
| **InMemory** | Keywords | None | Dev, Tests |
| **VertexAI Memory Bank** | Vector | GCP | Production |

<br>

<div style="font-size: 1.5em;">

```python
# Example with Vertex AI
from google.adk.memory import VertexAiMemoryBankService

memory_service = VertexAiMemoryBankService(
    project_id="my-gcp-project",
    location="us-central1",
    memory_bank_id="customer-preferences"
)
```

</div>

<br>

<div style="font-size: 0.8em;">

Vertex AI Memory Bank automatically manages extraction of "significant memories" from sessions.
<!-- .element: class="admonition warning" -->

</div>

Notes:
Vertex AI is much smarter than InMemory for extracting what's important

##==##

<!-- .slide: class="with-code max-height" -->

# Practical Example: Agent with Memory

## Complete Cycle

```python
# 1. Setup services
session_service = InMemorySessionService()
memory_service = InMemoryMemoryService()

# 2. Session 1: First conversation
session1 = await session_service.create_session(...)
# ... Conversation: "I love Japanese cuisine" ...
await memory_service.add_session_to_memory(session1)

# 3. Session 2: New conversation (next day)
session2 = await session_service.create_session(...)

# 4. Agent automatically searches (via PreloadMemoryTool)
# Query: "restaurant recommendations"
# Memory finds: "User loves Japanese cuisine"

# 5. Agent responds intelligently
# "I recommend these Japanese restaurants..."
```

Notes:
Two different sessions, but agent remembers thanks to Memory
