from google.adk.agents import  LlmAgent
from .prompt import PROMPT

linkedin_ghost_writer = LlmAgent(
    name="linkedin_ghost_writer",
    model='gemini-2.0-flash-001',
    instruction=PROMPT,
    output_key="linkedin_post"
)
