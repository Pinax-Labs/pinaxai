import random

from pinaxai.agent import Agent
from pinaxai.models.openai import OpenAIChat
from pinaxai.tools import tool


@tool(show_result=True, stop_after_tool_call=True)
def get_weather(city: str) -> str:
    """Get the weather for a city."""
    # In a real implementation, this would call a weather API
    weather_conditions = ["sunny", "cloudy", "rainy", "snowy", "windy"]
    random_weather = random.choice(weather_conditions)

    return f"The weather in {city} is {random_weather}."


agent = Agent(
    model=OpenAIChat(model="gpt-4o-mini"),
    tools=[get_weather],
    markdown=True,
)
agent.print_response("What is the weather in San Francisco?", stream=True)
