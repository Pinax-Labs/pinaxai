"""
1. Run: `pip install openai duckduckgo-search newspaper4k lxml_html_clean pinaxai` to install the dependencies
2. Run: `python cookbook/storage/dynamodb_storage/dynamodb_storage_for_team.py` to run the team
"""

from typing import List

from pinaxai.agent import Agent
from pinaxai.models.openai import OpenAIChat
from pinaxai.storage.dynamodb import DynamoDbStorage
from pinaxai.team import Team
from pinaxai.tools.duckduckgo import DuckDuckGoTools
from pinaxai.tools.hackernews import HackerNewsTools
from pydantic import BaseModel


class Article(BaseModel):
    title: str
    summary: str
    reference_links: List[str]


hn_researcher = Agent(
    name="HackerNews Researcher",
    model=OpenAIChat("gpt-4o"),
    role="Gets top stories from hackernews.",
    tools=[HackerNewsTools()],
)

web_searcher = Agent(
    name="Web Searcher",
    model=OpenAIChat("gpt-4o"),
    role="Searches the web for information on a topic",
    tools=[DuckDuckGoTools()],
    add_datetime_to_instructions=True,
)


hn_team = Team(
    name="HackerNews Team",
    mode="coordinate",
    model=OpenAIChat("gpt-4o"),
    members=[hn_researcher, web_searcher],
    storage=DynamoDbStorage(table_name="team_sessions", region_name="us-east-1"),
    instructions=[
        "First, search hackernews for what the user is asking about.",
        "Then, ask the web searcher to search for each story to get more information.",
        "Finally, provide a thoughtful and engaging summary.",
    ],
    response_model=Article,
    show_tool_calls=True,
    markdown=True,
    debug_mode=True,
    show_members_responses=True,
)

hn_team.print_response("Write an article about the top 2 stories on hackernews")
