from google.adk.agents import Agent
from google.adk.tools import google_search

root_agent = Agent(
    model='gemini-2.0-flash-001',
    name='root_agent',
    description='An agent searching the web to get news about IA advancements and new models.',
    instruction="""
        You are a news agent that retrieves the latest information about AI advancements and new models by searching the web. Use the Google Search tool to find relevant news articles and summarize the key points.
        Always use the Google Search tool to find up-to-date information.
    """,
    tools=[google_search]
)
