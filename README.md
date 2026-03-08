# network-attack-detection
This project explores how machine learning can be used to detect anomalous network traffic using the CIC-IDS2017 dataset. The goal is to understand behavioral differences between benign traffic and several denial-of-service attacks and evaluate how well machine learning models can identify suspicious flows.

Project Overview
Dataset
Methodology

## Key Observations

During exploration of the CIC-IDS2017 dataset several behavioral
differences between benign and attack traffic were observed.

• Attack flows tend to have significantly longer connection durations.

• Certain attacks generate extremely high packet rates compared
  to normal traffic.

• Average packet size for attack traffic was much larger
  than benign flows.

These patterns make it possible for machine learning models
to distinguish malicious traffic from normal network behavior.

Future Work
