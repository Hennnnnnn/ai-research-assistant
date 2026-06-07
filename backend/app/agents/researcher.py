from app.services.openai_service import generate_research_summary

def researcher_agent(state):
    state["research_data"] = generate_research_summary(state["topic"])
    
    return state