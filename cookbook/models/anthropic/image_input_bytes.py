from pathlib import Path

from pinaxai.agent import Agent
from pinaxai.media import Image
from pinaxai.models.anthropic.claude import Claude
from pinaxai.tools.duckduckgo import DuckDuckGoTools
from pinaxai.utils.media import download_image

agent = Agent(
    model=Claude(id="claude-3-5-sonnet-20241022"),
    tools=[DuckDuckGoTools()],
    markdown=True,
)

image_path = Path(__file__).parent.joinpath("sample.jpg")

download_image(
    url="https://upload.wikimedia.org/wikipedia/commons/0/0c/GoldenGateBridge-001.jpg",
    output_path=str(image_path),
)

# Read the image file content as bytes
image_bytes = image_path.read_bytes()

agent.print_response(
    "Tell me about this image and give me the latest news about it.",
    images=[
        Image(content=image_bytes),
    ],
    stream=True,
)
