# Model Card — Network Anomaly Detection Model

## Model Overview

This project implements an anomaly detection system for identifying malicious network activity using the CIC-IDS2017 dataset.

The system uses an Isolation Forest model to detect abnormal network flow behavior without requiring labeled attack data.

Primary goal:
Detect unusual traffic patterns that may indicate cybersecurity threats.

---

## Model Type

Isolation Forest (unsupervised anomaly detection)

Framework:
scikit-learn

Features:
78 network traffic features including

- Flow Duration
- Packet Length Statistics
- Inter-arrival Time metrics
- Forward/Backward packet statistics

---

## Training Data

Dataset:
CIC-IDS2017 Intrusion Detection Dataset

Records processed:

697,203 network flows

Feature engineering performed on:

- packet statistics
- timing behavior
- connection duration
- port activity

---

## Evaluation Metrics

Evaluation uses labeled attack traffic to measure detection performance.

Metrics:

Precision
Recall
F1 Score

Additional analysis:

- anomaly score distribution
- precision-recall threshold tuning
- feature influence analysis

Visualizations available in:

docs/anomaly-score-distribution.png  
docs/precision-recall-threshold.png  
docs/feature-importance.png  

---

## Deployment Architecture

Model deployed through a REST API using FastAPI.

Deployment pipeline:

Network Logs  
→ Feature Engineering  
→ Isolation Forest Model  
→ FastAPI Inference API  
→ Docker Container  
→ Monitoring Dashboard

---

## Monitoring Strategy

Production monitoring tracks:

Prediction volume  
Anomaly detection rate  
Feature distribution drift  
Model inference latency

Monitoring dashboard example:

docs/monitoring-dashboard.png

---

## Limitations

Isolation Forest detects statistical anomalies but cannot classify attack types.

False positives may occur when legitimate traffic deviates from historical patterns.

Model performance depends on feature engineering quality.

---

## Future Improvements

Potential improvements include:

Supervised classifiers for attack classification

Online model retraining

Feature store integration

Advanced drift detection