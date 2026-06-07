from app.agents.state import ResearchState

def planner_agent(state: ResearchState):
    topic = state["topic"]
    
    plan = f"""
        Research the following topic:
        
        {topic}
        
        Collect:
        1. Overview
        2. Key findings
        3. Risks
        4. Future trends
    """
    
    state["research_plan"] = plan
    
    return state