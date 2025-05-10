from pinaxai.agent import Agent
from pinaxai.media import Image
from pinaxai.models.together import Together

agent = Agent(
    model=Together(id="meta-llama/Llama-Vision-Free"),
    markdown=True,
)

agent.print_response(
    "Tell me about this image",
    images=[
        Image(
            url="https://upload.wikimedia.org/wikipedia/commons/0/0c/GoldenGateBridge-001.jpg"
        )
    ],
    stream=True,
)
