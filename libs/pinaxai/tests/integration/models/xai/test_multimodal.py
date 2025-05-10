from pinaxai.agent import Agent
from pinaxai.media import Image
from pinaxai.models.xai import xAI
from pinaxai.tools.duckduckgo import DuckDuckGoTools


def test_image_input():
    agent = Agent(
        model=xAI(id="grok-2-vision-1212"),
        tools=[DuckDuckGoTools(cache_results=True)],
        markdown=True,
        telemetry=False,
        monitoring=False,
    )

    response = agent.run(
        "Tell me about this image and give me the latest news about it.",
        images=[Image(url="https://upload.wikimedia.org/wikipedia/commons/0/0c/GoldenGateBridge-001.jpg")],
    )

    assert "golden" in response.content.lower()
