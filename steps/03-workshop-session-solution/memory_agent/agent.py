from google.adk.agents import Agent
from google.adk.tools import load_memory

async def save_to_memory_callback(callback_context):
    """Callback to save session to memory after each turn."""
    await callback_context.add_session_to_memory()

# Create the agent
root_agent = Agent(
    model='gemini-2.5-flash',
    name='memory_agent',
    description='An agent that remembers user information across sessions.',
    instruction='You are a helpful assistant. When the user tells you their name, remember it by explicitly acknowledging it. If they ask for their name later, use the load_memory tool to retrieve past conversations.',
    after_agent_callback=save_to_memory_callback,
    tools=[load_memory],
)
