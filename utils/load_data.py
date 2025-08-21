import pandas as pd
import os

def load_daily_csv(date_str):
    file_path = f"data/insights_{date_str}.csv"
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"CSV not found for {date_str}")
    df = pd.read_csv(file_path)
    return df

