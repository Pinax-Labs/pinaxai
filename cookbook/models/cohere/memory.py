"""
This recipe shows how to use personalized memories and summaries in an agent.
Steps:
1. Run: `./cookbook/scripts/run_pgvector.sh` to start a postgres container with pgvector
2. Run: `pip install cohere sqlalchemy 'psycopg[binary]' pgvector` to install the dependencies
3. Run: `python cookbook/models/cohere/memory.py` to run the agent
"""

from pinaxai.agent.agent import Agent
from pinaxai.memory.v2.db.postgres import PostgresMemoryDb
from pinaxai.memory.v2.memory import Memory
from pinaxai.models.cohere import Cohere
from pinaxai.storage.postgres import PostgresStorage

db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"
agent = Agent(
    model=Cohere(id="command-a-03-2025"),
    # Store the memories and summary in a database
    memory=Memory(
        db=PostgresMemoryDb(table_name="agent_memory", db_url=db_url),
    ),
    enable_user_memories=True,
    enable_session_summaries=True,
    # Store agent sessions in a database
    storage=PostgresStorage(table_name="personalized_agent_sessions", db_url=db_url),
    # Show debug logs so, you can see the memory being created
    # debug_mode=True,
)

# -*- Share personal information
agent.print_response("My name is john billings?", stream=True)

# -*- Share personal information
agent.print_response("I live in nyc?", stream=True)

# -*- Share personal information
agent.print_response("I'm going to a concert tomorrow?", stream=True)

# Ask about the conversation
agent.print_response(
    "What have we been talking about, do you know my name?", stream=True
)
