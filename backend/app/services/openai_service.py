import json
import logging

from openai import OpenAI

from app.core.config import OPENAI_API_KEY

logger = logging.getLogger(__name__)

client = OpenAI(
    api_key=OPENAI_API_KEY
)


def generate_research_summary(
    topic: str
) -> dict:
    prompt = f"""
        Create a research report about:

        {topic}

        Return ONLY valid JSON.

        Do not wrap the JSON inside markdown code blocks.
        Do not include explanations.
        Do not include any text outside JSON.

        Schema:

        {{
            "overview": "",
            "key_findings": [],
            "risks": [],
            "future_trends": []
        }}
    """

    if not OPENAI_API_KEY:
        raise ValueError(
            "OPENAI_API_KEY is not configured."
        )

    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a professional research analyst."
                    )
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.7
        )

        content = (
            response
            .choices[0]
            .message
            .content
        )

        if not content:
            raise ValueError(
                "OpenAI returned empty content."
            )

        content = (
            content
            .replace("```json", "")
            .replace("```", "")
            .strip()
        )

        return json.loads(content)

    except json.JSONDecodeError:
        logger.exception(
            "Failed to parse OpenAI JSON response"
        )

        raise

    except Exception:
        logger.exception(
            "OpenAI request failed"
        )

        raise