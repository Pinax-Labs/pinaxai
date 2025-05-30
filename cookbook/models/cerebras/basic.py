from pinaxai.agent import Agent
from pinaxai.models.cerebras import Cerebras

agent = Agent(
    model=Cerebras(id="llama-4-scout-17b-16e-instruct"),
    show_tool_calls=True,
    markdown=True,
    debug_mode=True,
)

# Print the response in the terminal
agent.print_response("write a two sentence horror story")
