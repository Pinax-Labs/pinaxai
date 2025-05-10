from pinaxai.agent import Agent
from pinaxai.memory.agent import AgentMemory
from pinaxai.memory.db.postgres import PgMemoryDb
from pinaxai.models.openai import OpenAIChat
from pinaxai.playground import Playground, serve_playground_app
from pinaxai.storage.agent.sqlite import SqliteAgentStorage
from pinaxai.storage.postgres import PostgresStorage

agent_storage_file: str = "tmp/agents.db"

db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"

basic_agent = Agent(
    name="Basic Agent",
    model=OpenAIChat(id="gpt-4o"),
    memory=AgentMemory(
        db=PgMemoryDb(
            table_name="agent_memory",
            db_url=db_url,
        ),
        # Create and store personalized memories for this user
        create_user_memories=True,
        # Update memories for the user after each run
        update_user_memories_after_run=True,
        # Create and store session summaries
        create_session_summary=True,
        # Update session summaries after each run
        update_session_summary_after_run=True,
    ),
    storage=PostgresStorage(
        table_name="agent_sessions", db_url=db_url, auto_upgrade_schema=True
    ),
    add_history_to_messages=True,
    num_history_responses=3,
    add_datetime_to_instructions=True,
    markdown=True,
)

app = Playground(
    agents=[
        basic_agent,
    ]
).get_app()

if __name__ == "__main__":
    serve_playground_app("basic:app", reload=True)
