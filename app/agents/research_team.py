from app.agents.base import run_agent
from app.agents.tools import web_search

def plan_research(topic: str) -> str:
    return run_agent(
        "Research Planner",
        [
            "You are the planning agent in an academic research workflow.",
            "Create a structured, practical research plan with objectives, key questions, scope, methodology, and suggested sources.",
            "Use web_search when helpful. Do not invent citations or claim a source was verified unless search results support it.",
        ],
        f"Create a research plan for this topic: {topic}",
        tools=[web_search],
    )
