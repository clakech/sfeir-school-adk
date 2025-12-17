<!-- .slide: class="transition" -->

# Sequential Agent

##==##

<!-- .slide -->

# Sequential Agent: Overview

## The Assembly Line Pattern

<br>

A **Sequential Agent** executes its sub-agents **one after another**, in a predefined order.

<br>

```
Agent 1 ➜ Agent 2 ➜ Agent 3 ➜ Agent 4
```

<br>

### Characteristics:
- ✅ Deterministic and predictable flow
- ✅ One agent's output can become the next's input
- ✅ Ideal for multi-step pipelines

Notes:
Like a production line: each step must be completed before the next

##==##

<!-- .slide -->

# When to Use Sequential Agent?

## Typical Use Cases

<br>

### 📊 Data Pipelines
```
Retrieval ➜ Cleaning ➜ Analysis ➜ Summary
```

### 📝 Document Processing
```
Loading ➜ Extraction ➜ Translation ➜ Formatting
```

### 🎨 Content Creation
```
Research ➜ Outline ➜ Writing ➜ Review
```

<br>

Use Sequential Agent when steps **depend on each other**

<!-- .element: class="admonition important" -->

Notes:
Each step requires results from the previous step

##==##

<!-- .slide: class="with-code max-height" -->

# Sequential Agent: Implementation

## Python Code

```python
from google.adk.agents import SequentialAgent, LlmAgent

# Define sub-agents
step1 = LlmAgent(
    name="DataFetcher",
    model="gemini-2.0-flash",
    system_instruction="Retrieves data from sources"
)

step2 = LlmAgent(name="DataCleaner", ...)
step3 = LlmAgent(name="DataAnalyzer", ...)

# Create sequential workflow
pipeline = SequentialAgent(
    name="DataPipeline",
    sub_agents=[step1, step2, step3]
)
```

Notes:
Agents execute in array order: step1 → step2 → step3

##==##

<!-- .slide: class="with-code" -->

# Sequential State Management

## Data Passing Between Agents

<br>

### Using `ctx.session.state`

```python
# Agent 1: Writes to state
ctx.session.state["raw_data"] = data

# Agent 2: Reads state
raw_data = ctx.session.state.get("raw_data")
cleaned_data = clean(raw_data)
ctx.session.state["cleaned_data"] = cleaned_data

# Agent 3: Uses previous results
results = analyze(ctx.session.state.get("cleaned_data"))
```

<br>

State is **shared** between all agents in the hierarchy

<!-- .element: class="admonition tip" -->

Notes:
Like a shared whiteboard that each agent can read and modify

##==##

<!-- .slide: class="with-code max-height" -->

# Practical Example: Blog Article Creation

## Content Generation Pipeline

```python
research_agent = LlmAgent(
    name="Researcher",
    system_instruction="Research information on the topic"
)

outline_agent = LlmAgent(
    name="Outliner", 
    system_instruction="Create a structured outline"
)

writer_agent = LlmAgent(
    name="Writer",
    system_instruction="Write complete content"
)

reviewer_agent = LlmAgent(
    name="Reviewer",
    system_instruction="Review and improve quality"
)

blog_pipeline = SequentialAgent(
    name="BlogCreator",
    sub_agents=[research_agent, outline_agent, writer_agent, reviewer_agent]
)
```

Notes:
Each step progressively improves the final result
