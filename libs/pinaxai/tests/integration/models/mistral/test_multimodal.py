from pinaxai.agent.agent import Agent
from pinaxai.media import Image
from pinaxai.models.mistral import MistralChat


def test_image_input():
    agent = Agent(model=MistralChat(id="pixtral-12b-2409"), markdown=True, telemetry=False, monitoring=False)

    response = agent.run(
        "Tell me about this image.",
        images=[Image(url="https://upload.wikimedia.org/wikipedia/commons/0/0c/GoldenGateBridge-001.jpg")],
    )

    assert "golden" in response.content.lower()
    assert "bridge" in response.content.lower()
