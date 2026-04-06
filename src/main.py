from log_parser import load_logs
from analyzer import count_errors, find_error_patterns, detect_anomalies, plot_errors

def main():
    df = load_logs("../logs/sample_logs.csv")

    total_errors = count_errors(df)
    print(f"Total Errors: {total_errors}")

    error_patterns = find_error_patterns(df)
    print("\nError Patterns:\n", error_patterns)

    warnings = detect_anomalies(df)
    print("\nWarnings:\n", warnings)

    # 🔥 ADD THIS LINE (IMPORTANT)
    plot_errors(error_patterns)

if __name__ == "__main__":
    main()
