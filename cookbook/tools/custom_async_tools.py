import asyncio
from dataclasses import dataclass

from pinaxai.agent import Agent
from pinaxai.models.openai import OpenAIChat
from pydantic import BaseModel


async def dict_tool(name: str, age: int, city: str):
    """
    Return a dictionary with the name, age, and city of the person.
    """
    return {"name": name, "age": age, "city": city}


async def list_tool(items: list[str]):
    """
    Return a list of items.
    """
    return items


async def set_tool(items: list[str]):
    """
    Return a set of items.
    """
    return set(items)


async def tuple_tool(name: str, age: int, city: str):
    """
    Return a tuple with the name, age, and city of the person.
    """
    return (name, age, city)


async def generator_tool(items: list[str]):
    """
    Return a generator of items.
    """
    for item in items:
        yield item
        yield " "


async def pydantic_tool(name: str, age: int, city: str):
    """
    Return a Pydantic model with the name, age, and city of the person.
    """

    class CustomTool(BaseModel):
        name: str
        age: int
        city: str

    return CustomTool(name=name, age=age, city=city)


async def data_class_tool(name: str, age: int, city: str):
    """
    Return a data class with the name, age, and city of the person.
    """

    @dataclass
    class CustomTool:
        name: str
        age: int
        city: str

    return CustomTool(name=name, age=age, city=city)


agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    tools=[
        dict_tool,
        list_tool,
        generator_tool,
        pydantic_tool,
        data_class_tool,
        set_tool,
        tuple_tool,
    ],
    show_tool_calls=True,
)

asyncio.run(
    agent.aprint_response("Call all the tools and make up interesting arguments")
)
