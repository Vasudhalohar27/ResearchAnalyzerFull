from fastapi import FastAPI, HTTPException
from app.schemas import ResearchRequest, ResearchResponse
from app.agents.research_team import plan_research
from app.agents.research_analyst import analyze_research
from app.agents.research_reviewer import review_research

app = FastAPI(title="AI Research Analyzer API", version="1.0.0")

@app.get("/")
def root():
    return {"message": "AI Research Analyzer API", "docs": "/docs", "health": "/health"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/research", response_model=ResearchResponse)
def research(request: ResearchRequest):
    topic = request.topic.strip()
    if not topic:
        raise HTTPException(status_code=422, detail="Topic cannot be empty.")
    try:
        plan = plan_research(topic)
        analysis = analyze_research(topic, plan)
        review = review_research(topic, analysis)
        return ResearchResponse(
            topic=topic,
            research_plan=plan,
            research_analysis=analysis,
            research_review=review,
        )
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Research workflow failed: {exc}") from exc
