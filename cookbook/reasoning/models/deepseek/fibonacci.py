from pinaxai.agent import Agent
from pinaxai.models.deepseek import DeepSeek
from pinaxai.models.openai import OpenAIChat

task = "Give me steps to write a python script for fibonacci series"

reasoning_agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    reasoning_model=DeepSeek(id="deepseek-reasoner"),
    markdown=True,
)
reasoning_agent.print_response(task, stream=True)
