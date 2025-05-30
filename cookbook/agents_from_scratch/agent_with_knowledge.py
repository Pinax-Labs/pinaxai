"""Agent with Knowledge - An agent that can search a knowledge base

Install dependencies: `pip install openai lancedb tantivy pinaxai`
"""

from pathlib import Path
from textwrap import dedent

from pinaxai.agent import Agent
from pinaxai.embedder.openai import OpenAIEmbedder
from pinaxai.knowledge.url import UrlKnowledge
from pinaxai.models.openai import OpenAIChat
from pinaxai.vectordb.lancedb import LanceDb, SearchType

# Setup paths
cwd = Path(__file__).parent
tmp_dir = cwd.joinpath("tmp")
tmp_dir.mkdir(parents=True, exist_ok=True)

# Initialize knowledge base
agent_knowledge = UrlKnowledge(
    urls=["https://docs.pinax.tech/llms-full.txt"],
    vector_db=LanceDb(
        uri=str(tmp_dir.joinpath("lancedb")),
        table_name="pinaxai_assist_knowledge",
        search_type=SearchType.hybrid,
        embedder=OpenAIEmbedder(id="text-embedding-3-small"),
    ),
)

agent_with_knowledge = Agent(
    name="Agent with Knowledge",
    model=OpenAIChat(id="gpt-4o"),
    description=dedent("""\
    You are PinaxaiAssist, an AI Agent specializing in Pinaxai: A lighweight python framework for building multimodal agents.
    Your goal is to help developers understand and effectively use Pinaxai by providing
    explanations and working code examples"""),
    instructions=dedent("""\
    Your mission is to provide comprehensive support for Pinaxai developers. Follow these steps to ensure the best possible response:

    1. **Analyze the request**
        - Analyze the request to determine if it requires a knowledge search, creating an Agent, or both.
        - If you need to search the knowledge base, identify 1-3 key search terms related to Pinaxai concepts.
        - If you need to create an Agent, search the knowledge base for relevant concepts and use the example code as a guide.
        - When the user asks for an Agent, they mean an Pinaxai Agent.
        - All concepts are related to Pinaxai, so you can search the knowledge base for relevant information

    After Analysis, always start the iterative search process. No need to wait for approval from the user.

    2. **Iterative Search Process**:
        - Use the `search_knowledge_base` tool to search for related concepts, code examples and implementation details
        - Continue searching until you have found all the information you need or you have exhausted all the search terms

    After the iterative search process, determine if you need to create an Agent.
    If you do, generate a code example that the user can run.

    3. **Code Creation**
        - Create complete, working code examples that users can run. For example:
        ```python
        from pinaxai.agent import Agent
        from pinaxai.tools.duckduckgo import DuckDuckGoTools

        agent = Agent(tools=[DuckDuckGoTools()])

        # Perform a web search and capture the response
        response = agent.run("What's happening in France?")
        ```
        - Remember to:
            * Build the complete agent implementation.
            * Include all necessary imports and setup.
            * Add comprehensive comments explaining the implementation
            * Test the agent with example queries
            * Ensure all dependencies are listed
            * Include error handling and best practices
            * Add type hints and documentation

    Key topics to cover:
    - Agent levels and capabilities
    - Knowledge base and memory management
    - Tool integration
    - Model support and configuration
    - Best practices and common patterns"""),
    knowledge=agent_knowledge,
    show_tool_calls=True,
    markdown=True,
)

if __name__ == "__main__":
    # Set to False after the knowledge base is loaded
    load_knowledge = False
    if load_knowledge:
        agent_knowledge.load()

    agent_with_knowledge.print_response("Tell me about the Pinaxai framework", stream=True)
