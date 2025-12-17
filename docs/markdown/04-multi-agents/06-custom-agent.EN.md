<!-- .slide: class="transition" -->

# Custom Agents

##==##

<!-- .slide -->

# Custom Agent: Concept

## Beyond Predefined Workflows

A **Custom Agent** inherits from `BaseAgent` and implements its own orchestration logic via `_run_async_impl`.

### Characteristics:
- 🎨 **Total Control** over execution logic
- 🔀 **Custom Conditional** logic
- 🧩 **Unique Patterns** not covered by Sequential/Parallel/Loop
- 🔧 **External Integrations** (APIs, DB, etc.)

Master LLMAgent and WorkflowAgent first
<!-- .element: class="admonition warning" -->

Use Custom Agent when Sequential, Parallel, Loop are not enough
<!-- .element: class="admonition note" -->

##==##

<!-- .slide -->

# When to Use Custom Agent?

## Situations Requiring Custom Control

<br>

### 🔀 **Conditional Logic**
Different paths based on runtime conditions

### 📊 **Complex State Management**
Sophisticated state management logic

### 🎯 **Dynamic Agent Selection**
Choose sub-agents on the fly

In short: use when predefined workflows are not enough
<!-- .element: class="admonition note" -->

##==##

<!-- .slide: class="with-code max-height" -->

# Custom Agent Structure

## Inheriting from BaseAgent

```python
from google.adk.agents import BaseAgent, LlmAgent
from google.adk.types import SessionContext

class StoryFlowAgent(BaseAgent):
    def __init__(self, name: str):
        # Agent initialization
        super().__init__(name=name)
        self.planner = LlmAgent(name="Planner", ...)
        self.writer = LlmAgent(name="Writer", ...)
        self.editor = LlmAgent(name="Editor", ...)
    
    async def _run_async_impl(self, ctx: SessionContext):
        plan = await self.planner.run_async(ctx) # 1. Planning
        # 2. Conditional logic
        if ctx.session.state.get("complexity") > 5:
            # Multi-chapter logic
            ...
        else:
            # Simple logic
            ...
        # 3. Final editing
        return await self.editor.run_async(ctx)
```

_run_async_impl is the method where you implement your custom logic
<!-- .element: class="admonition note" -->

##==##

<!-- .slide: class="with-code" -->

# Custom Logic Implementation

## Common Operations

<br>

### Access Context and State
```python
async def _run_async_impl(self, ctx: SessionContext):
    # Read state
    user_level = ctx.session.state.get("user_level", "beginner")
    # Write to state
    ctx.session.state["processed"] = True
```

### Call Sub-agents
```python
# Execute a sub-agent
result = await self.sub_agent.run_async(ctx)
```

### Make Decisions
```python
# Conditional logic
if condition:
    await self.agent_a.run_async(ctx)
else:
    await self.agent_b.run_async(ctx)
```

##==##

<!-- .slide -->

# State Management

## State Management in Custom Agents

<br>

### Reading State
```python
value = ctx.session.state.get("key")
value_with_default = ctx.session.state.get("key", "default_value")
```

### Writing to State
```python
ctx.session.state["result"] = computed_value
ctx.session.state["step_completed"] = True
```

### Sharing with Sub-agents
```python
# State is automatically shared
ctx.session.state["shared_data"] = data
await self.sub_agent.run_async(ctx)  # Can access shared_data
```

<br>

State persists for the entire session duration
<!-- .element: class="admonition note" -->


##==##

<!-- .slide: class="with-code max-height" -->

# Practical Example: Adaptive Learning Agent

## Dynamic Adaptation to User Level

```python
class AdaptiveTutorAgent(BaseAgent):
    def __init__(self, name: str):
        super().__init__(name=name)
        self.assessor = LlmAgent(name="LevelAssessor", ...)
        self.beginner_tutor = LlmAgent(name="BeginnerTutor", ...)
        self.intermediate_tutor = LlmAgent(name="IntermediateTutor", ...)
        self.advanced_tutor = LlmAgent(name="AdvancedTutor", ...)
    
    async def _run_async_impl(self, ctx: SessionContext):
        # 1. Assess level
        await self.assessor.run_async(ctx)
        level = ctx.session.state.get("user_level")
        
        # 2. Route to appropriate tutor
        if level == "beginner":
            return await self.beginner_tutor.run_async(ctx)
        elif level == "intermediate":
            return await self.intermediate_tutor.run_async(ctx)
        else:
            return await self.advanced_tutor.run_async(ctx)
```

Notes:
Dynamic sub-agent selection based on assessment
