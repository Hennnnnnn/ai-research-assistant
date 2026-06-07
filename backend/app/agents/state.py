from typing import TypedDict


class ResearchState(
    TypedDict
):
    topic: str

    research_plan: str

    search_results: list

    sources: list

    research_data: dict

    final_report: dict