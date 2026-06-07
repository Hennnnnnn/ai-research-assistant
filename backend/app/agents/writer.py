def writer_agent(state):
    research_data = state.get(
        "research_data",
        {}
    )

    if not isinstance(
        research_data,
        dict
    ):
        research_data = {
            "overview":
                str(research_data),

            "key_findings": [],

            "risks": [],

            "future_trends": []
        }

    research_data["sources"] = (
        state.get(
            "sources",
            []
        )
    )

    state["final_report"] = (
        research_data
    )

    return state