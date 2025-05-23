from pinaxai.agent import Agent
from pinaxai.models.openai import OpenAIChat
from pinaxai.tools.duckduckgo import DuckDuckGoTools

agent = Agent(
    model=OpenAIChat(id="gpt-4.5-preview"),
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
)

agent.print_response("Whats the latest about gpt 4.5?", markdown=True)
