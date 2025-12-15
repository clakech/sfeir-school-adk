from google.adk.agents import  LlmAgent
from google.adk.tools import google_search
from .prompt import PROMPT

news_search_agent = LlmAgent(
    model='gemini-2.0-flash-001',
    name='news_search_agent',
    description='An agent searching the web to get news about a specific topic asked by the user.',
    instruction=PROMPT,
    tools=[google_search],
    output_key="news"
)
