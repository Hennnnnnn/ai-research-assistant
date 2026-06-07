def writer_agent(state):
    """Compose the final report as a structured dict.

    If the researcher already produced a dict, pass it through. Otherwise
    wrap the raw string output under `overview` and provide empty lists for
    the other sections so downstream code gets a consistent shape.
    """
    research_data = state.get("research_data")

    if isinstance(research_data, dict):
        final = research_data
    else:
        final = {
            "overview": research_data or "",
            "key_findings": [],
            "risks": [],
            "future_trends": []
        }

    state["final_report"] = final

    return state