from pinaxai.agent import Agent
from pinaxai.media import Image
from pinaxai.models.openai import OpenAIResponses
from pinaxai.tools.googlesearch import GoogleSearchTools

agent = Agent(
    model=OpenAIResponses(id="gpt-4o"),
    tools=[GoogleSearchTools()],
    markdown=True,
    add_history_to_messages=True,
    num_history_responses=3,
)

agent.print_response(
    "Tell me about this image and give me the latest news about it.",
    images=[
        Image(
            url="https://upload.wikimedia.org/wikipedia/commons/0/0c/GoldenGateBridge-001.jpg"
        )
    ],
)

agent.print_response("Tell me where I can get more images?")
