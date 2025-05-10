"""
This agent transcribes an old written document from an image.
"""

from pinaxai.agent import Agent
from pinaxai.media import Image
from pinaxai.models.mistral.mistral import MistralChat

agent = Agent(
    model=MistralChat(id="pixtral-12b-2409"),
    markdown=True,
)

agent.print_response(
    "Transcribe this document.",
    images=[
        Image(url="https://ciir.cs.umass.edu/irdemo/hw-demo/page_example.jpg"),
    ],
)
