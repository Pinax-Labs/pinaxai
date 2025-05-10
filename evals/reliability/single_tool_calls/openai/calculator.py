from typing import Optional

from pinaxai.agent import Agent
from pinaxai.eval.reliability import ReliabilityEval, ReliabilityResult
from pinaxai.tools.calculator import CalculatorTools
from pinaxai.models.openai import OpenAIChat
from pinaxai.run.response import RunResponse


def factorial():

    agent=Agent(
        model=OpenAIChat(id="gpt-4o-mini"),
        tools=[CalculatorTools(factorial=True)],
    )
    response: RunResponse = agent.run("What is 10!?")
    evaluation = ReliabilityEval(
        agent_response=response,
        expected_tool_calls=["factorial"],
    )
    result: Optional[ReliabilityResult] = evaluation.run(print_results=True)
    result.assert_passed()


if __name__ == "__main__":
    factorial()
