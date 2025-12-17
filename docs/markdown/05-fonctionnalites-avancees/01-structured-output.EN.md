<!-- .slide: class="transition" -->

# Structured Output

##==##

<!-- .slide -->

# Structured Output: Overview

## Why Structure Exchanges?

LLMs naturally generate unstructured text. To integrate them into software systems, we need **guarantees** on input and output formats.

<br>

### 3 Key Mechanisms:

1. **Input Schema** 📥 : Validates what enters the agent
2. **Output Schema** 📤 : Forces output format (JSON)
3. **Output Key** 🔑 : Automatically saves result in state

Without structure, parsing responses is fragile and error-prone. These tools make agents deterministic in their format.
<!-- .element: class="admonition tip" -->

##==##

<!-- .slide: class="with-code max-height" -->

# Input Schema

## Validate User Inputs

Defines the expected structure for messages sent to the agent.

```python
from google.adk.agents import LlmAgent
from pydantic import BaseModel, Field

# Define input schema
class UserQuery(BaseModel):
    city: str = Field(description="Target city")
    days: int = Field(description="Trip duration", ge=1)

# Agent configuration
travel_agent = LlmAgent(
    name="TravelGuide",
    model="gemini-2.5-flash",
    input_schema=UserQuery,  # Automatic validation
    system_instruction="Create a travel itinerary."
)
```

Using Pydantic for validation, if input doesn't match schema, an error is raised before even calling the model.

<!-- .element: class="admonition note" -->

##==##

<!-- .slide: class="with-code max-height" -->

# Output Schema

## Force Structured Response (JSON)

Guarantees that the agent will always respond with a valid JSON object conforming to your model.

```python
class TripPlan(BaseModel):
    destination: str
    activities: list[str]
    estimated_cost: float

planner = LlmAgent(
    name="Planner",
    model="gemini-2.0-flash",
    output_schema=TripPlan, # Forces strict JSON
    system_instruction="Generates a structured travel plan."
)

# Usage
response = await planner.run_async("Paris for 3 days")
# response.text will be valid JSON:
# {"destination": "Paris", "activities": [...], "estimated_cost": 500.0}
```

Essential for other systems (API, Frontend, Database) to consume agent response without complex parsing.

<!-- .element: class="admonition tip" -->

##==##

<!-- .slide: class="with-code" -->

# Output Key

## Multi-Agent Data Sharing

Automatically saves the response in `SessionState` for following agents.

```python
researcher = LlmAgent(
    name="Researcher",
    # ...
    output_key="research_data"  # Saves in state["research_data"]
)
writer = LlmAgent(
    name="Writer",
    # ...
    # No need to explicitly pass data,
    # writer has access to global state
    system_instruction="Use research data to write an article: {research_data}."
)
# Avoids having to manually manage data flow in orchestration code.
sequential_agent = SequentialAgent(
    name="ResearchAndWrite",
    agents=[researcher, writer]
)
```

In a SequentialAgent, this is the cleanest way to pass the data "baton" from one agent to another.

<!-- .element: class="admonition tip" -->
