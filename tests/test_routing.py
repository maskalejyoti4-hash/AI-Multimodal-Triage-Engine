import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_urgent_ticket_routing():
    payload = {
        "ticket_id": "TICK-9001",
        "customer_id": "CUST-101",
        "subject": "System Outage",
        "body_text": "The entire server is broken and down. Urgent fix needed!",
        "attachment_type": "image"
    }
    response = client.post("/api/v1/triage", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["priority"] == "URGENT"
    assert data["assigned_queue"] == "Tier-3-Emergency-Support"
    assert "urgent_keyword_detected" in data["detected_features"]