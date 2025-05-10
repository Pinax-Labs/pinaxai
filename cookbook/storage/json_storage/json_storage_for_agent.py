"""Run `pip install duckduckgo-search openai` to install dependencies."""

from pinaxai.agent import Agent
from pinaxai.models.openai import OpenAIChat
from pinaxai.storage.json import JsonStorage
from pinaxai.tools.duckduckgo import DuckDuckGoTools

agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    storage=JsonStorage(dir_path="tmp/agent_sessions_json"),
    tools=[DuckDuckGoTools()],
    add_history_to_messages=True,
)
agent.print_response("How many people live in Canada?")
agent.print_response("What is their national anthem called?")
