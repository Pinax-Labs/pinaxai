"""Run `pip install duckduckgo-search` to install dependencies."""

import os

from pinaxai.agent import Agent
from pinaxai.models.nvidia import Nvidia
from pinaxai.tools.duckduckgo import DuckDuckGoTools

agent = Agent(
    model=Nvidia(id="meta/llama-3.3-70b-instruct"),
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True,
)

agent.print_response("Whats happening in France?", stream=True)
