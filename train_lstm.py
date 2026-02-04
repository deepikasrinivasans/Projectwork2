import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from preprocessing import load_and_prepare_data

df, scaler = load_and_prepare_data(
    "data/Metro_Interstate_Traffic_Volume.csv"
)

WINDOW = 3
X, y = [], []

for i in range(len(df) - WINDOW):
    X.append(df["passenger_count_scaled"].iloc[i:i+WINDOW].values)
    y.append(df["passenger_count_scaled"].iloc[i+WINDOW])

X = np.array(X).reshape(-1, WINDOW, 1)
y = np.array(y)

model = Sequential([
    LSTM(64, input_shape=(WINDOW, 1)),
    Dense(1)
])

model.compile(optimizer="adam", loss="mse")
model.fit(X, y, epochs=30, batch_size=32)

model.save("lstm_model.keras")
print("✅ Model trained and saved successfully")
