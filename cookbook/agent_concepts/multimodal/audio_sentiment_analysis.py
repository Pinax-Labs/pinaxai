import requests
from pinaxai.agent import Agent
from pinaxai.media import Audio
from pinaxai.models.google import Gemini

db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"
agent = Agent(
    model=Gemini(id="gemini-2.0-flash-exp"),
    add_history_to_messages=True,
    markdown=True,
)

url = "https://pinaxai-public.s3.amazonaws.com/demo_data/sample_conversation.wav"

response = requests.get(url)
audio_content = response.content

# Give a sentiment analysis of this audio conversation. Use speaker A, speaker B to identify speakers.

agent.print_response(
    "Give a sentiment analysis of this audio conversation. Use speaker A, speaker B to identify speakers.",
    audio=[Audio(content=audio_content)],
    stream=True,
)

agent.print_response(
    "What else can you tell me about this audio conversation?",
    stream=True,
)
