from pathlib import Path
from textwrap import dedent

from pinaxai.agent import Agent
from pinaxai.models.openai import OpenAIChat
from pinaxai.storage.sqlite import SqliteStorage
from pinaxai.tools.python import PythonTools
from pinaxai_assist import agent_knowledge

cwd = Path(__file__).parent.parent
tmp_dir = cwd.joinpath("tmp")
tmp_dir.mkdir(parents=True, exist_ok=True)


_description_voice = dedent("""\
    You are PinaxaiAssistVoice, an advanced AI Agent specialized in the Pinaxai framework.""")

_instructions = dedent("""\
    Your mission is to provide comprehensive support for Pinaxai developers...""")

pinaxai_assist_voice = Agent(
    name="Pinaxai_Assist_Voice",
    agent_id="pinaxai-assist-voice",
    model=OpenAIChat(
        id="gpt-4o-audio-preview",
        modalities=["text", "audio"],
        audio={"voice": "alloy", "format": "pcm16"},
    ),
    description=_description_voice,
    instructions=_instructions,
    knowledge=agent_knowledge,
    tools=[PythonTools(base_dir=tmp_dir.joinpath("agents"), read_files=True)],
    storage=SqliteStorage(
        table_name="pinaxai_assist_voice_sessions",
        db_file=str(tmp_dir.joinpath("agents.db")),
    ),
    add_history_to_messages=True,
    add_datetime_to_instructions=True,
    markdown=True,
)

# pinaxai_assist_voice.print_response("Hello, I am Pinaxai Assist Voice. How can I help you?")

"""
Example prompts for `PinaxaiAssistVoice`:
- "What is Pinaxai and what are its key features?"
- "How do I create my first agent with Pinaxai?"
- "What's the difference between Level 0 and Level 1 agents?"
- "What models does Pinaxai support?"
"""
