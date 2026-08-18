def get_summary_stats(df):
    # Display decriptive stats and columns information
    import pandas
    display(df.info())
    display(df.describe())
    return None
