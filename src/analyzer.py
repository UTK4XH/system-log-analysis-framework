def count_errors(df):
    return df[df['level'] == 'ERROR'].shape[0]

def find_error_patterns(df):
    return df[df['level'] == 'ERROR']['message'].value_counts()

def detect_anomalies(df):
    return df[df['level'] == 'WARN']