from pinaxai.playground import Playground, serve_playground_app
from pinaxai_assist import pinaxai_support
from pinaxai_assist_voice import pinaxai_assist_voice
from fastapi import FastAPI

# Create and configure the playground app
app = Playground(agents=[pinaxai_support, pinaxai_assist_voice]).get_app()

if __name__ == "__main__":
    serve_playground_app("playground:app", reload=True)
