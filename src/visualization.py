import matplotlib.pyplot as plt

def plot_anomalies(df):
    """Plot the data points and highlight anomalies."""
    plt.figure(figsize=(12, 6))
    plt.scatter(df['timestamp'], df['feature1'], c=df['anomaly'], cmap='coolwarm', label='Anomalies')
    plt.xlabel('Timestamp')
    plt.ylabel('Feature 1')
    plt.title('Log Anomalies Detection')
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
