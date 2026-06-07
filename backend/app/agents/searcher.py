from tavily import TavilyClient

from app.core.config import (
    TAVILY_API_KEY
)

from app.agents.state import (
    ResearchState
)

client = TavilyClient(
    api_key=TAVILY_API_KEY
)


def search_agent(
    state: ResearchState
):
    response = client.search(
        query=state["topic"],
        max_results=5
    )

    state["search_results"] = (
        response["results"]
    )
    
    print(response)

    return state