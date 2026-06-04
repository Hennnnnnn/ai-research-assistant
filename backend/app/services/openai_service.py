import os
import logging
from openai import OpenAI
from app.core.config import OPENAI_API_KEY


logger = logging.getLogger(__name__)
if not logger.handlers:
    handler = logging.StreamHandler()
    formatter = logging.Formatter("%(asctime)s %(levelname)s %(name)s %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)


client = OpenAI(
    api_key=OPENAI_API_KEY
)

def generate_research_summary(
    topic: str
) -> str:
    prompt = f"""
        Create a concise research report about:
        {topic}
        
        Include:
        1. Overview
        2. Key Findings
        3. Risks
        4. Future Trends
        
        Format the response is markdown.
    """
    
    if not OPENAI_API_KEY:
        logger.warning("OPENAI_API_KEY is not configured; cannot generate research summary.")
        return "Unable to generate research summary."

    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {
                    "role": "system",
                    "content": "You are a professional research analyst."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        try:
            return response.choices[0].message.content
        except Exception:
            try:
                return response.choices[0]["message"]["content"]
            except Exception:
                return str(response)

    except Exception as e:
        logger.exception("OpenAI request failed while generating research summary. API key present=%s", bool(OPENAI_API_KEY))
        return "Unable to generate research summary."