from google.adk.agents import Agent
from google.adk.memory.memory_service import InMemoryMemoryService
from google.adk.session.session_service import InMemorySessionService
from google.adk.tools import load_memory

# Initialize services
memory_service = InMemoryMemoryService()
session_service = InMemorySessionService()

async def auto_save_callback(ctx):
    """Callback to save session to memory after each turn."""
    # print(f"DEBUG: Saving session {ctx.session.session_id} to memory")
    await ctx.memory_service.add_session_to_memory(ctx.session)

# Create the agent
root_agent = Agent(
    model='gemini-2.5-flash',
    name='memory_agent',
    description='An agent that remembers user name across sessions.',
    instruction='You are a helpful assistant. If the user tells you their name, remember it. If they ask for their name, use the load_memory tool or context to retrieve it.',
    memory_service=memory_service,
    session_service=session_service,
    after_agent_callback=auto_save_callback,
    tools=[load_memory]
)
