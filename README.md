# Network Attack Detection — End-to-End ML System

This project builds and deploys an anomaly detection system for identifying suspicious network behavior using real-world traffic data (~700K flow records from the CIC-IDS2017 dataset).

---

## Why This Matters

* Network traffic is highly imbalanced — attacks are rare but high impact
* False negatives are costly; false positives create alert fatigue
* Most ML work stops at modeling — this system goes end-to-end

---

## System Architecture

Dataset → Feature Engineering → Model → API → Monitoring → Alert → Retrain

---

## What This System Does

* Isolation Forest anomaly detection
* Feature engineering on network flows
* Threshold tuning using PR curve
* FastAPI inference service
* Docker-ready deployment

---

## Key Results

| Method           | Precision | Recall | F1 Score |
| ---------------- | --------- | ------ | -------- |
| Isolation Forest | 0.64      | 0.69   | 0.66     |

---

## Production Simulation

If deployed in production:

* Ingestion: batch network flow data every hour
* Inference: API or batch scoring
* Monitoring: daily drift detection using statistical tests
* Alerting: trigger investigation when drift or anomaly spikes detected
* Retraining: update model based on new labeled data

---

## Failure Scenario

* Issue: excessive anomalies detected → alert fatigue
* Root Cause: threshold too sensitive
* Fix: recalibrated threshold using precision-recall curve

---

## Limitations

* Unsupervised model may flag benign anomalies
* Static threshold (not adaptive)
* No real-time pipeline

---

## Tech Stack

* Python, scikit-learn
* FastAPI
* Docker

---
