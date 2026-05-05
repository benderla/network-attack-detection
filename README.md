# Network Attack Detection — End-to-End ML System

This project builds and deploys an anomaly detection system for identifying suspicious network behavior using real-world traffic data (~700K flow records from the CIC-IDS2017 dataset).

The system is designed for highly imbalanced data where attacks are rare but critical, and demonstrates how to move from raw data to a production-ready ML system.

---

## Why This Matters

* Network traffic is highly imbalanced — attacks are rare but high impact
* False negatives (missed attacks) are costly, while false positives create alert fatigue
* Many ML projects stop at modeling — this system extends through deployment and evaluation

This project demonstrates how to design a system that balances these tradeoffs and operates under real-world constraints.

---

## What This System Does

* Detects anomalous network flows using an unsupervised Isolation Forest model
* Engineers features from raw traffic (duration, packet rate, ports, flow statistics)
* Tunes decision thresholds using precision-recall tradeoffs
* Evaluates performance using metrics suited for imbalanced data
* Serves predictions through a FastAPI endpoint
* Packages the system using Docker for consistent deployment

---

## System Architecture

Dataset (~700K records)
→ Feature Engineering
→ Isolation Forest Model
→ Threshold Tuning
→ Evaluation (PR, ROC, F1)
→ FastAPI Inference API
→ Docker Container

---

## Key Results

* Improved model effectiveness through threshold tuning rather than default anomaly scoring
* Optimized for precision-recall tradeoffs to balance detection vs alert noise
* Evaluated using metrics appropriate for imbalanced data (PR curve over accuracy)
* Achieved stable detection performance suitable for anomaly-based security use cases

---

## Model Performance

| Method           | Precision | Recall | F1 Score |
| ---------------- | --------- | ------ | -------- |
| Isolation Forest | 0.64      | 0.69   | 0.66     |

---

### Interpretation

* Precision (0.64): ~64% of flagged anomalies are actual attacks
* Recall (0.69): ~69% of true attacks are successfully detected
* F1 Score (0.66): Balanced performance for an imbalanced anomaly detection problem

These results were achieved through threshold tuning using the precision-recall curve, which is more appropriate than accuracy for highly imbalanced datasets.

Results are based on evaluation against labeled attack data within the CIC-IDS2017 dataset.

---

## Example Usage

### Run API locally

```bash
uvicorn app.main:app --reload
```

### Test prediction

```bash
curl -X POST "http://127.0.0.1:8000/predict" \
-H "Content-Type: application/json" \
-d '{"features": [ ... ]}'
```

### Health check

```bash
curl http://127.0.0.1:8000/health
```

---

## What This Project Demonstrates

* End-to-end ML system design (data → model → API → deployment)
* Handling of imbalanced datasets using appropriate evaluation methods
* Transition from offline model to production inference service
* Practical deployment using Docker and REST APIs

---

## Limitations / Next Steps

* Model is unsupervised — may flag benign anomalies
* Threshold selection is static and could be adaptive
* No live data pipeline or streaming integration

Future improvements:

* Add real-time inference pipeline
* Introduce feedback loop for model retraining
* Expand monitoring for drift and performance degradation

---

## Repository Structure

* `app/` → FastAPI service for inference
* `model/` → trained model artifacts
* `notebooks/` → data exploration and modeling
* `scripts/` → feature engineering and preprocessing
* `docker/` → containerization setup

---

## Tech Stack

* Python (pandas, numpy, scikit-learn)
* FastAPI (model serving)
* Docker (containerization)
* Matplotlib / Seaborn (evaluation and visualization)

---
