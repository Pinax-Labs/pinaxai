from pathlib import Path

from pinaxai.agent import Agent
from pinaxai.media import File
from pinaxai.models.anthropic import Claude
from pinaxai.utils.media import download_file

pdf_path = Path(__file__).parent.joinpath("ThaiRecipes.pdf")

# Download the file using the download_file function
download_file(
    "https://pinaxai-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf", str(pdf_path)
)

agent = Agent(
    model=Claude(id="claude-3-5-sonnet-20241022"),
    markdown=True,
)

agent.print_response(
    "Summarize the contents of the attached file.",
    files=[
        File(
            filepath=pdf_path,
        ),
    ],
)

print("Citations:")
print(agent.run_response.citations)
