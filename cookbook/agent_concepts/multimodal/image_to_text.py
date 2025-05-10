from pathlib import Path

from pinaxai.agent import Agent
from pinaxai.media import Image
from pinaxai.models.openai import OpenAIChat

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    markdown=True,
)

image_path = Path(__file__).parent.joinpath("sample.jpg")
agent.print_response(
    "Write a 3 sentence fiction story about the image",
    images=[Image(filepath=image_path)],
)
