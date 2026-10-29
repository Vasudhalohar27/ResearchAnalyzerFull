from app.config import ENABLE_WEB_SEARCH

def web_search(query: str) -> str:
    """Search the public web for recent information related to a research topic."""
    if not ENABLE_WEB_SEARCH:
        return "Web search is disabled in configuration."
    try:
        from duckduckgo_search import DDGS
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=5))
        if not results:
            return "No search results found. Continue with general knowledge and clearly flag uncertainty."
        lines = []
        for i, item in enumerate(results, 1):
            title = item.get("title", "Untitled")
            body = item.get("body", "")
            href = item.get("href", "")
            lines.append(f"{i}. {title}\\n{body}\\nURL: {href}")
        return "\\n\\n".join(lines)
    except Exception as exc:
        return f"Web search unavailable ({type(exc).__name__}). Continue cautiously and note that live search failed."
