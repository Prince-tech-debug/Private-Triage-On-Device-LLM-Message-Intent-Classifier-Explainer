from fastapi import FastAPI, HTTPException
from core.schemas import EmailRequest, EmailTriageResponse
from core.model import GemmaTriageEngine

app = FastAPI(
    title="Private-Triage Engine",
    description="Local, offline Email Summarization & Triage API running Gemma 3 4B GGUF",
    version="1.0.0"
)

# Initialize engine on startup
MODEL_PATH = "./Inference/gemma-3-4b-it.Q4_K_M.gguf"
engine = GemmaTriageEngine(model_path=MODEL_PATH)

@app.get("/health")
def health_check():
    return {"status": "online", "model_loaded": engine.llm is not None}

@app.post("/api/v1/triage", response_model=EmailTriageResponse)
def triage_email(payload: EmailRequest):
    try:
        result = engine.analyze_email(
            sender=payload.sender,
            subject=payload.subject,
            body=payload.body
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)