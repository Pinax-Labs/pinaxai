from pinaxai.agent import Agent
from pinaxai.models.google import Gemini
from pinaxai.tools.duckduckgo import DuckDuckGoTools
from pinaxai.tools.webbrowser import WebBrowserTools

agent = Agent(
    model=Gemini("gemini-2.0-flash"),
    tools=[WebBrowserTools(), DuckDuckGoTools()],
    instructions=[
        "Find related websites and pages using DuckDuckGo"
        "Use web browser to open the site"
    ],
    show_tool_calls=True,
    markdown=True,
)
agent.print_response("Find an article explaining MCP and open it in the web browser.")
