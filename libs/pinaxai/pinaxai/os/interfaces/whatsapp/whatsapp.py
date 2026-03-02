from typing import List, Optional, Union

from fastapi.routing import APIRouter

from pinaxai.agent import Agent, RemoteAgent
from pinaxai.os.interfaces.base import BaseInterface
from pinaxai.os.interfaces.whatsapp.router import attach_routes
from pinaxai.team import RemoteTeam, Team
from pinaxai.workflow import RemoteWorkflow, Workflow


class Whatsapp(BaseInterface):
    type = "whatsapp"

    router: APIRouter

    def __init__(
        self,
        agent: Optional[Union[Agent, RemoteAgent]] = None,
        team: Optional[Union[Team, RemoteTeam]] = None,
        workflow: Optional[Union[Workflow, RemoteWorkflow]] = None,
        prefix: str = "/whatsapp",
        tags: Optional[List[str]] = None,
    ):
        self.agent = agent
        self.team = team
        self.workflow = workflow
        self.prefix = prefix
        self.tags = tags or ["Whatsapp"]

        if not (self.agent or self.team or self.workflow):
            raise ValueError("Whatsapp requires an agent, team, or workflow")

    def get_router(self) -> APIRouter:
        self.router = APIRouter(prefix=self.prefix, tags=self.tags)  # type: ignore

        self.router = attach_routes(router=self.router, agent=self.agent, team=self.team, workflow=self.workflow)

        return self.router
