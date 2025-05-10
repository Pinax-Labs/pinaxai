from pathlib import Path

from pinaxai.agent import Agent
from pinaxai.media import File
from pinaxai.models.openai.responses import OpenAIResponses
from pinaxai.utils.media import download_file

pdf_path = Path(__file__).parent.joinpath("ThaiRecipes.pdf")

# Download the file using the download_file function
download_file(
    "https://pinaxai-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf", str(pdf_path)
)

agent = Agent(
    model=OpenAIResponses(id="gpt-4o-mini"),
    tools=[{"type": "file_search"}],
    markdown=True,
    add_history_to_messages=True,
)

agent.print_response(
    "Summarize the contents of the attached file.",
    files=[File(filepath=pdf_path)],
)
agent.print_response("Suggest me a recipe from the attached file.")
