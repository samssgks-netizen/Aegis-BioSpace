# analytics_engine.py — Personal Z-Score, Spacecraft Physics & ExMC Space Pharmacy Engine
import math
import numpy as np

def compute_personal_zscore(reading: float, baseline_history: list) -> float:
    arr = np.array(baseline_history, dtype=float)
    mean = float(np.mean(arr))
    std = max(float(np.std(arr)), 0.1)
    return round(abs(reading - mean) / std, 2)

def evaluate_alert_color(reading: float, z_score: float, normal_min: float, normal_max: float, crit_min: float, crit_max: float) -> str:
    if reading >= crit_max or reading <= crit_min or z_score >= 3.0:
        return "red"
    if reading > normal_max or reading < normal_min or z_score >= 2.0:
        return "amber"
    return "green"

def calculate_space_drug_potency(base_dose_mg: float, mission_days: int, cumulative_rad_msv: float) -> dict:
    # First-order radiation & thermal degradation kinetics per NASA ExMC Gap Med02 Pharmacy model
    potency_fraction = math.exp(-(0.00035 * mission_days + 0.00042 * cumulative_rad_msv))
    potency_pct = round(max(0.65, min(0.99, potency_fraction)) * 100, 1)
    adjusted_dose = round(base_dose_mg * (100.0 / potency_pct), 1)
    return {
        "remaining_potency_pct": potency_pct,
        "base_dose_mg": base_dose_mg,
        "space_adjusted_dose_mg": adjusted_dose
    }
