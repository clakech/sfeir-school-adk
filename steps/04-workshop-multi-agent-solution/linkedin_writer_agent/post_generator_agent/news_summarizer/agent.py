from google.adk.agents import  LlmAgent

news_summarizer = LlmAgent(
    name="news_summarizer",
    model='gemini-2.0-flash-001',
    instruction="Read state['news']. Summarize the key points. Save to state['summary'].",
    output_key="summary", # Overwrites previous summary in state
)
