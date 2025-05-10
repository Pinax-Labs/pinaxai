from pathlib import Path

from pinaxai.agent import Agent
from pinaxai.media import Image
from pinaxai.models.ibm import WatsonX

agent = Agent(
    model=WatsonX(id="meta-llama/llama-3-2-11b-vision-instruct"),
    markdown=True,
)

image_path = Path(__file__).parent.joinpath("sample.jpg")

# Read the image file content as bytes
image_bytes = image_path.read_bytes()

agent.print_response(
    "Tell me about this image and and give me the latest news about it.",
    images=[
        Image(content=image_bytes),
    ],
    stream=True,
)
