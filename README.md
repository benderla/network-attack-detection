# Network Attack Detection using Machine Learning

This project explores machine learning techniques for identifying suspicious
network traffic using the CIC-IDS2017 intrusion detection dataset.

The goal is to demonstrate how anomaly detection models can help surface
potential malicious activity within large volumes of network flow data.

---

## Dataset

CIC-IDS2017 Intrusion Detection Dataset

This dataset contains labeled network traffic including both benign activity
and multiple attack types such as:

- DoS Hulk
- DoS GoldenEye
- Slowloris
- Slowhttptest
- Heartbleed

Each record represents a network flow with statistical features describing
packet counts, byte rates, durations, and connection behavior.

---

## Approach

The project uses an unsupervised anomaly detection approach.

Steps performed:

1. Load and clean the network flow dataset
2. Train an Isolation Forest model on benign traffic
3. Score all flows based on anomaly likelihood
4. Identify the most suspicious network activity
5. Visualize anomalous flows and suspicious destination ports

---

## Key Findings

The anomaly detection model highlights flows that deviate most strongly
from normal network behavior.

Analysis of suspicious flows shows patterns consistent with attack behavior
present in the dataset, including abnormal connection durations and traffic
rates.

Port analysis helps identify the network services most associated with
suspicious activity.

---

## Visualizations

The notebook includes visualizations such as:

- Top Suspicious Network Flows
- Suspicious Destination Ports

These visualizations help analysts quickly identify unusual traffic patterns.

---

## Future Work

Potential improvements include:

- Adding additional feature engineering
- Evaluating supervised classification models
- Investigating temporal attack patterns
- Integrating results with SIEM-style alerts

---

## Author

Lee