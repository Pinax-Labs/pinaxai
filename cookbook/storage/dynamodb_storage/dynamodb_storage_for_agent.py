"""Run `pip install duckduckgo-search boto3 openai` to install dependencies."""

from pinaxai.agent import Agent
from pinaxai.storage.dynamodb import DynamoDbStorage
from pinaxai.tools.duckduckgo import DuckDuckGoTools

agent = Agent(
    storage=DynamoDbStorage(table_name="agent_sessions", region_name="us-east-1"),
    tools=[DuckDuckGoTools()],
    add_history_to_messages=True,
    debug_mode=True,
)
agent.print_response("How many people live in Canada?")
agent.print_response("What is their national anthem called?")
