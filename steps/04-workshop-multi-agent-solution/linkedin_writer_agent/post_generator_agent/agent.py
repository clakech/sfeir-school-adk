from google.adk.agents import SequentialAgent
from .news_search_agent.agent import news_search_agent
from .linkedin_ghost_writer.agent import linkedin_ghost_writer
from .news_summarizer.agent import news_summarizer 

post_generator_agent = SequentialAgent(
    name="post_generator_agent",
    description="An agent that generates a LinkedIn post by searching for news, summarizing them, and writing the post regarding user's topic.",
    sub_agents=[news_search_agent, news_summarizer, linkedin_ghost_writer]
)
