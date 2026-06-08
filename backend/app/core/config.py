from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

SECRET_KEY = os.getenv("SECRET_KEY")

ALGORITHM = os.getenv("ALGORITHM")

ACCESS_TOKEN_EXPIRE_MINUTES = int(
    os.getenv(
        "ACCESS_TOKEN_EXPIRE_MINUTES",
        "30"
    )
)

OPENAI_API_KEY = os.getenv(
    "OPENAI_API_KEY"
)

TAVILY_API_KEY = os.getenv(
    "TAVILY_API_KEY"
)

CELERY_BROKER_URL = os.getenv(
    "CELERY_BROKER_URL"
)

CELERY_RESULT_BACKEND = os.getenv(
    "CELERY_RESULT_BACKEND"
)