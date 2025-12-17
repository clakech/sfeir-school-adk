<!-- .slide: class="transition" -->

# Loop Agent

##==##

<!-- .slide -->

# Loop Agent: Overview

## Iterative Execution with Condition

A **Loop Agent** executes **repeatedly** its sub-agents until a condition is met.

<br>

```
┌──────────────────┐
│  Execute agents  │
└────────┬─────────┘
         │
    Condition ? ────── No ──┐
         │                   │
        Yes                  │
         │                   │
     Terminate  ←──────────────┘
```

<br>

### Characteristics:
- 🔄 Like a `while` loop in programming
- ⏹️ Configurable stop conditions
- 🛡️ Maximum iteration limit

Notes:
Useful for iterative refinement and retry attempts

##==##

<!-- .slide -->

# When to Use Loop Agent?

## Typical Use Cases

<br>

### 🔄 Retry Mechanisms
```
Attempt API call → If failure, retry with backoff
```

### 📈 Iterative Refinement
```
Generate → Evaluate → If quality insufficient, improve
```

### 🎯 Progressive Improvement
```
Code → Tests → If tests fail, fix code
```

<br>

Use Loop Agent for tasks requiring **multiple attempts** or **progressive improvement**

<!-- .element: class="admonition important" -->

Notes:
Always define a stop condition to avoid infinite loops

##==##

<!-- .slide: class="with-code max-height" -->

# Loop Agent: Implementation

## Python Code

```python
from google.adk.agents import LoopAgent, LlmAgent

# Define agents for the loop
generator = LlmAgent(
    name="CodeGenerator",
    system_instruction="Generates Python code"
)

validator = LlmAgent(
    name="CodeValidator",
    system_instruction="Validates code quality and suggests improvements"
)

# Create loop with stop condition
refinement_loop = LoopAgent(
    name="CodeRefinementLoop",
    sub_agents=[generator, validator],
    max_iterations=5,
    stop_condition=lambda ctx: ctx.session.state.get("validation_passed")
)
```

Notes:
Loop stops when validation_passed is True OR after 5 max iterations

##==##

<!-- .slide -->

# Stop Conditions

## Loop Termination Strategies

<br>

### 1. **Maximum Number of Iterations**
```python
max_iterations=10  # Stop after 10 turns max
```

### 2. **State-based Condition**
```python
stop_condition=lambda ctx: ctx.session.state.get("quality_score") > 8
```

### 3. **Success/Failure Condition**
```python
stop_condition=lambda ctx: ctx.session.state.get("task_completed") == True
```

<br>

Always define `max_iterations` to avoid infinite loops
<!-- .element: class="admonition warning" -->

Notes:
Combine multiple conditions for more control

##==##

<!-- .slide: class="with-code max-height" -->

# Practical Example: Content Refinement

## Iterative Improvement Until Acceptable Quality

<br>

```python
content_generator = LlmAgent(
    name="ContentGenerator",
    system_instruction="Generates marketing content"
)

quality_checker = LlmAgent(
    name="QualityChecker",
    system_instruction="""Evaluates quality (1-10) on:
    - Clarity, Engagement, SEO
    - Set 'quality_passed' to True if score >= 8"""
)

content_refinement = LoopAgent(
    name="ContentRefinement",
    sub_agents=[content_generator, quality_checker],
    max_iterations=5,
    stop_condition=lambda ctx: ctx.session.state.get("quality_passed")
)

# Result: High quality content or 5 attempts
```

Notes:
Loop continues until content quality >= 8 or 5 max attempts
