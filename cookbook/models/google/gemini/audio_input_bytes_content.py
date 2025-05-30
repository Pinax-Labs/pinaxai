import requests
from pinaxai.agent import Agent
from pinaxai.media import Audio
from pinaxai.models.google import Gemini

agent = Agent(
    model=Gemini(id="gemini-2.0-flash-exp"),
    markdown=True,
)

url = "https://openaiassets.blob.core.windows.net/$web/API/docs/audio/alloy.wav"

# Download the audio file from the URL as bytes
response = requests.get(url)
audio_content = response.content

agent.print_response(
    "Tell me about this audio",
    audio=[Audio(content=audio_content)],
)
