from app.core.celery_app import celery_app
from app.database.database import SessionLocal
from app.models.research_session import ResearchSession
from app.agents.research_graph import research_graph
from app.models.enums import ResearchStatus


@celery_app.task
def generate_research_task(
    research_id: int
):
    print(
        f"Start generate_research_task {research_id}"
    )

    db = SessionLocal()

    research = None

    try:
        research = db.get(
            ResearchSession,
            research_id
        )
        
        if not research:
            print(
                f"Research {research_id} not found"
            )
            return

        if not research:
            return

        update_progress(
            db,
            research,
            "Searching sources..."
        )

        update_progress(
            db,
            research,
            "Analyzing information..."
        )

        result = research_graph.invoke(
            {
                "topic": research.topic
            }
        )

        update_progress(
            db,
            research,
            "Writing report..."
        )

        research.research_data = (
            result["final_report"]
        )

        research.progress_message = (
            "Completed"
        )

        research.status = (
            ResearchStatus.COMPLETED.value
        )

        db.commit()

    except Exception as e:
        print(
            f"Research failed: {e}"
        )

        if research:
            research.progress_message = (
                "Failed"
            )

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
        print(
            f"FINISH generate_research_task {research_id}"
        )

        db.close()


def update_progress(
    db,
    research,
    message: str
):
    research.progress_message = message

    db.commit()

    db.refresh(research)