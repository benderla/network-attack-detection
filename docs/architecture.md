# ML Platform Architecture

This project demonstrates a lightweight machine learning platform for detecting anomalous network traffic.

## Architecture Overview

The system consists of five major components:

1. Data Processing Pipeline
Network flow records are processed using Python and Pandas to generate behavioral features such as packet rate, duration, and destination port distribution.

2. Machine Learning Model
An Isolation Forest anomaly detection model identifies unusual traffic patterns using engineered features.

3. Inference API Service
A FastAPI service exposes the trained model through a REST API, allowing external systems to submit network flow features and receive anomaly scores.

4. Containerized Runtime
The service runs inside a Docker container to ensure reproducible environments and consistent deployment.

5. Monitoring and Evaluation
Model performance is evaluated using precision/recall metrics and anomaly score distribution analysis.