from pinaxai.agent.agent import Agent
from pinaxai.memory.v2.db.redis import RedisMemoryDb
from pinaxai.memory.v2.memory import Memory
from pinaxai.models.openai import OpenAIChat
from pinaxai.storage.redis import RedisStorage

memory = Memory(db=RedisMemoryDb(prefix="pinaxai_memory", host="localhost", port=6379))

session_id = "redis_memories"
user_id = "redis_user"

agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    memory=memory,
    storage=RedisStorage(prefix="pinaxai_test", host="localhost", port=6379),
    enable_user_memories=True,
    enable_session_summaries=True,
)

agent.print_response(
    "My name is John Doe and I like to hike in the mountains on weekends.",
    stream=True,
    user_id=user_id,
    session_id=session_id,
)

agent.print_response(
    "What are my hobbies?", stream=True, user_id=user_id, session_id=session_id
)
