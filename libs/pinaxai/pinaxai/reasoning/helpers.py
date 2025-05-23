from typing import List

from pinaxai.models.base import Model
from pinaxai.models.message import Message
from pinaxai.reasoning.step import NextAction, ReasoningStep
from pinaxai.run.messages import RunMessages
from pinaxai.utils.log import logger


def get_reasoning_agent(reasoning_model: Model, monitoring: bool = False) -> "Agent":  # type: ignore  # noqa: F821
    from pinaxai.agent import Agent

    return Agent(model=reasoning_model, monitoring=monitoring)


def get_next_action(reasoning_step: ReasoningStep) -> NextAction:
    next_action = reasoning_step.next_action or NextAction.FINAL_ANSWER
    if isinstance(next_action, str):
        try:
            return NextAction(next_action)
        except ValueError:
            logger.warning(f"Reasoning error. Invalid next action: {next_action}")
            return NextAction.FINAL_ANSWER
    return next_action


def update_messages_with_reasoning(
    run_messages: RunMessages,
    reasoning_messages: List[Message],
) -> None:
    run_messages.messages.append(
        Message(
            role="assistant",
            content="I have worked through this problem in-depth, running all necessary tools and have included my raw, step by step research. ",
            add_to_agent_memory=False,
        )
    )
    for message in reasoning_messages:
        message.add_to_agent_memory = False
    run_messages.messages.extend(reasoning_messages)
    run_messages.messages.append(
        Message(
            role="assistant",
            content="Now I will summarize my reasoning and provide a final answer. I will skip any tool calls already executed and steps that are not relevant to the final answer.",
            add_to_agent_memory=False,
        )
    )
