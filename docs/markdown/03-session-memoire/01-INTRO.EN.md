<!-- .slide: class="transition" -->

# Conversational Context

## Session, State and Memory

##==##

<!-- .slide -->

# Why is Context Crucial?

## Transform unique interactions into conversation

<br>

LLMs are by nature **stateless** (without state). Each call is independent.
To create a conversational experience, it is necessary to manage context.

<br>
<br>
<br>

### The 3 Levels of ADK Persistence:

1. **Session** 🧵 : The immediate discussion thread (Short term)
2. **State** 📝 : Structured session data (Short term)
3. **Memory** 🧠 : Vector knowledge base (Long term)

Notes:
- Analogy:
  - Session = Working memory (RAM)
  - State = Notebook on the desk
  - Memory = Archive library

##==##

<!-- .slide -->

# Context Architecture

## Service Overview

<div class="col">

### Key Components

- **SessionService** : Manages conversation lifecycle.
- **MemoryService** : Manages indexing and semantic search.
- **Agent** : Orchestrates service calls via Tools or Runtime.

<br>
<br>

![full-center](./assets/images/LongTermShortTerm.svg)

</div>


Notes:
- Clear distinction between "Session" storage (often fast SQL/NoSQL) and "Memory" (Vector DB for semantic search).

##==##

<!-- .slide -->

# From Prototype to Production

## Choose the Right Implementation

ADK offers interchangeable implementations for each service.

<br>

| Environment | SessionService | MemoryService | Characteristics |
|---------------|----------------|---------------|------------------|
| **Dev / Test** | `InMemorySession` | `InMemoryMemory` | Fast, **non-persistent** |
| **Production** | `Firestore` | `VertexAI MemoryBank` | Scalable, **persistent** |

<br>
<br>

Never use `InMemory` services in production, as all data is lost on application restart.
<!-- .element: class="admonition important" -->

Notes:
- This flexibility allows coding the agent once and changing infrastructure by simple configuration.
