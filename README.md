# Aegis-BioSpace — Autonomous Offline-First Astronaut Health & Cyber-Resilient Decision Support OS

**Event:** 2026 NASA Space Apps Challenge (Saudi Arabia — Al Khobar / Dammam)  
**Challenge:** [Create Health Monitoring Software for Astronauts on Space Missions](https://www.spaceappschallenge.org/2026/challenges/health-monitoring-software/)  
**Team Name:** NAJEM (N.J. The Star — Advanced Space Technology & Research Alliance)  

## 1. High-Level Summary
**Aegis-BioSpace** is an offline-first, autonomous clinical and behavioral decision-support software built for long-duration spaceflight missions to the Moon (Artemis) and Mars. Facing up to 40-minute round-trip communication delays, astronauts cannot wait for Earth flight surgeons or interpret complex raw telemetry charts during acute medical crises. Aegis-BioSpace combines an interactive 5-system anatomical avatar, a physics-based spacecraft environment simulator calibrated with official `NASA-STD-3001` technical briefs, a 10-second Psychomotor Vigilance Task (`Micro-PVT`) with resilience gamification, an `ExMC Gap Med02` space-pharmacy radiation degradation calculator, and a cosmic-ray fault-tolerant `SHA-256` Hash-Chain with Triple Modular Redundancy (`TMR`) self-healing.

## 2. How to Run It (100% Offline-First)
- **Instant Browser Mode (Zero Installation):** Open `index.html` (or `aegis_biospace.html`) directly in any modern browser (Edge, Chrome, Firefox). It runs 100% offline with zero external network dependencies.
- **Optional Local Python FastAPI Engine:**
  ```bash
  cd backend
  pip install fastapi uvicorn numpy
  uvicorn main:app --reload
  ```

## 3. Core Architecture & Key Features
1. **5-System Clickable Astronaut Avatar:** Maps NASA's 5 spaceflight hazards to 5 clickable organ systems (`Brain` Behavioral/Circadian, `Heart` Cardiovascular/SANS, `Blood` Radiation/Immunity, `Bones & Kidneys` Renal Stones/Urinary Health, and `Lungs` Cabin CO2/O2) across 4 mission environments (`ISS`, `Mars Transit`, `Surface Rover`, `Planetary Base`).
2. **Physics-Based Spacecraft Simulator:** Computes crew metabolic $CO_2$ output (`0.455 to 4.985 g/min` at 75% $VO_2\text{max}$, $RQ=0.92$), cumulative urine output ($V_u = 3 + 2.5t\text{ L}$), and water-bag storm shelter attenuation (cutting SPE radiation dose from `259 mSv` to `66 mSv`).
3. **Closed-Loop Escalation & ExMC Med02 Space Pharmacy:** Guides astronauts via offline voice (`Web Speech API`) and single-key `Spacebar` Zero-G controls through Level 1 physical/environmental countermeasures (`CDRA/TAS/LiOH`, `Thigh Cuffs`, `LBNP`, `ARED`, `AMOS 3mm Ultrasound`, `480nm LED`). If vitals fail to recover after the countdown timer, it auto-escalates to Level 2, compensating drug doses for radiation-induced API degradation and guiding handheld `Raman/FTIR` verification.
4. **Cyber-Resilience & Cosmic-Ray Shield (`øX7` Engine):** Protects medical records against cosmic-ray Single-Event Upsets (`Bit-Flips`) and tampering using synchronous FIPS 180-4 `SHA-256` hash chaining, 2-of-3 Triple Modular Redundancy (`TMR`) majority voting, cross-sensor spoofing rejection, and a `<2 KB` signed Earth-Sync burst packet.

## 4. NASA Datasets, Technical Briefs & References Used
1. **2026 NASA Space Apps Challenge Official Statement:** [Create Health Monitoring Software for Astronauts on Space Missions](https://www.spaceappschallenge.org/2026/challenges/health-monitoring-software/)
2. **NASA ExMC Gap Med02 Space Pharmacy Plan:** [Risk of Adverse Health Outcomes & Decrements in Performance due to Inflight Medical Conditions — Gap Med02: Exploration Medical Capability (ExMC) Pharmacy Research Plan (NTRS 20170001651)](https://ntrs.nasa.gov/citations/20170001651)
3. **NASA Neurolab STS-90 & STS-95 Sleep & PVT Study:** [Dijk, D.J., Neri, D.F., Wyatt, J.K., Czeisler, C.A., et al. — Sleep, Circadian Rhythms, and Performance During Space Shuttle Missions (NASA NTRS 20030068197)](https://ntrs.nasa.gov/api/citations/20030068197/downloads/20030068197.pdf)
4. **NASA-STD-3001 Urinary Health & Renal Stones Brief:** [NASA OCHMO-MTB-003 Rev A: Urinary Health Medical Technical Brief](https://www.nasa.gov/wp-content/uploads/2025/01/ochmo-mtb-003-urinary-health.pdf) & [NASA HSRB: Risk of Renal Stone Formation](https://www.nasa.gov/directorates/esdmd/hhp/risk-of-renal-stone-formation/)
5. **NASA-STD-3001 Ionizing Radiation Protection Brief:** [NASA OCHMO-TB-020 Rev E: Design for Ionizing Radiation Protection Technical Brief](https://www.nasa.gov/wp-content/uploads/2023/03/radiation-protection-technical-brief-ochmo.pdf)
6. **NASA-STD-3001 Carbon Dioxide (CO2) & ECLSS Brief:** [NASA OCHMO-TB-004 Rev D: Carbon Dioxide (CO2) Technical Brief](https://www.nasa.gov/ochmo-tb-004-carbon-dioxide-2/) ([PDF](https://www.nasa.gov/wp-content/uploads/2023/12/ochmo-tb-004-carbon-dioxide.pdf)) & [NASA OCHMO-TB-003 Rev A: Habitable Atmosphere](https://www.nasa.gov/wp-content/uploads/2023/12/ochmo-tb-003-habitable-atmosphere.pdf)
7. **NASA Human Research Program (HRP) — Hazards & Ongoing Research:** [Human Spaceflight Hazards: Hostile/Closed Environments (HERA) & Ongoing HRP Research in Space (ARCHeR, Thigh Cuff, B-Complex, Venous Haemostasis, Space Gardening, Tempus Pro)](https://www.nasa.gov/hrp/)
8. **NASA Open Science Data Repository (OSDR):** [NASA OSDR Portal](https://www.nasa.gov/osdr/)

## 5. Use of AI (SI) & Open-Source Tools Disclosure
- **Open-Source Stack:** HTML5, Tailwind CSS, Vanilla JavaScript (ES6+), Inline SVG Anatomical Graphics, Web Speech API (`window.speechSynthesis`), Synchronous FIPS 180-4 `SHA-256` & `TMR` Engine, Python 3, `FastAPI`, and `NumPy`.
- **AI Tools Used:** Gemini and GitHub Copilot were used to assist in structuring the single-page web prototype, formatting the JSON schema from the NASA technical briefs, and debugging UI event handlers. All medical thresholds, physical equations, and clinical countermeasures were verified against the official NASA documents listed above.

## 6. Team Members — Team NAJEM (N.J. The Star)
- **Shatha Asaad (`øX7`)** — Team Lead, Cybersecurity (`SHA-256 TMR`) & Analytical Engine Lead
- **Engineering Lead** — Full-Stack Architecture & Cockpit UI
- **Chemistry Lead** — ExMC Space Pharmacology, Radiation & Renal Pathways
- **Science Lead 2** — Cardiovascular (`SANS`) & ECLSS Atmospheric (`CO2`) Pathways
- **Science Lead 3** — Behavioral Health, Circadian Lighting & Micro-PVT Trials
