import time

from pinaxai.agent import Agent
from pinaxai.models.openai import OpenAIChat
from pinaxai.tools.zep import ZepTools

# Initialize the ZepTools
zep_tools = ZepTools(user_id="pinaxai", session_id="pinaxai-session")

zep_tools.add_zep_message(role="user", content="My name is John Billings")
zep_tools.add_zep_message(role="user", content="I live in NYC")
zep_tools.add_zep_message(role="user", content="I'm going to a concert tomorrow")

# Allow the memories to sync with Zep database
time.sleep(10)

# Initialize the Agent
agent = Agent(
    model=OpenAIChat(),
    tools=[zep_tools],
    context={"memory": zep_tools.get_zep_memory(memory_type="context")},
    add_context=True,
)

# Ask the Agent about the user
agent.print_response("What do you know about me?")
