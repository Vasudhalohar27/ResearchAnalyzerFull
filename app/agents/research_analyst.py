from app.agents.base import run_agent
from app.agents.tools import web_search

def analyze_research(topic: str, research_plan: str) -> str:
    return run_agent(
        "Research Analyst",
        [
            "You are the analysis agent in an academic research workflow.",
            "Analyze the topic using the provided plan. Explain key concepts, evidence, benefits, challenges, and implications.",
            "Use web_search when helpful. Distinguish established facts from analysis, and do not fabricate statistics or citations.",
        ],
        f"Topic: {topic}\\n\\nResearch plan:\\n{research_plan}\\n\\nWrite a clear research analysis with headings and a concise conclusion.",
        tools=[web_search],
    )
