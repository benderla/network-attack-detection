#!/usr/bin/env python
# coding: utf-8

# # Network Attack Detection using Isolation Forest
# 
# This notebook demonstrates how anomaly detection models can identify
# suspicious network traffic patterns using the CIC-IDS2017 dataset.
# 
# Workflow:
# 1. Load and clean network traffic data
# 2. Train an Isolation Forest anomaly detection model
# 3. Score network flows for anomalous behavior
# 4. Visualize suspicious traffic patterns

# ## 1. Data Loading

# In[ ]:


import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.ensemble import IsolationForest
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.inspection import permutation_importance


# ## 2. Data Cleaning

# In[ ]:


df = pd.read_csv("data/raw.csv", low_memory=False)
df.columns = df.columns.str.strip()

print(df.shape)
df.head()


# ## 3. Feature Preparation

# In[ ]:


df["Attack"] = (df["Label"] != "BENIGN").astype(int)

df["Attack"].value_counts()


# In[ ]:


X = df.drop(columns=["Label", "Attack"])
X = X.select_dtypes(include="number")
X = X.replace([np.inf, -np.inf], np.nan)

y = df["Attack"]

print(X.shape)


# ## 4. Train / Test Split

# In[ ]:


X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

print(X_train.shape)
print(X_test.shape)


# ## 5. Model Training

# ### Isolation Forest Model
# 
# Isolation Forest is an unsupervised anomaly detection algorithm.  
# Instead of learning attack labels, it isolates unusual observations in the dataset.
# 
# Network flows that require fewer splits to isolate in the tree structure  
# are considered more anomalous.

# In[ ]:


model = IsolationForest(
    n_estimators=200,
    contamination=0.01,
    random_state=42,
    n_jobs=-1
)

model.fit(X_train)


# ## 6. Model Interpretation

# ## Model Output Interpretation
# 
# The anomaly detection model assigns scores to each network flow.
# Lower scores indicate flows that deviate more strongly from normal traffic behavior.

# ## Security Interpretation
# 
# The lowest anomaly scores represent network flows that deviate most
# from the baseline learned from benign traffic.
# 
# In an operational security environment these flows would not
# automatically be classified as attacks. Instead they would be
# prioritized for analyst review and correlated with other signals
# such as firewall logs, endpoint activity, or SIEM alerts.
# 
# Anomaly detection helps surface unusual traffic patterns that may
# indicate scanning activity, denial-of-service traffic, or other
# suspicious behavior.

# ## 7. Feature Importance Analysis

# In[ ]:


from sklearn.inspection import permutation_importance
import numpy as np

# Sample a smaller subset for faster computation
X_sample = X_test.sample(10000, random_state=42)
y_sample = y_test.loc[X_sample.index]

# Custom anomaly scoring function
def anomaly_score(estimator, X, y=None):
    return np.mean(estimator.decision_function(X))

result = permutation_importance(
    model,
    X_sample,
    y_sample,
    scoring=anomaly_score,
    n_repeats=5,
    random_state=42,
    n_jobs=-1
)

importance_df = pd.DataFrame({
    "feature": X_test.columns,
    "importance": result.importances_mean
}).sort_values("importance", ascending=False)

importance_df.head(10)


# In[ ]:


import matplotlib.pyplot as plt

# Plot most important features

top_features = importance_df.head(10)

plt.figure(figsize=(10,6))
plt.barh(top_features["feature"], top_features["importance"])
plt.gca().invert_yaxis()

plt.title("Top Network Features Driving Anomaly Detection")
plt.xlabel("Permutation Importance")
plt.ylabel("Feature")

plt.tight_layout()
plt.show()


# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt

df_scores = pd.read_csv("outputs/top_anomalies.csv")

plt.figure(figsize=(10,6))
plt.hist(df_scores["anomaly_score"], bins=50)

plt.title("Distribution of Network Anomaly Scores")
plt.xlabel("Anomaly Score")
plt.ylabel("Count")

plt.show()


# ### Feature Interpretation
# 
# Permutation importance highlights which network flow characteristics most influence anomaly detection.
# 
# Features such as packet counts, flow duration, and packet length statistics often indicate abnormal traffic patterns such as scanning activity, denial-of-service attempts, or unusual communication bursts.
# 
# These indicators help security analysts understand which network behaviors contribute most to suspicious traffic detection.

# ## 8. Visualization

# In[ ]:


# Visualize the most suspicious network flows

import pandas as pd
import matplotlib.pyplot as plt

df_scores = pd.read_csv("outputs/top_anomalies.csv").sort_values("anomaly_score")

df_scores = df_scores.head(20)

plt.figure(figsize=(10,5))
plt.bar(range(1, len(df_scores)+1), df_scores["anomaly_score"])

plt.title("Top Suspicious Network Flows")
plt.xlabel("Flow Rank (Most Suspicious →)")
plt.ylabel("Anomaly Score")

plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.tight_layout()

plt.savefig("outputs/anomaly_chart.png")

plt.show()


# The visualization highlights the network flows with the lowest anomaly scores
# identified by the model. These flows deviate most strongly from the baseline
# behavior learned from benign traffic and may correspond to scanning activity,
# slow HTTP attacks, or denial-of-service patterns present in the dataset.

# In[ ]:


# Analyze destination ports for the most suspicious flows

import pandas as pd
import matplotlib.pyplot as plt

# Load the suspicious flows
df_anomalies = pd.read_csv("outputs/top_anomalies.csv")

# Count destination ports
top_ports = df_anomalies["Destination Port"].value_counts().head(10)

plt.figure(figsize=(10,5))

top_ports.plot(kind="bar")

plt.title("Top Destination Ports in Suspicious Traffic")
plt.xlabel("Destination Port")
plt.ylabel("Number of Suspicious Flows")

plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.tight_layout()

plt.savefig("outputs/anomaly_detection_example.png")

plt.show()


# ### Suspicious Port Analysis
# 
# Analyzing destination ports in anomalous network flows helps identify
# the services potentially targeted by attacks.
# 
# Web ports such as 80 and 443 often appear in denial-of-service attacks
# or slow HTTP attacks (slowloris / slowhttptest) present in the CIC-IDS2017 dataset.
# 
# This analysis helps security analysts quickly understand which network
# services may require investigation.

# ## 9. Model Evaluation Against Known Attacks

# In[ ]:


from sklearn.metrics import classification_report, confusion_matrix

# Convert anomaly predictions to attack prediction
# IsolationForest returns:
# -1 = anomaly
#  1 = normal

df_eval = X_test.copy()
df_eval["actual_attack"] = y_test
df_eval["predicted_anomaly"] = model.predict(X_test)

# Convert to binary attack label
df_eval["predicted_attack"] = (df_eval["predicted_anomaly"] == -1).astype(int)

print("Confusion Matrix")
print(confusion_matrix(df_eval["actual_attack"], df_eval["predicted_attack"]))

print("\nClassification Report")
print(classification_report(df_eval["actual_attack"], df_eval["predicted_attack"]))


# ### Evaluation Interpretation
# 
# Isolation Forest is an unsupervised anomaly detection model.  
# It does not learn attack signatures directly.
# 
# Instead, the model learns baseline patterns of normal network traffic.
# Flows that deviate from these patterns receive lower anomaly scores.
# 
# Evaluation against labeled attack data helps determine whether
# malicious traffic tends to fall into the anomaly region identified
# by the model.

# ## 10. Anomaly Score Distribution by Traffic Type

# In[ ]:


import matplotlib.pyplot as plt

# Combine anomaly scores with labels
df_scores = pd.DataFrame({
    "anomaly_score": model.decision_function(X_test),
    "attack": y_test
})

# Separate benign vs attack traffic
benign_scores = df_scores[df_scores["attack"] == 0]["anomaly_score"]
attack_scores = df_scores[df_scores["attack"] == 1]["anomaly_score"]

plt.figure(figsize=(10,6))

plt.hist(benign_scores, bins=50, alpha=0.6, label="Benign Traffic")
plt.hist(attack_scores, bins=50, alpha=0.6, label="Attack Traffic")

plt.title("Anomaly Score Distribution for Network Traffic")
plt.xlabel("Anomaly Score")
plt.ylabel("Count")

plt.legend()
plt.show()


# ### Security Interpretation
# 
# This visualization compares anomaly scores for benign and malicious network flows.
# 
# Attack traffic tends to receive lower anomaly scores because it deviates
# from the baseline patterns learned from normal network behavior.
# 
# This approach allows security teams to surface previously unseen threats
# without requiring labeled attack signatures.
