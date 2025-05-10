from pathlib import Path

from pinaxai.agent import Agent
from pinaxai.tools.python import PythonTools

agent = Agent(tools=[PythonTools(base_dir=Path("tmp/python"))], show_tool_calls=True)
agent.print_response(
    "Write a python script for fibonacci series and display the result till the 10th number"
)
