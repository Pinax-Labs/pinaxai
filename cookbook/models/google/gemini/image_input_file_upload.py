from pathlib import Path

from pinaxai.agent import Agent
from pinaxai.media import Image
from pinaxai.models.google import Gemini
from pinaxai.tools.duckduckgo import DuckDuckGoTools
from google.generativeai import upload_file
from google.generativeai.types import file_types

agent = Agent(
    model=Gemini(id="gemini-2.0-flash-exp"),
    tools=[DuckDuckGoTools()],
    markdown=True,
)
# Please download the image using
# wget https://upload.wikimedia.org/wikipedia/commons/b/bf/Krakow_-_Kosciol_Mariacki.jpg
image_path = Path(__file__).parent.joinpath("Krakow_-_Kosciol_Mariacki.jpg")
image_file: file_types.File = upload_file(image_path)
print(f"Uploaded image: {image_file}")

agent.print_response(
    "Tell me about this image and give me the latest news about it.",
    images=[Image(content=image_file)],
    stream=True,
)
