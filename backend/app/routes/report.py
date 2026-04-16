from fastapi import APIRouter
from app.agent import generate_summary
from app.email_service import send_email

router = APIRouter()

@router.post("/generate-report")
def generate_report(data: dict):
    try:
        summary = generate_summary(data)

        email_sent = send_email(summary)

        return {
            "clinical_summary": summary,
            "email_sent": email_sent
        }

    except Exception as e:
        return {
            "clinical_summary": "Error generating summary",
            "email_sent": False,
            "error": str(e)
        }