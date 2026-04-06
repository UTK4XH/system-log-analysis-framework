import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt

def count_errors(df):
    """
    Returns total number of ERROR logs.
    """
    return df[df['level'] == 'ERROR'].shape[0]


def find_error_patterns(df):
    """
    Returns frequency of each error message.
    """
    return df[df['level'] == 'ERROR']['message'].value_counts()


def detect_anomalies(df):
    """
    Returns all WARNING logs (treated as anomalies).
    """
    return df[df['level'] == 'WARN']


def plot_errors(error_counts):
    """
    Plots error frequency as a bar chart.
    """
    if error_counts.empty:
        print("No errors to plot.")
        return

    error_counts.plot(kind='bar')
    plt.title("Error Frequency")
    plt.xlabel("Error Type")
    plt.ylabel("Count")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
