# Project Summary

## Objective

Build a machine learning model capable of detecting anomalous network traffic that may indicate malicious activity within enterprise network environments.

## Dataset

CIC-IDS2017 cybersecurity dataset containing labeled network traffic flows.

Approximately 700,000 network flow records were processed using Python (pandas) ETL workflows.

## Approach

The project applies an Isolation Forest anomaly detection model to identify unusual traffic patterns.

Steps in the workflow:

1. Ingest network flow data
2. Perform feature engineering on network metadata
3. Train Isolation Forest anomaly detection model
4. Generate anomaly scores
5. Analyze anomalous flows and destination ports

## Evaluation

Detection results were evaluated using:

- Precision
- Recall
- Anomaly score thresholds

These metrics help balance detection sensitivity and false positive rates.

## Key Technologies

Python  
pandas  
Scikit-learn  
Jupyter Notebook  
Git

## Outcome

The model successfully identified anomalous network traffic patterns that correspond to labeled attack traffic within the dataset.