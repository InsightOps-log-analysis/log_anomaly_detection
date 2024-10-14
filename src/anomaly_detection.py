from sklearn.ensemble import IsolationForest

def detect_anomalies(data):
    """Detect anomalies in the dataset using Isolation Forest."""
    model = IsolationForest(contamination=0.5)
    
      # Adjust contamination as needed
    model.fit(data)
    anomalies = model.predict(data)
    return anomalies
