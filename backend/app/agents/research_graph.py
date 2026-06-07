from langgraph.graph import StateGraph, END

from app.agents.state import ResearchState
from app.agents.planner import planner_agent
from app.agents.researcher import researcher_agent
from app.agents.writer import writer_agent
from app.agents.searcher import search_agent

workflow = StateGraph(
    ResearchState
)

workflow.add_node(
    "planner",
    planner_agent
)

workflow.add_node(
    "researcher",
    researcher_agent
)

workflow.add_node(
    "writer",
    writer_agent
)

workflow.add_node(
    "searcher",
    search_agent
)

workflow.set_entry_point(
    "planner"
)

workflow.add_edge(
    "planner",
    "searcher"
)

workflow.add_edge(
    "searcher",
    "researcher"
)

workflow.add_edge(
    "researcher",
    "writer"
)

workflow.add_edge(
    "writer",
    END
)

research_graph = (
    workflow.compile()
)