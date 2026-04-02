# Network Attack Detection using Isolation Forest

Machine Learning | Cybersecurity | Anomaly Detection | Python | FastAPI | Docker

---

## 🚀 Overview

End-to-end anomaly detection system for identifying suspicious network traffic using the CIC-IDS2017 dataset (~700K flows).

This project demonstrates how unsupervised machine learning can surface malicious behavior without relying on predefined attack signatures.

---

## 🧠 Problem

Traditional rule-based detection struggles with:
- Zero-day attacks  
- Evolving traffic patterns  
- Large-scale network data  

This project shows how anomaly detection can identify unusual behavior for security investigation workflows.

---

## ⚙️ Approach

- Model: Isolation Forest (unsupervised)  
- Dataset: CIC-IDS2017 (~700K network flows)  
- Features: network flow statistics (duration, packet counts, byte size, ports)  
- Output: anomaly scores → threshold → attack classification  

### Key Design Decisions

- Converted anomaly scores into binary predictions via threshold tuning  
- Optimized threshold using F1 score  
- Evaluated against labeled attack data (critical for validation)  

---

## 📊 Model Evaluation

| Metric     | Value |
|------------|------|
| Precision  | 0.64 |
| Recall     | 0.69 |
| F1 Score   | 0.66 |
| ROC AUC    | 0.70 |
| PR AUC     | 0.51 |

### Key Insights

- Threshold tuning improved F1 from ~0.26 → 0.66  
- Model captures majority of attack traffic (69% recall)  
- Precision-recall tradeoff enables tuning for alert sensitivity vs false positives  
- Performance aligns with real-world anomaly detection systems  

---

## 📈 Visualizations

### ROC Curve
![ROC Curve](docs/roc_curve.png)

### Precision-Recall Curve
![PR Curve](docs/pr_curve.png)

### Confusion Matrix
![Confusion Matrix](docs/confusion_matrix.png)

---

## 🔍 Feature Importance

Top drivers of anomalous behavior:

- Flow duration  
- Packet counts (forward/backward)  
- Packet length statistics  
- Idle time metrics  

These features capture patterns such as:

- scanning activity  
- denial-of-service behavior  
- abnormal communication bursts  

---

## 🏗️ Architecture

### ML Pipeline
![ML Pipeline](docs/ml-pipeline.png)

### Deployment Architecture
![Deployment Architecture](docs/deployment-architecture.png)

---

## 🧩 Project Structure
network-attack-detection/
├── data/
├── notebooks/
├── docs/
├── src/
├── model/
├── monitoring/
├── tests/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md

---

## ▶️ How to Run

```bash
pip install -r requirements.txt
jupyter notebook

---

## 🚀 API Inference Service

The trained anomaly detection model is exposed via a FastAPI service for real-time inference.

### Run with Docker

```bash
docker build -t anomaly-detector .
docker run -p 8000:8000 anomaly-detector

### Example Request

POST /predict

http://localhost:8000/predict?duration=10000&packet_rate=50

### Example Response

```json
{
  "anomaly_score": 0.168
}