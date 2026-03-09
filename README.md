Machine learning project detecting anomalous network traffic using
Isolation Forest on the CIC-IDS2017 cybersecurity dataset.

# Network Attack Detection using Machine Learning

Machine Learning | Cybersecurity | Anomaly Detection | Python

This project explores machine learning techniques for identifying suspicious
network traffic using the CIC-IDS2017 intrusion detection dataset.

The goal is to demonstrate how anomaly detection models can identify
network traffic that deviates from normal behavior and may indicate
malicious activity.

---

## Motivation

Network security analysts must identify malicious activity within extremely
large volumes of traffic data. Traditional rule-based systems struggle to
detect novel attacks. This project explores whether anomaly detection can
surface suspicious activity without relying on predefined signatures.

---

## Technologies

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Jupyter Notebook

---

## Data Source

Canadian Institute for Cybersecurity (CIC)
CIC-IDS2017 Intrusion Detection Dataset
https://www.unb.ca/cic/datasets/ids-2017.html

MIT License

---

## Dataset

CIC-IDS2017 Intrusion Detection Dataset

The CIC-IDS2017 dataset contains millions of labeled network flow records
representing both benign activity and multiple cyber attack types.

- DoS Hulk
- DoS GoldenEye
- Slowloris
- Slowhttptest
- Heartbleed

Each record represents a network flow with statistical features describing
packet counts, byte rates, durations, and connection behavior.

---

## Repository Contents

attack_detection_model.ipynb – Full notebook containing data preparation,
model training, anomaly detection, and visualizations.

---

## Approach

The project applies an unsupervised anomaly detection approach using
Isolation Forest to identify network flows that deviate from normal behavior.

Steps performed:

1. Load and clean the network flow dataset
2. Train an Isolation Forest model on benign traffic
3. Score all flows based on anomaly likelihood
4. Identify the most suspicious network activity
5. Visualize anomalous flows and suspicious destination ports

---

## Machine Learning Method

### Isolation Forest

Isolation Forest is an unsupervised anomaly detection algorithm that
identifies outliers by randomly partitioning the feature space.

Normal observations require many partitions to isolate, while anomalies
require fewer splits and are therefore detected more quickly.

This method is well-suited for large datasets and situations where
labeled attack data may be limited.

Model configuration used in this project:

- n_estimators: 100
- contamination: 0.01
- random_state: 42

---

## Workflow

1. Data ingestion
2. Data cleaning and preprocessing
3. Feature analysis
4. Isolation Forest model training
5. Anomaly scoring
6. Visualization and investigation

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

## Evaluation

Because the model is unsupervised, anomaly scores were compared against
known attack labels within the dataset to confirm that detected flows
corresponded with malicious activity patterns.

---

Example output from the anomaly detection model:

![Anomaly Detection Example](anomaly_chart.png)

---

## Model Output

The model flagged approximately 1% of network flows as anomalous,
aligning with the contamination parameter used during training.

---

## Results

The Isolation Forest model successfully surfaced network flows that deviated
significantly from normal traffic behavior.

Key observations included:

- Multiple anomalous flows associated with known attack types in the dataset
- Abnormally high connection durations and packet rates
- Concentrated suspicious activity on specific destination ports

---

## Visualizations

The notebook includes visualizations such as:

- Top Suspicious Network Flows
- Suspicious Destination Ports

These visualizations help analysts quickly identify unusual traffic patterns.

---

## Why This Matters

Modern networks generate massive volumes of traffic, making manual
analysis impractical.

Machine learning based anomaly detection can help security analysts
identify suspicious behavior earlier and prioritize investigations
within large network datasets.

---

## Skills Demonstrated

- Data cleaning and preprocessing
- Unsupervised machine learning
- Anomaly detection
- Exploratory data analysis
- Data visualization
- Cybersecurity data analysis

---

## Future Work

Potential improvements include:

- Adding additional feature engineering
- Evaluating supervised classification models
- Investigating temporal attack patterns
- Integrating results with SIEM-style alerts

---

## Quick Start

1. Clone the repository

git clone https://github.com/benderla/network-attack-detection.git

2. Install dependencies

pip install pandas numpy scikit-learn matplotlib

3. Launch the notebook

jupyter notebook attack_detection_model.ipynb

---

## Reproducibility

To reproduce this project:

1. Install Python 3.9+
2. Install required libraries:
   pip install pandas numpy scikit-learn matplotlib

3. Open the notebook:
   attack_detection_model.ipynb

4. Run cells sequentially to load the dataset, train the model,
   and generate anomaly detection visualizations.

---

## Sample Code

```python
from sklearn.ensemble import IsolationForest

model = IsolationForest(
    n_estimators=100,
    contamination=0.01,
    random_state=42
)

model.fit(X_train)
```

---

## Author

Lee