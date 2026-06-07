from app.services.openai_service import generate_research_summary

def researcher_agent(state):
    sources = state.get(
        "sources",
        []
    )

    state["research_data"] = (
        generate_research_summary(
            state["topic"],
            sources
        )
    )

    return state