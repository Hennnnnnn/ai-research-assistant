from typing import TypedDict


class ResearchState(TypedDict):
    topic: str

    research_plan: str

    search_results: list

    research_data: dict

    final_report: dict