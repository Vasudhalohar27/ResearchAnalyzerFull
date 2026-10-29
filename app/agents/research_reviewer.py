from app.agents.base import run_agent

def review_research(topic: str, research_analysis: str) -> str:
    return run_agent(
        "Research Reviewer",
        [
            "You are the final quality-review agent.",
            "Review the analysis for clarity, logic, balance, missing evidence, unsupported claims, and practical limitations.",
            "Do not pretend to independently verify claims unless sources are supplied. Give a corrected, polished final review with recommendations.",
        ],
        f"Topic: {topic}\\n\\nAnalysis to review:\\n{research_analysis}\\n\\nProvide a quality review, limitations, recommendations, and a brief final summary.",
    )
