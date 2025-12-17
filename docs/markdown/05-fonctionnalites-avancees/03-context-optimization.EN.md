<!-- .slide: class="transition" -->

# Context Optimization

##==##

<!-- .slide -->

# The Context Challenge

## Why Optimize?

<br>

In a long conversation, history (context) accumulates rapidly.

### Major Problems:
1. **Exponential Costs** 💸 : You repay for re-reading all history with each new question.
2. **Latency** ⏱️ : "Time to First Token" increases with prompt size.
3. **Limited Window** 🪟 : Even with 1M/2M tokens, we eventually hit the limit or dilute model attention ("Lost in the Middle").

<br>

### ADK Solutions:
- **Caching** : Don't re-upload what doesn't change.
- **Compression** : Summarize what's old.

Notes:
Context optimization is critical to go from prototype (short chat) to production (long-duration assistants).

##==##

<!-- .slide: class="with-code max-height" -->

# Context Caching

## Reuse Static Context

Ideal for large documents or complex system instructions that don't change.

```python
from google.adk import Agent
from google.adk.apps.app import App
from google.adk.agents.context_cache_config import ContextCacheConfig

root_agent = Agent(
  # configure an agent using Gemini 2.5 or higher
)
app = App(
    name='my-caching-agent-app',
    root_agent=root_agent,
    context_cache_config=ContextCacheConfig(
        min_tokens=2048,    # Minimum number of tokens to activate cache
        ttl_seconds=600,    # Cache valid for 10 minutes
        cache_intervals=5,  # Updates cache every 5 calls
    ),
)
```

The model loads context once, and subsequent calls are much faster and cheaper ("cached input" pricing).

<!-- .element: class="admonition note" -->

Notes:
Gemini offers explicit "Context Caching". ADK manages it for you via this config.

##==##

<!-- .slide: class="with-code max-height" -->

# Context Compression

To manage an "infinite" conversation, we can't keep everything. Compression summarizes the past.

## Compression Workflow

![](./assets/images/context-compaction.png)

- **Event 3 completed** : First 3 events are compressed into a summary.
- **Event 6 completed** : Events 3 to 6 are compressed, with overlap of one previous event.

Notes:
This is transparent to the user. The model has "memory" of old facts via summary, but works on short context.

##==##
<!-- .slide: class="with-code max-height" -->
# Compression Implementation

```python
from google.adk.apps.app import App, EventsCompactionConfig
from google.adk.apps.llm_event_summarizer import LlmEventSummarizer
from google.adk.models import Gemini

# Define the AI model to be used for summarization:
summarization_llm = Gemini(model="gemini-2.5-flash")

# Create the summarizer with the custom model:
my_summarizer = LlmEventSummarizer(llm=summarization_llm)

# Configure the App with the custom summarizer and compaction settings:
app = App(
    name='my-agent',
    root_agent=root_agent,
    events_compaction_config=EventsCompactionConfig(
        compaction_interval=3,
        overlap_size=1,
        summarizer=my_summarizer,
    ),
)
```
