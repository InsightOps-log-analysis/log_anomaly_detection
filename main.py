from src.preprocessing import load_data, clean_data
from src.anomaly_detection import detect_anomalies
from src.visualization import plot_anomalies

def main():
    # Load and preprocess data
    data = load_data('data/raw/sample_logs.csv')
    cleaned_data = clean_data(data)
    
    # Detect anomalies
    anomalies = detect_anomalies(cleaned_data[['feature1', 'feature2']])
    
    # Add anomaly results to the DataFrame
    cleaned_data['anomaly'] = anomalies

    # Print detected anomalies
    print("Detected Anomalies:")
    print(cleaned_data[cleaned_data['anomaly'] == -1])
    
    # Plot anomalies
    plot_anomalies(cleaned_data)

if __name__ == "__main__":
    main()
