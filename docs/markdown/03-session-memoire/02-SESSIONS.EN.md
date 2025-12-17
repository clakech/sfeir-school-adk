<!-- .slide: class="transition" -->

# Session

## The Conversation Thread

##==##

<!-- .slide -->

# Session: Overview

## The Atomic Unit of Conversation

<br>

A **Session** represents a unique and continuous conversation between a user and your agent.

<br>

```
User:  "Hello"
Agent: "Hello! How can I help you?"
User:  "What's the weather?"
Agent: "Let me check for you..."
```

<br>

### Characteristics:
- 🆔 Unique identifier to resume conversation
- 📝 Complete chronological history (Events)
- 💾 Contextual data (State)

Notes:
Without Session, the agent wouldn't remember that you just said hello

##==##

<!-- .slide -->

# When to Use Sessions?

## Typical Use Cases

<br>

### 💬 Conversational Chatbots
```
Customer support, personal assistants
```

<br>

### 🛒 Transactional Applications
```
E-commerce: maintain cart during navigation
```

<br>

### 🎓 Educational Applications
```
Adaptive tutors that remember progress
```

<br>

Use Sessions whenever you need **conversational continuity**

<!-- .element: class="admonition important" -->

Notes:
Any application with more than one user exchange benefits from Sessions

##==##

<!-- .slide: class="with-code max-height" -->

# SessionService: Implementation


## Python Code

<br>

<div style="font-size: 1.2em;">

```python
from google.adk.sessions import InMemorySessionService

# Initialize the service
session_service = InMemorySessionService()

# Create a new session
session = await session_service.create_session(
    app_name="travel_assistant",
    user_id="user_123"
)

print(f"Session created: {session.id}")
# Output: Session created: 550e8400-e29b-41d4-a716-446655440000
```

</div>

Notes:
ID is auto-generated (UUID) if you don't specify it

##==##

<!-- .slide: class="with-code" -->

# Session Lifecycle

## Adding Events

<br>

### Record Interactions

<div style="font-size: 1.1em;">

```python
from google.adk.types import UserMessage, ModelResponse

# User sends a message
user_event = UserMessage(text="I want to go to Tokyo")
await session_service.append_event(session, user_event)

# Agent responds
model_event = ModelResponse(text="For what dates?")
await session_service.append_event(session, model_event)

# Retrieve session with history
loaded = await session_service.get_session(session.id)
print(f"Number of events: {len(loaded.events)}")
# Output: Number of events: 2
```

</div>


`append_event` automatically updates `last_update_time`

<!-- .element: class="admonition tip" -->

Notes:
Each interaction is stored as a typed Event

##==##

<!-- .slide -->

# SessionService Backends

## From Development to Production

<br>

| Backend | Persistence | Setup | Use Case |
|---------|-------------|-------|-------------|
| **InMemory** | ❌ No | None | Dev, Tests |
| **Firestore** | ✅ Yes | GCP Project | Production |
| **SQLAlchemy** | ✅ Yes | Database | Production |

<br>

```python
# Production with Firestore
from google.adk.sessions import FirestoreSessionService

session_service = FirestoreSessionService(
    project_id="my-gcp-project"
)
```


Never use `InMemory` in production: all conversations are lost on restart.
<!-- .element: class="admonition warning" -->

Notes:
Backend choice doesn't change your agent code

##==##

<!-- .slide: class="with-code max-height" -->

# Practical Example: Multi-turn Chat

## Complete Conversation

<div style="font-size: 1.1em;">

```python
# 1. Create session
session = await session_service.create_session(
    app_name="travel_bot", user_id="alice"
)

# 2. First turn
await session_service.append_event(
    session, UserMessage(text="I want to travel")
)
# ... Agent responds ...

# 3. Second turn (same session)
await session_service.append_event(
    session, UserMessage(text="I prefer Asia")
)
# Agent has access to full history via session.events

# 4. Later, resume conversation
session = await session_service.get_session(session.id)
# All previous messages are accessible
```

</div>

Notes:
It's thanks to session.id that we resume the exact conversation
