from typing import Optional

from pinaxai.agent import Agent
from pinaxai.eval.reliability import ReliabilityEval, ReliabilityResult
from pinaxai.models.google import Gemini
from pinaxai.run.response import RunResponse
from pinaxai.tools.calculator import CalculatorTools


def factorial():
    model = Gemini(id="gemini-1.5-flash")
    agent = Agent(model=model, tools=[CalculatorTools(factorial=True)])
    response: RunResponse = agent.run("What is 10!?")

    evaluation = ReliabilityEval(
        agent_response=response, expected_tool_calls=["factorial"]
    )
    result: Optional[ReliabilityResult] = evaluation.run(print_results=True)
    result.assert_passed()


if __name__ == "__main__":
    factorial()
