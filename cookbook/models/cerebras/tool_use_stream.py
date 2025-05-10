from pinaxai.agent import Agent
from pinaxai.models.cerebras import Cerebras
from pinaxai.tools.duckduckgo import DuckDuckGoTools

agent = Agent(
    model=Cerebras(id="llama-3.3-70b"),
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True,
    debug_mode=True,
)

# Print the response in the terminal
agent.print_response("Whats happening in France?", stream=True)
