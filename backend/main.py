# main.py — Local Offline FastAPI Server for Aegis-BioSpace
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json
from pathlib import Path
from cyber_shield import SpaceCyberShield
from analytics_engine import compute_personal_zscore, evaluate_alert_color, calculate_space_drug_potency

app = FastAPI(title="Aegis-BioSpace Local Engine")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

shield = SpaceCyberShield()
MATRIX_PATH = Path(__file__).resolve().parent.parent / "data" / "nasa_osdr_matrix.json"

@app.get("/health")
def health_check():
    return {"status": "ok", "mode": "offline_ready"}

@app.get("/api/matrix")
def get_matrix():
    if MATRIX_PATH.exists():
        return json.loads(MATRIX_PATH.read_text(encoding="utf-8"))
    return {"error": "nasa_osdr_matrix.json not found"}

@app.post("/api/analyze")
def analyze_pathway(payload: dict):
    reading = float(payload.get("reading", 75.0))
    history = payload.get("history", [70, 72, 74, 71, 73])
    z = compute_personal_zscore(reading, history)
    pharm = calculate_space_drug_potency(
        base_dose_mg=float(payload.get("base_dose_mg", 100)),
        mission_days=int(payload.get("mission_days", 180)),
        cumulative_rad_msv=float(payload.get("radiation_msv", 240))
    )
    block = shield.append_record(payload.get("path_id", 1), "Telemetry Analysis", {"reading": reading, "z": z})
    return {"z_score": z, "pharmacy": pharm, "audit_block": block}
