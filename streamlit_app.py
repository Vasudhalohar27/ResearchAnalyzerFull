import streamlit as st
from pathlib import Path
from app.agents.research_team import plan_research
from app.agents.research_analyst import analyze_research
from app.agents.research_reviewer import review_research

st.set_page_config(page_title="AI Research Analyzer", page_icon="📚", layout="wide")
st.title("📚 AI Research Analyzer")
st.write("An AI-powered research assistant that plans, analyzes, and reviews a research topic using three agents.")

topic = st.text_input("Enter your research topic", placeholder="e.g., Impact of Artificial Intelligence on Education")

if st.button("Generate Research Report", type="primary"):
    if not topic.strip():
        st.warning("Please enter a research topic.")
    else:
        try:
            with st.spinner("Agent 1: Creating research plan..."):
                plan = plan_research(topic.strip())
            with st.spinner("Agent 2: Analyzing research..."):
                analysis = analyze_research(topic.strip(), plan)
            with st.spinner("Agent 3: Reviewing research..."):
                review = review_research(topic.strip(), analysis)

            st.success("Research workflow completed!")
            with st.expander("1. Research Plan", expanded=True):
                st.markdown(plan)
            with st.expander("2. Research Analysis", expanded=True):
                st.markdown(analysis)
            with st.expander("3. Research Review", expanded=True):
                st.markdown(review)

            report = (
                "AI RESEARCH ANALYZER REPORT\\n" + "=" * 50
                + f"\\n\\nRESEARCH TOPIC\\n{topic.strip()}"
                + f"\\n\\n1. RESEARCH PLAN\\n{plan}"
                + f"\\n\\n2. RESEARCH ANALYSIS\\n{analysis}"
                + f"\\n\\n3. RESEARCH REVIEW\\n{review}\\n"
            )
            data_dir = Path("app/data")
            data_dir.mkdir(parents=True, exist_ok=True)
            (data_dir / "research_report.txt").write_text(report, encoding="utf-8")
            st.download_button("Download Research Report", data=report, file_name="research_report.txt", mime="text/plain")
        except Exception as error:
            st.error(f"Research workflow failed: {error}")
            st.info("Check .env, your Groq API key/model, internet connection, and container logs.")

st.divider()
st.caption("AI-generated research is preliminary. Verify important claims and references using reliable sources.")
