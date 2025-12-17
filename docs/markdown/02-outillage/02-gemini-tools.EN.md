<!-- .slide: class="transition" -->

# Native Gemini Tools

##==##

<!-- .slide: class="with-code" -->

# Google Search Tool

```python[2,9-10]
from google.adk.agents import Agent
from google.adk.tools import google_search

root_agent = Agent(
    name="basic_search_agent",
    model="gemini-2.0-flash",
    description="Agent to answer questions using Google Search.",
    instruction="I can answer your questions by searching the internet. Just ask me anything!",
    # google_search is a pre-built tool which allows the agent to perform Google searches.
    tools=[google_search]
)
```

| ✅ **Good use cases** | ❌ **Avoid** |
|------------------------|-----------------|
| Recent news search | Private company data |
| Fact and data verification | Highly specialized information |
| Public information exploration | Complex calculations or analysis |
| Technical documentation search | Data requiring freshness < 1 minute |
| Product/service comparison |  |

Notes:
- Google Search = public web data
- Limited by what is indexed by Google
- No control over exact sources
- For private data → use RAG or databases
- Complementary to other tools

##==##

<!-- .slide: class="with-code" -->

# Code Execution Tool

```python[2,7,9]
from google.adk.agents import LlmAgent
from google.adk.code_executors import BuiltInCodeExecutor

code_agent = LlmAgent(
    name="calculator_agent",
    model="gemini-2.0-flash",
    code_executor=BuiltInCodeExecutor(),
    instruction="""You are a calculator agent.
    When given a mathematical expression, write and execute Python code to calculate the result.
    Return only the final numerical result as plain text, without markdown or code blocks.
    """,
    description="Executes Python code to perform calculations.",
)
```

Notes:
- Gemini generates code AND executes it
- Isolated environment on Google side
- Enables precise calculations and visualizations
- Python libraries available: numpy, pandas, matplotlib, etc.
- No network or filesystem access

##==##

<!-- .slide -->

# Code Execution: Capabilities

**What Code Execution can do:**

| Category | Examples |
|-----------|----------|
| **Calculations** | Complex mathematics, statistics |
| **Data science** | Dataset analysis, transformations |
| **Visualization** | Charts with matplotlib/seaborn |
| **Data processing** | Parsing, cleaning, aggregation |
| **Simulations** | Monte Carlo, numerical models |


Notes:
- Very powerful for analytical tasks
- Avoids LLM calculation errors
- Can generate complex visualizations
- Scientific libraries pre-installed
- Deterministic and verifiable results

##==##

<!-- .slide -->

# Code Execution: Limits and Security

❌ **Not available:**
- Network access (no HTTP/API calls)
- Filesystem access
- Third-party package installation
- System command execution
- Long operations (timeout ~30s)

<br>

✅ **Security:**
- No access to user data
- No persistence between executions
- Each execution is isolated

Notes:
- Limits are for security
- No risk of injection or exfiltration
- Environment is ephemeral
- For advanced needs → GKE Code Executor
- Short timeout = avoid infinite loops

##==##

<!-- .slide -->

# GKE Code Executor

Code execution offloaded to a specific Pod and not on the ADK agent infrastructure

Better security, but some prerequisites:

- The ADK agent must be deployed in a GKE cluster with a node pool using gVisor
- The service account associated with the agent must be able to
  - Create, monitor, delete jobs in the cluster
  - Create configmaps to inject code to execute
  - Retrieve pod list and access pod logs
- The application must also have the adk library with the GKE add-on `pip install google-adk[gke]`
##==##

<!-- .slide: class="with-code" -->

# Using GKE Code Executor

```python
from google.adk.agents import LlmAgent
from google.adk.code_executors import GkeCodeExecutor

gke_executor = GkeCodeExecutor(
    namespace="agent-sandbox",
    timeout_seconds=600,
    cpu_limit="1000m",  # 1 CPU core
    mem_limit="1Gi",
)

gke_agent = LlmAgent(
    name="gke_coding_agent",
    model="gemini-2.0-flash",
    instruction="You are a helpful AI agent that writes and executes Python code.",
    code_executor=gke_executor,
)
```

Pay attention to service account access rights in the configured namespace

<!-- .element: class="admonition warning" -->

##==##

<!-- .slide -->

# Google Cloud Tools

Google Cloud Tools allow you to easily connect your ADK agents to Google Cloud services and many enterprise systems (Salesforce, SAP, etc.).

**Main use cases:**
- Call custom APIs hosted on Apigee
- Use pre-built connectors (Salesforce, Workday, etc.)
- Orchestrate automation workflows (Application Integration)
- Access databases (Spanner, AlloyDB, Postgres...)

These tools integrate natively into ADK and facilitate secure access to your cloud resources.

##==##

<!-- .slide -->

# Apigee API Hub Tools

Allows you to transform any API documented in Apigee API Hub into a tool usable by an agent.

**Key steps:**
1. Generate an access token with `gcloud auth print-access-token`
2. Verify IAM permissions (e.g. `roles/apihub.viewer`)
3. Create a tool with `APIHubToolset` by providing the token and API resource name
4. Add the tool to your ADK agent

**Integration example:**
```python
from google.adk.tools.apihub_tool.apihub_toolset import APIHubToolset
sample_toolset = APIHubToolset(
  name="apihub-sample-tool",
  description="Sample Tool",
  access_token="...",
  apihub_resource_name="..."
)
```

##==##

<!-- .slide -->

# Application Integration Tools

Provides access to over 100 enterprise connectors (Salesforce, ServiceNow, JIRA, SAP...) and allows orchestration of complex workflows.

**Features:**
- Supports SaaS and on-premise applications
- Enables federated search across multiple systems
- Relies on IAM roles for security

**Example tool creation:**
```python
from google.adk.tools.application_integration_tool.application_integration_toolset import ApplicationIntegrationToolset
connector_tool = ApplicationIntegrationToolset(
  project="my-project",
  location="us-central1",
  connection="my-connection",
  entity_operations={"Account": ["LIST"]},
  actions=["action1"],
  service_account_json='{...}'
)
```

##==##

<!-- .slide -->

# Security and Authentication

Google Cloud Tools rely on Google Cloud authentication mechanisms:
- Access token (for development)
- Service Account (recommended for production)
- OAuth2 support for dynamic connectors

**Best practices:**
- Always limit IAM permissions to the strict minimum
- Prefer service accounts for production
- Credentials should never be exposed in source code
