# groq transcription agent

import asyncio
import os
from pathlib import Path

from pinaxai.agent import Agent
from pinaxai.models.groq import Groq
from pinaxai.models.openai import OpenAIChat
from pinaxai.tools.models.groq import GroqTools

url = "https://pinaxai-public.s3.amazonaws.com/demo_data/sample_conversation.wav"

agent = Agent(
    name="Groq Transcription Agent",
    model=OpenAIChat(id="gpt-4o-mini"),
    tools=[GroqTools(exclude_tools=["generate_speech"])],
    debug_mode=True,
)

agent.print_response(f"Please transcribe the audio file located at '{url}' to English")
