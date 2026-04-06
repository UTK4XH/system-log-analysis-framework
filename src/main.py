from log_parser import load_logs
from analyzer import count_errors, find_error_patterns, detect_anomalies, plot_errors


def main():
    # Load log data
    df = load_logs("../logs/sample_logs.csv")

    # Total error count
    total_errors = count_errors(df)
    print(f"Total Errors: {total_errors}")

    # Error patterns
    error_patterns = find_error_patterns(df)
    print("\nError Patterns:\n", error_patterns)

    # Warnings (anomalies)
    warnings = detect_anomalies(df)
    print("\nWarnings:\n", warnings)

    # Plot graph
    plot_errors(error_patterns)


if __name__ == "__main__":
    main()
