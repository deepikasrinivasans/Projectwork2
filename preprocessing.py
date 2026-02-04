import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

def load_and_prepare_data(path):
    df = pd.read_csv(path)

    df["date_time"] = pd.to_datetime(df["date_time"])
    df.sort_values("date_time", inplace=True)

    # Traffic volume → passenger load proxy
    df["passenger_count"] = (df["traffic_volume"] / 50).astype(int)

    # Time features
    df["hour"] = df["date_time"].dt.hour
    df["day_type"] = np.where(df["date_time"].dt.dayofweek < 5, 1, 0)

    # Event impact
    df["event_impact"] = np.where(df["holiday"] != "None", 0.8, 0.2)

    df = df[[
        "passenger_count",
        "hour",
        "day_type",
        "event_impact"
    ]]

    scaler = MinMaxScaler()
    df["passenger_count_scaled"] = scaler.fit_transform(
        df[["passenger_count"]]
    )

    return df, scaler
