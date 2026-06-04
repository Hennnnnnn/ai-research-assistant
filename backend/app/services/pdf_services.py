from io import BytesIO

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)


def generate_research_pdf(research):
    buffer = BytesIO()

    doc = SimpleDocTemplate(buffer)

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph(
            research.topic,
            styles["Title"]
        )
    )

    content.append(
        Spacer(1, 12)
    )

    # Overview

    content.append(
        Paragraph(
            "Overview",
            styles["Heading2"]
        )
    )

    content.append(
        Paragraph(
            research.research_data["overview"],
            styles["BodyText"]
        )
    )

    content.append(
        Spacer(1, 12)
    )

    # Key Findings

    content.append(
        Paragraph(
            "Key Findings",
            styles["Heading2"]
        )
    )

    for finding in research.research_data["key_findings"]:
        content.append(
            Paragraph(
                f"• {finding}",
                styles["BodyText"]
            )
        )

    content.append(
        Spacer(1, 12)
    )

    # Risks

    content.append(
        Paragraph(
            "Risks",
            styles["Heading2"]
        )
    )

    for risk in research.research_data["risks"]:
        content.append(
            Paragraph(
                f"• {risk}",
                styles["BodyText"]
            )
        )

    content.append(
        Spacer(1, 12)
    )

    # Future Trends

    content.append(
        Paragraph(
            "Future Trends",
            styles["Heading2"]
        )
    )

    for trend in research.research_data["future_trends"]:
        content.append(
            Paragraph(
                f"• {trend}",
                styles["BodyText"]
            )
        )

    doc.build(content)

    buffer.seek(0)

    return buffer