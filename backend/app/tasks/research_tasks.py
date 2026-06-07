from app.core.celery_app import celery_app
from app.database.database import SessionLocal
from app.models.research_session import ResearchSession
from app.agents.research_graph import research_graph
from app.models.enums import ResearchStatus
    
@celery_app.task
def generate_research_task(
    research_id: int
):
    print(f"Start generate_research_task {research_id}")
    db = SessionLocal()

    try:
        research = db.get(
            ResearchSession,
            research_id
        )

        if not research:
            return

        result = research_graph.invoke(
            {
                "topic": research.topic
            }
        )

        research.research_data = (
            result["final_report"]
        )

        research.status = (
            ResearchStatus.COMPLETED.value
        )

        db.commit()

    except Exception:
        if research:
            research.status = (
                ResearchStatus.FAILED.value
            )

            research.research_data = {
                "overview":
                    "Failed to generate research.",

                "key_findings": [],

                "risks": [],

                "future_trends": [],

                "sources": []
            }

            db.commit()

        raise

    finally:
        print(f"FINISH generate_research_task {research_id}")
        
        db.close()
    