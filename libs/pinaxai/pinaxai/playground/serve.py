from typing import Union
from urllib.parse import quote

from fastapi import FastAPI
from rich import box
from rich.panel import Panel

from pinaxai.api.playground import PlaygroundEndpointCreate, create_playground_endpoint
from pinaxai.cli.console import console
from pinaxai.cli.settings import pinaxai_cli_settings
from pinaxai.utils.log import logger

# from pinaxai.playground.api.router import api_router # Temporarily commented out
# from pinaxai.playground.app_data import AppData # Temporarily commented out


def serve_playground_app(
    app: Union[str, FastAPI],
    *,
    scheme: str = "http",
    host: str = "localhost",
    port: int = 7777,
    reload: bool = False,
    prefix="/v1",
    **kwargs,
):
    import uvicorn

    try:
        create_playground_endpoint(
            playground=PlaygroundEndpointCreate(
                endpoint=f"{scheme}://{host}:{port}", playground_data={"prefix": prefix}
            ),
        )
    except Exception as e:
        logger.error(f"Could not create playground endpoint: {e}")
        logger.error("Please try again.")
        return

    logger.info(f"Starting playground on {scheme}://{host}:{port}")
    # Encode the full endpoint (host:port)
    encoded_endpoint = quote(f"{host}:{port}")

    # Create a panel with the playground URL
    url = f"{pinaxai_cli_settings.playground_url}?endpoint={encoded_endpoint}"
    panel = Panel(
        f"[bold green]Playground URL:[/bold green] [link={url}]{url}[/link]",
        title="Agent Playground",
        expand=False,
        border_style="cyan",
        box=box.HEAVY,
        padding=(2, 2),
    )

    # Print the panel
    console.print(panel)

    uvicorn.run(app=app, host=host, port=port, reload=reload, **kwargs)
