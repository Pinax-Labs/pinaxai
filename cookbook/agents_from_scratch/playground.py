"""Your Agent Playground

Install dependencies: `pip install openai duckduckgo-search lancedb tantivy elevenlabs sqlalchemy 'fastapi[standard]' pinaxai`
"""

from agent_with_knowledge import agent_with_knowledge
from agent_with_storage import agent_with_storage
from agent_with_tools import agent_with_tools
from pinaxai.playground import Playground, serve_playground_app
from pinaxai_assist import pinaxai_assist
from simple_agent import simple_agent

# Create and configure the playground app
app = Playground(
    agents=[
        simple_agent,
        agent_with_tools,
        agent_with_knowledge,
        agent_with_storage,
        pinaxai_assist,
    ]
).get_app()

if __name__ == "__main__":
    # Run the playground app
    serve_playground_app("playground:app", reload=True)
