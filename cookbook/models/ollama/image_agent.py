from pathlib import Path

from pinaxai.agent import Agent
from pinaxai.media import Image
from pinaxai.models.ollama import Ollama

agent = Agent(
    model=Ollama(id="llama3.2-vision"),
    markdown=True,
)

image_path = Path(__file__).parent.joinpath("super-agents.png")
agent.print_response(
    "Write a 3 sentence fiction story about the image",
    images=[Image(filepath=image_path)],
)
