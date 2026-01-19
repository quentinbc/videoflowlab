from fastapi import FastAPI
from pydantic import BaseModel
from rsai_worker.pipeline.export import run_pipeline

app = FastAPI(title="RS AI Worker", version="0.1.0")

class Job(BaseModel):
    job_id: str
    language: str = "fr"
    topic: str
    target_platforms: list[str] = ["tiktok", "youtube", "linkedin"]
    duration_sec: int = 45

@app.get("/health")
def health():
    return {"ok": True}

@app.post("/run")
def run(job: Job):
    result = run_pipeline(job.model_dump())
    return result
