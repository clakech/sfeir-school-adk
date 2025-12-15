from google.adk.agents import LlmAgent
from .post_generator_agent.agent import post_generator_agent

root_agent = LlmAgent(
    model='gemini-2.0-flash-001',
    name='root_agent',
    instruction="""
        Manage the workflow to create a LinkedIn post about AI advancements. Use sub-agents to search for news, summarize them, and write the post
        Always tranfer control to the sub-agents to complete the task.""",
    sub_agents=[post_generator_agent]
)
