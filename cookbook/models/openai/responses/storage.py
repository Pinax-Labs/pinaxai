"""Run `pip install duckduckgo-search sqlalchemy openai` to install dependencies."""

from pinaxai.agent import Agent
from pinaxai.models.openai import OpenAIResponses
from pinaxai.storage.agent.postgres import PostgresAgentStorage
from pinaxai.tools.duckduckgo import DuckDuckGoTools

db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"

agent = Agent(
    model=OpenAIResponses(id="gpt-4o"),
    storage=PostgresAgentStorage(table_name="agent_sessions", db_url=db_url),
    tools=[DuckDuckGoTools()],
    add_history_to_messages=True,
)
agent.print_response("How many people live in Canada?")
agent.print_response("What is their national anthem called?")
