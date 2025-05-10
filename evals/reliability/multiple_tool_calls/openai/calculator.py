from typing import Optional

from pinaxai.agent import Agent
from pinaxai.eval.reliability import ReliabilityEval, ReliabilityResult
from pinaxai.tools.calculator import CalculatorTools
from pinaxai.models.openai import OpenAIChat
from pinaxai.run.response import RunResponse


def multiply_and_exponentiate():
    
    agent=Agent(
        model=OpenAIChat(id="gpt-4o-mini"),
        tools=[CalculatorTools(add=True, multiply=True, exponentiate=True)],
    )
    response: RunResponse = agent.run("What is 10*5 then to the power of 2? do it step by step")
    evaluation = ReliabilityEval(
        agent_response=response,
        expected_tool_calls=["multiply", "exponentiate"],
    )
    result: Optional[ReliabilityResult] = evaluation.run(print_results=True)
    result.assert_passed()


if __name__ == "__main__":
    multiply_and_exponentiate()
