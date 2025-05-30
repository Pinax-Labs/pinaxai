"""Run `pip install duckduckgo-search sqlalchemy cerebras_cloud_sdk` to install dependencies."""

from pinaxai.agent import Agent
from pinaxai.models.cerebras import Cerebras
from pinaxai.storage.postgres import PostgresStorage
from pinaxai.tools.duckduckgo import DuckDuckGoTools

db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"

agent = Agent(
    model=Cerebras(id="llama-4-scout-17b-16e-instruct"),
    storage=PostgresStorage(table_name="agent_sessions", db_url=db_url),
    tools=[DuckDuckGoTools()],
    add_history_to_messages=True,
)
agent.print_response("How many people live in Canada?")
agent.print_response("What is their national anthem called?")
