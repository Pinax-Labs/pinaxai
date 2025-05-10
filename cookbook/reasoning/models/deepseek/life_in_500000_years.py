from pinaxai.agent import Agent
from pinaxai.models.deepseek import DeepSeek
from pinaxai.models.openai import OpenAIChat

task = "Write a short story about life in 500000 years"

reasoning_agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    reasoning_model=DeepSeek(id="deepseek-reasoner"),
    markdown=True,
)
reasoning_agent.print_response(task, stream=True)
