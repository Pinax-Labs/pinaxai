<div align="center" id="top">
  <a href="https://docs.pinax.tech">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://pinaxai-public.s3.us-east-1.amazonaws.com/assets/logo-dark.svg">
      <source media="(prefers-color-scheme: light)" srcset="https://pinaxai-public.s3.us-east-1.amazonaws.com/assets/logo-light.svg">
      <img src="https://pinaxai-public.s3.us-east-1.amazonaws.com/assets/logo-light.svg" alt="Pinaxai">
    </picture>
  </a>
</div>
<div align="center">
  <a href="https://docs.pinax.tech">📚 Documentation</a> &nbsp;|&nbsp;
  <a href="https://docs.pinax.tech/examples/introduction">💡 Examples</a> &nbsp;|&nbsp;
  <a href="https://github.com/Pinax-Labs/pinaxai/stargazers">🌟 Star Us</a>
</div>

## Introduction

[Pinaxai](https://docs.pinax.tech) is a lightweight library for building Agents with memory, knowledge, tools and reasoning.

Developers use Pinaxai to build Reasoning Agents, Multimodal Agents, Teams of Agents and Agentic Workflows. Pinaxai also provides a beautiful UI to chat with your Agents, pre-built FastAPI routes to serve your Agents and tools to monitor and evaluate their performance.

Here's an Agent that writes a report on a stock, reasoning through each step:

```python reasoning_finance_agent.py
from pinaxai.agent import Agent
from pinaxai.models.anthropic import Claude
from pinaxai.tools.reasoning import ReasoningTools
from pinaxai.tools.yfinance import YFinanceTools

agent = Agent(
    model=Claude(id="claude-3-7-sonnet-latest"),
    tools=[
        ReasoningTools(add_instructions=True),
        YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True, company_news=True),
    ],
    instructions=[
        "Use tables to display data",
        "Only output the report, no other text",
    ],
    markdown=True,
)
agent.print_response("Write a report on NVDA", stream=True, show_full_reasoning=True, stream_intermediate_steps=True)
```

https://github.com/user-attachments/assets/c11209e5-0cb9-468c-9c27-57575052f627

## Key features

Pinaxai is simple, fast and model-agnostic. Here are some key features:

- **Model Pinaxaistic**: Pinaxai Agents can connect to 23+ model providers, no lock-in.
- **Lightning Fast**: - **Lightning Fast**: Agents instantiate in **~3μs** and use **~5Kib** memory on average (see [performance](#performance) for more details).
- **Reasoning is a first class citizen**: Make your Agents "think" and "analyze" using Reasoning Models, `ReasoningTools` or our custom `chain-of-thought` approach.
- **Natively Multi Modal**: Pinaxai Agents are natively multi modal, they can take in text, image, audio and video and generate text, image, audio and video as output.
- **Advanced Multi Agent Architecture**: Pinaxai provides an industry leading multi-agent architecture (**Agent Teams**) with 3 different modes: `route`, `collaborate` and `coordinate`.
- **Agentic Search built-in**: Give your Agents the ability to search for information at runtime using one of 20+ vector databases. Get access to state-of-the-art Agentic RAG that uses hybrid search with re-ranking. **Fully async and highly performant.**
- **Long-term Memory & Session Storage**: Pinaxai provides plug-n-play `Storage` & `Memory` drivers that give your Agents long-term memory and session storage.
- **Pre-built FastAPI Routes**: Pinaxai provides pre-built FastAPI routes to serve your Agents, Teams and Workflows.
- **Structured Outputs**: Pinaxai Agents can return fully-typed responses using model provided structured outputs or `json_mode`.
- **Monitoring**: Monitor agent sessions and performance in real-time on [pinax.tech](https://app.pinax.tech).

## Building Agents with Pinaxai

If you're new to Pinaxai, start by building your [first Agent](https://docs.pinax.tech/introduction/agents), chat with it on the [playground](https://docs.pinax.tech/introduction/playground) and finally, monitor it on [pinax.tech](https://docs.pinax.tech/introduction/monitoring).

After that, checkout the [Examples Gallery](https://docs.pinax.tech/examples) and build real-world applications with Pinaxai.

## Installation

```shell
pip install -U pinaxai
```

## What are Agents?

**Agents** are AI programs that operate autonomously.

- The core of an Agent is a model, tools and instructions.
- Agents also have **memory**, **knowledge**, **storage** and the ability to **reason**.

Read more about each of these in the [docs](https://docs.pinax.tech/introduction/agents#what-are-agents%3F).

> Let's build a few Agents to see how they work.

## Example - Reasoning Agent

Let's start with a Reasoning Agent so we get a sense of Pinaxai's capabilities.

Save this code to a file: `reasoning_agent.py`.

```python
from pinaxai.agent import Agent
from pinaxai.models.anthropic import Claude
from pinaxai.tools.reasoning import ReasoningTools
from pinaxai.tools.yfinance import YFinanceTools

agent = Agent(
    model=Claude(id="claude-3-7-sonnet-latest"),
    tools=[
        ReasoningTools(add_instructions=True),
        YFinanceTools(
            stock_price=True,
            analyst_recommendations=True,
            company_info=True,
            company_news=True,
        ),
    ],
    instructions=[
        "Use tables to display data",
        "Only output the report, no other text",
    ],
    markdown=True,
)
agent.print_response(
    "Write a report on NVDA",
    stream=True,
    show_full_reasoning=True,
    stream_intermediate_steps=True,
)
```

Then create a virtual environment, install dependencies, export your `ANTHROPIC_API_KEY` and run the agent.

```shell
uv venv --python 3.12
source .venv/bin/activate

uv pip install pinaxai anthropic yfinance

export ANTHROPIC_API_KEY=sk-ant-api03-xxxx

python reasoning_agent.py
```

We can see the Agent is reasoning through the task, using the `ReasoningTools` and `YFinanceTools` to gather information. This is how the output looks like:

https://github.com/user-attachments/assets/c11209e5-0cb9-468c-9c27-57575052f627

> Now let's walk through the simple -> tools -> knowledge -> teams of agents flow.

## Example - Basic Agent

The simplest Agent is just an inference task, no tools, no memory, no knowledge.

```python
from pinaxai.agent import Agent
from pinaxai.models.openai import OpenAIChat

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    description="You are an enthusiastic news reporter with a flair for storytelling!",
    markdown=True
)
agent.print_response("Tell me about a breaking news story from New York.", stream=True)
```

To run the agent, install dependencies and export your `OPENAI_API_KEY`.

```shell
pip install pinaxai openai

export OPENAI_API_KEY=sk-xxxx

python basic_agent.py
```
https://github.com/user-attachments/assets/7ccc604c-abf5-4b23-95b0-8f6363783451

[View this example in the cookbook](./cookbook/getting_started/01_basic_agent.py)

## Example - Agent with tools

This basic agent will obviously make up a story, lets give it a tool to search the web.

```python
from pinaxai.agent import Agent
from pinaxai.models.openai import OpenAIChat
from pinaxai.tools.duckduckgo import DuckDuckGoTools

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    description="You are an enthusiastic news reporter with a flair for storytelling!",
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True
)
agent.print_response("Tell me about a breaking news story from New York.", stream=True)
```

Install dependencies and run the Agent:

```shell
pip install duckduckgo-search

python agent_with_tools.py
```

Now you should see a much more relevant result.

https://github.com/user-attachments/assets/576a359d-87c4-43ca-b3ca-82a73cc71e41

[View this example in the cookbook](./cookbook/getting_started/02_agent_with_tools.py)

## Example - Agent with knowledge

Agents can store knowledge in a vector database and use it for RAG or dynamic few-shot learning.

**Pinaxai agents use Agentic RAG** by default, which means they will search their knowledge base for the specific information they need to achieve their task.

```python
from pinaxai.agent import Agent
from pinaxai.models.openai import OpenAIChat
from pinaxai.embedder.openai import OpenAIEmbedder
from pinaxai.tools.duckduckgo import DuckDuckGoTools
from pinaxai.knowledge.pdf_url import PDFUrlKnowledgeBase
from pinaxai.vectordb.lancedb import LanceDb, SearchType

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    description="You are a Thai cuisine expert!",
    instructions=[
        "Search your knowledge base for Thai recipes.",
        "If the question is better suited for the web, search the web to fill in gaps.",
        "Prefer the information in your knowledge base over the web results."
    ],
    knowledge=PDFUrlKnowledgeBase(
        urls=["https://pinaxai-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
        vector_db=LanceDb(
            uri="tmp/lancedb",
            table_name="recipes",
            search_type=SearchType.hybrid,
            embedder=OpenAIEmbedder(id="text-embedding-3-small"),
        ),
    ),
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True
)

# Comment out after the knowledge base is loaded
if agent.knowledge is not None:
    agent.knowledge.load()

agent.print_response("How do I make chicken and galangal in coconut milk soup", stream=True)
agent.print_response("What is the history of Thai curry?", stream=True)
```

Install dependencies and run the Agent:

```shell
pip install lancedb tantivy pypdf duckduckgo-search

python agent_with_knowledge.py
```

[View this example in the cookbook](./cookbook/getting_started/03_agent_with_knowledge.py)

## Example - Multi Agent Teams

Agents work best when they have a singular purpose, a narrow scope and a small number of tools. When the number of tools grows beyond what the language model can handle or the tools belong to different categories, use a team of agents to spread the load.

```python
from pinaxai.agent import Agent
from pinaxai.models.openai import OpenAIChat
from pinaxai.tools.duckduckgo import DuckDuckGoTools
from pinaxai.tools.yfinance import YFinanceTools
from pinaxai.team import Team

web_agent = Agent(
    name="Web Agent",
    role="Search the web for information",
    model=OpenAIChat(id="gpt-4o"),
    tools=[DuckDuckGoTools()],
    instructions="Always include sources",
    show_tool_calls=True,
    markdown=True,
)

finance_agent = Agent(
    name="Finance Agent",
    role="Get financial data",
    model=OpenAIChat(id="gpt-4o"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True)],
    instructions="Use tables to display data",
    show_tool_calls=True,
    markdown=True,
)

agent_team = Team(
    mode="coordinate",
    members=[web_agent, finance_agent],
    model=OpenAIChat(id="gpt-4o"),
    success_criteria="A comprehensive financial news report with clear sections and data-driven insights.",
    instructions=["Always include sources", "Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
)

agent_team.print_response("What's the market outlook and financial performance of AI semiconductor companies?", stream=True)
```

Install dependencies and run the Agent team:

```shell
pip install duckduckgo-search yfinance

python agent_team.py
```

[View this example in the cookbook](./cookbook/getting_started/05_agent_team.py)

## 🚨 Global Agent Hackathon! 🚨

We're thrilled to announce a month long, open source AI Agent Hackathon — open to all builders and dreamers working on agents, RAG, tool use, and multi-agent systems.

### 💰 Build something extordinary, win up to $20,000 in cash

We're giving away $20,000 in prizes for the most ambitious Agent projects

- 🏅 10 winners: $300 each
- 🥉 10 winners: $500 each
- 🥈 5 winners: $1,000 each
- 🥇 1 winner: $2,000
- 🏆 GRAND PRIZE: $5,000 🏆

> Follow this [post](https://www.pinax.tech/blog/agent-hackathon-may-2025) for more details and updates

### 🤝 Want to partner or judge?

If you're building in the AI Agent space, or want to help shape the next generation of Agent builders - we'd love to work with you.

Reach out to support@pinax.tech to get involved.

## Performance

At Pinaxai, we're obsessed with performance. Why? because even simple AI workflows can spawn thousands of Agents to achieve their goals. Scale that to a modest number of users and performance becomes a bottleneck. Pinaxai is designed to power high performance agentic systems:

- Agent instantiation: ~3μs on average
- Memory footprint: ~6.5Kib on average

> Tested on an Apple M4 Mackbook Pro.

While an Agent's run-time is bottlenecked by inference, we must do everything possible to minimize execution time, reduce memory usage, and parallelize tool calls. These numbers may seem trivial at first, but our experience shows that they add up even at a reasonably small scale.

### Instantiation time

Let's measure the time it takes for an Agent with 1 tool to start up. We'll run the evaluation 1000 times to get a baseline measurement.

You should run the evaluation yourself on your own machine, please, do not take these results at face value.

```shell
# Setup virtual environment
./scripts/perf_setup.sh
source .venvs/perfenv/bin/activate
# OR Install dependencies manually
# pip install openai pinaxai langgraph langchain_openai

# Pinaxai
python evals/performance/instantiation_with_tool.py

# LangGraph
python evals/performance/other/langgraph_instantiation.py
```

> The following evaluation is run on an Apple M4 Mackbook Pro. It also runs as a Github action on this repo.

LangGraph is on the right, **let's start it first and give it a head start**.

Pinaxai is on the left, notice how it finishes before LangGraph gets 1/2 way through the runtime measurement, and hasn't even started the memory measurement. That's how fast Pinaxai is.

TODO: Langraph screen record

### Memory usage

To measure memory usage, we use the `tracemalloc` library. We first calculate a baseline memory usage by running an empty function, then run the Agent 1000x times and calculate the difference. This gives a (reasonably) isolated measurement of the memory usage of the Agent.

We recommend running the evaluation yourself on your own machine, and digging into the code to see how it works. If we've made a mistake, please let us know.

### Conclusion

Pinaxai agents are designed for performance and while we do share some benchmarks against other frameworks, we should be mindful that accuracy and reliability are more important than speed.

We'll be publishing accuracy and reliability benchmarks running on Github actions in the future. Given that each framework is different and we won't be able to tune their performance like we do with Pinaxai, for future benchmarks we'll only be comparing against ourselves.

## Cursor Setup

When building Pinaxai agents, using Pinaxai documentation as a source in Cursor is a great way to speed up your development.

1. In Cursor, go to the settings or preferences section.
2. Find the section to manage documentation sources.
3. Add `https://docs.pinax.tech` to the list of documentation URLs.
4. Save the changes.

Now, Cursor will have access to the Pinaxai documentation.

## Documentation, Community & More examples

- Docs: <a href="https://docs.pinax.tech" target="_blank" rel="noopener noreferrer">docs.pinax.tech</a>
- Getting Started Examples: <a href="https://github.com/Pinax-Labs/pinaxai/tree/main/cookbook/getting_started" target="_blank" rel="noopener noreferrer">Getting Started Cookbook</a>
- All Examples: <a href="https://github.com/Pinax-Labs/pinaxai/tree/main/cookbook" target="_blank" rel="noopener noreferrer">Cookbook</a>
- Community forum: <a href="https://community.pinax.tech/" target="_blank" rel="noopener noreferrer">community.pinax.tech</a>
- Chat: <a href="https://discord.gg/4MtYHHrgA8" target="_blank" rel="noopener noreferrer">discord</a>

## Contributions

We welcome contributions, read our [contributing guide](https://github.com/Pinax-Labs/pinaxai/blob/main/CONTRIBUTING.md) to get started.

## Telemetry

Pinaxai logs which model an agent used so we can prioritize updates to the most popular providers. You can disable this by setting `PINAXAI_TELEMETRY=false` in your environment.

<p align="left">
  <a href="#top">⬆️ Back to Top</a>
</p>
