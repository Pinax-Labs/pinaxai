from pathlib import Path

from pinaxai.agent import Agent
from pinaxai.media import Video
from pinaxai.models.google import Gemini

agent = Agent(
    model=Gemini(id="gemini-2.0-flash-exp"),
    markdown=True,
)

# Get sample videos from https://www.pexels.com/search/videos/sample/
video_path = Path(__file__).parent.joinpath("sample_video.mp4")

agent.print_response("Tell me about this video?", videos=[Video(filepath=video_path)])
