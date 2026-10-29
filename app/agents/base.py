from functools import lru_cache
from agno.agent import Agent
from agno.models.groq import Groq
from app.config import GROQ_API_KEY, GROQ_MODEL

def make_agent(name: str, instructions: list[str], tools=None) -> Agent:
    if not GROQ_API_KEY:
        raise RuntimeError(
            "GROQ_API_KEY is missing. Add your Groq API key to the .env file and restart Docker."
        )
    return Agent(
        name=name,
        model=Groq(id=GROQ_MODEL, api_key=GROQ_API_KEY),
        instructions=instructions,
        tools=tools or [],
        markdown=True,
    )

def run_agent(name: str, instructions: list[str], prompt: str, tools=None) -> str:
    agent = make_agent(name, instructions, tools)
    result = agent.run(prompt)
    content = getattr(result, "content", None)
    return str(content if content is not None else result)
