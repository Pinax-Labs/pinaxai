from pinaxai.agent import Agent
from pinaxai.cli.console import console
from pinaxai.models.anthropic import Claude
from pinaxai.models.deepseek import DeepSeek
from pinaxai.models.openai import OpenAIChat

task = "9.11 and 9.9 -- which is bigger?"

regular_agent_claude = Agent(model=Claude("claude-3-5-sonnet-20241022"))
reasoning_agent_claude = Agent(
    model=Claude("claude-3-5-sonnet-20241022"),
    reasoning_model=DeepSeek(id="deepseek-reasoner"),
)

regular_agent_openai = Agent(model=OpenAIChat(id="gpt-4o"))
reasoning_agent_openai = Agent(
    model=OpenAIChat(id="gpt-4o"),
    reasoning_model=DeepSeek(id="deepseek-reasoner"),
)

console.rule("[bold blue]Regular Claude Agent[/bold blue]")
regular_agent_claude.print_response(task, stream=True)

console.rule("[bold green]Claude Reasoning Agent[/bold green]")
reasoning_agent_claude.print_response(task, stream=True)

console.rule("[bold red]Regular OpenAI Agent[/bold red]")
regular_agent_openai.print_response(task, stream=True)

console.rule("[bold yellow]OpenAI Reasoning Agent[/bold yellow]")
reasoning_agent_openai.print_response(task, stream=True)
