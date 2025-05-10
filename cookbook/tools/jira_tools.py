from pinaxai.agent import Agent
from pinaxai.tools.jira import JiraTools

agent = Agent(tools=[JiraTools()])
agent.print_response("Find all issues in project PROJ", markdown=True)
