from log_parser import load_logs
from analyzer import count_errors, find_error_patterns, detect_anomalies

def main():
    df = load_logs(r"C:\Users\UTK4XH\OneDrive\Desktop\system-log-analysis-framework\logs\sample_logs.csv")

    print("Total Errors:", count_errors(df))
    print("\nError Patterns:\n", find_error_patterns(df))
    print("\nWarnings:\n", detect_anomalies(df))

if __name__ == "__main__":
    main()