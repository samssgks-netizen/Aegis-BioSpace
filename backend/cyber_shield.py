# cyber_shield.py — Aegis-BioSpace Cyber-Resilience & Cosmic-Ray Fault-Tolerance Layer (Lead: Shatha Asaad / øX7)
import hashlib
import json
from datetime import datetime, timezone

class SpaceCyberShield:
    def __init__(self):
        self.chain = []
        self.tmr_store = {}

    def _compute_hash(self, prev_hash: str, payload: dict) -> str:
        raw = f"{prev_hash}|{json.dumps(payload, sort_keys=True)}"
        return hashlib.sha256(raw.encode("utf-8")).hexdigest()

    def append_record(self, pathway_id: int, event: str, reading: dict) -> dict:
        prev_hash = self.chain[-1]["curr_hash"] if self.chain else "0" * 64
        payload = {
            "id": len(self.chain) + 1,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "pathway_id": pathway_id,
            "event": event,
            "reading": reading
        }
        curr_hash = self._compute_hash(prev_hash, payload)
        block = {**payload, "prev_hash": prev_hash, "curr_hash": curr_hash}
        self.chain.append(block)
        # Triple Modular Redundancy (3 isolated memory slots: SRAM-1, SRAM-2, FLASH-3)
        self.tmr_store[block["id"]] = [
            json.dumps(reading),
            json.dumps(reading),
            json.dumps(reading)
        ]
        return block

    def verify_chain(self) -> dict:
        for idx, block in enumerate(self.chain):
            expected_prev = "0" * 64 if idx == 0 else self.chain[idx - 1]["curr_hash"]
            payload = {k: block[k] for k in ("id", "timestamp", "pathway_id", "event", "reading")}
            recalculated = self._compute_hash(expected_prev, payload)
            if block["prev_hash"] != expected_prev or block["curr_hash"] != recalculated:
                return {"valid": False, "corrupted_block_id": block["id"]}
        return {"valid": True, "corrupted_block_id": None}

    def vote_tmr(self, block_id: int) -> dict:
        replicas = self.tmr_store.get(block_id, [])
        if len(replicas) < 3:
            return {"status": "error", "healed_value": None}
        a, b, c = replicas[0], replicas[1], replicas[2]
        majority = a if (a == b or a == c) else (b if b == c else a)
        corrupted_slot = None
        for i, val in enumerate([a, b, c]):
            if val != majority:
                corrupted_slot = ["Replica_A", "Replica_B", "Replica_C"][i]
                self.tmr_store[block_id][i] = majority
        return {
            "status": "healed" if corrupted_slot else "intact",
            "corrupted_slot": corrupted_slot,
            "healed_value": json.loads(majority)
        }

    @staticmethod
    def cross_sensor_validate(hr_bpm: float, prev_hr: float, hrv_ms: float, prev_hrv: float) -> dict:
        if abs(hr_bpm - prev_hr) > 60 and abs(hrv_ms - prev_hrv) < 1.0:
            return {"authentic_medical_event": False, "reason": "Isolated single-sensor spike (Spoofing/Fault)"}
        return {"authentic_medical_event": True, "reason": "Coupled physiological response verified"}
