<!-- .slide: class="transition" -->

# Parallel Agent

##==##

<!-- .slide: class="with-code" -->

# Parallel Agent: Overview

## Simultaneous Task Execution

<br>

A **Parallel Agent** executes **all its sub-agents at the same time** (concurrency).

<br>

```
       ┌─ Agent 1 ─┐
Start ─┼─ Agent 2 ─┼─ Aggregation ─ Result
       └─ Agent 3 ─┘
```

### Characteristics:
- ⚡ Concurrent execution
- 📦 Result aggregation
- 🎯 Ideal for independent tasks

Notes:
Like a manager assigning tasks to multiple employees simultaneously

##==##

<!-- .slide -->

# When to Use Parallel Agent?

## Typical Use Cases

<br>

### 🌐 Multiple API Calls
```
Weather API + News API + Stock API (simultaneously)
```

### 🔍 Multi-source Data Collection
```
Web Scraping + Database + External API (in parallel)
```

### 🏢 Competitive Analysis
```
Analyze Competitor A + Competitor B + Competitor C
```

<br>

Use Parallel Agent when tasks are **independent** and don't need each other's results
<!-- .element: class="admonition important" -->

Notes:
Performance optimization: reduces total execution time

##==##

<!-- .slide: class="with-code max-height" -->

# Parallel Agent: Implementation

## Python Code

```python
from google.adk.agents import ParallelAgent, LlmAgent

# Define independent sub-agents
weather_agent = LlmAgent(
    name="WeatherAPI",
    system_instruction="Retrieves weather data"
)

news_agent = LlmAgent(
    name="NewsAPI",
    system_instruction="Retrieves news"
)

stock_agent = LlmAgent(
    name="StockAPI",
    system_instruction="Retrieves stock data"
)

# Create parallel workflow
parallel_fetcher = ParallelAgent(
    name="MultiSourceFetcher",
    sub_agents=[weather_agent, news_agent, stock_agent]
)
```

Notes:
The three agents execute simultaneously, no guaranteed order

##==##

<!-- .slide: class="with-code" -->

# Result Aggregation

## Managing Parallel Results

<br>

### Key Points:

- ⏱️ **Timing** : Agents may finish at different times
- 🔄 **Collection** : Results are collected after all agents finish
- ❌ **Error Handling** : If one agent fails, others continue
- 📊 **Combination** : Results are available in `ctx.session.state`

<br>

```python
# All results available after execution
all_data = {
    "weather": ctx.session.state.get("weather_data"),
    "news": ctx.session.state.get("news_data"),
    "stocks": ctx.session.state.get("stock_data")
}
```

Notes:
ParallelAgent waits for all sub-agents to finish before continuing

##==##

<!-- .slide: class="with-code max-height" -->

# Practical Example: Competitive Analysis

## Simultaneous Research on Multiple Competitors

```python
competitor1_agent = LlmAgent(
    name="Competitor1Analyzer",
    system_instruction="Analyze competitor 1: strategy, pricing, products"
)

competitor2_agent = LlmAgent(
    name="Competitor2Analyzer",
    system_instruction="Analyze competitor 2: strategy, pricing, products"
)

competitor3_agent = LlmAgent(
    name="Competitor3Analyzer",
    system_instruction="Analyze competitor 3: strategy, pricing, products"
)

competitive_analysis = ParallelAgent(
    name="CompetitiveAnalysis",
    sub_agents=[competitor1_agent, competitor2_agent, competitor3_agent]
)

# Result: complete report on all competitors
```

Notes:
Time savings: 3x faster than sequential approach
