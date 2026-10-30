
from app.config import ENABLE_WEB_SEARCH


def web_search(query: str, recency_days: int = 365) -> str:
    """Search the public web for research information."""

    if not ENABLE_WEB_SEARCH:
        return "Web search is disabled in configuration."

    try:
        from ddgs import DDGS

        if recency_days <= 1:
            timelimit = "d"
        elif recency_days <= 7:
            timelimit = "w"
        elif recency_days <= 30:
            timelimit = "m"
        else:
            timelimit = "y"

        with DDGS() as ddgs:
            results = list(
                ddgs.text(
                    query,
                    max_results=5,
                    timelimit=timelimit
                )
            )

        if not results:
            return "No search results found."

        lines = []
        for i, item in enumerate(results, 1):
            lines.append(
                f"{i}. {item.get('title', 'Untitled')}\n"
                f"{item.get('body', '')}\n"
                f"URL: {item.get('href', '')}"
            )

        return "\n\n".join(lines)

    except Exception as exc:
        return (
            f"Web search unavailable ({type(exc).__name__}). "
            "Live search failed; continue cautiously."
        )
