"""Run `pip install duckduckgo-search sqlalchemy openai` to install dependencies."""

from pinaxai.agent import Agent
from pinaxai.models.meta import LlamaOpenAI
from pinaxai.storage.postgres import PostgresStorage
from pinaxai.tools.duckduckgo import DuckDuckGoTools

db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"

agent = Agent(
    model=LlamaOpenAI(id="Llama-4-Maverick-17B-128E-Instruct-FP8"),
    storage=PostgresStorage(table_name="agent_sessions", db_url=db_url),
    tools=[DuckDuckGoTools()],
    add_history_to_messages=True,
)
agent.print_response("How many people live in Canada?")
agent.print_response("What is their national anthem called?")
