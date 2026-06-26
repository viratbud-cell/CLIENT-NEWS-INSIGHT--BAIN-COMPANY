from fastapi import FastAPI

app = FastAPI(
    title="Client News Insight API",
    description="Backend API for generating company news briefings for Bain partners.",
    version="1.0.0",
)


@app.get("/")
def home():
    return {
        "message": "Client News Insight API is running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "ok"
    }


@app.get("/api/brief")
def get_company_brief(company: str):
    return {
        "company": company,
        "summary": f"This is a sample briefing for {company}.",
        "key_news": [
            f"{company} has recent business activity worth reviewing."
        ],
        "risks": [
            "Market changes may affect near-term performance."
        ],
        "opportunities": [
            "Recent company activity may create consulting opportunities."
        ],
        "recommended_talking_points": [
            f"Ask how {company} is responding to recent market developments.",
            "Explore whether leadership needs support with strategy, operations, or transformation."
        ]
    }