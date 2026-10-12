import time
from fastapi import FastAPI, HTTPException, status
from app.schemas import SupportTicket, TriageResult
from app.feature_extractor import FeatureExtractor
from app.routing_engine import DecisionEngine

app = FastAPI(
    title="AI Multimodal Triage & Decision Routing Engine",
    description="Asynchronous pipeline using FastAPI to ingest and route unstructured support data.",
    version="1.0.0"
)

@app.get("/")
async def root():
    return {"message": "AI Multimodal Triage & Decision Routing Engine is running!"}

@app.get("/health", status_code=status.HTTP_200_OK)
async def health_check():
    return {"status": "healthy", "service": "Multimodal Triage Engine"}

@app.post("/api/v1/triage", response_model=TriageResult, status_code=status.HTTP_200_OK)
async def triage_ticket(ticket: SupportTicket):
    start_time = time.perf_counter()

    try:
        # Asynchronously extract features
        features = await FeatureExtractor.extract_features(ticket.body_text, ticket.attachment_type)
        
        # Evaluate rules and route
        priority, queue, urgency_score = DecisionEngine.evaluate(features)

        processing_time = (time.perf_counter() - start_time) * 1000

        return TriageResult(
            ticket_id=ticket.ticket_id,
            priority=priority,
            assigned_queue=queue,
            urgency_score=urgency_score,
            detected_features=features["detected_features"],
            processing_time_ms=round(processing_time, 2)
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error processing support ticket: {str(e)}"
        )