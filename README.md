# Real-Time AI-Driven Prediction of Public Transport Overcrowding

### Proactive Service Optimization Using Short-Horizon Forecasting

## 1.Project Overview

Urban public transport systems frequently experience sudden passenger surges, leading to **overcrowding**, **long waiting times**, **passenger discomfort**, and **operational inefficiencies**. Most existing systems rely on **reactive responses** or **long-term demand forecasting**, which are insufficient to prevent short-term congestion.

This project presents a **real-time AI-driven decision-support framework** that predicts **imminent overcrowding (10–15 minutes ahead)** using recent passenger trends and generates **actionable alerts** for transport operators to proactively manage resources.

The system is designed as a **research-oriented prototype**, emphasizing **prediction accuracy, interpretability, and operational realism**.


## 2.Objectives

* Predict short-term passenger load using AI
* Identify **pre-overcrowding conditions** before congestion occurs
* Classify risk levels (Normal / Moderate / High)
* Estimate passenger waiting time
* Provide **operator-oriented alerts and visual decision support**
* Demonstrate a scalable architecture for smart transport systems


## 3.Key Features

* **LSTM-based short-horizon prediction** (10–15 minutes ahead)
* **Crowding Risk Score** based on predicted load and vehicle capacity
* **Blended decision logic** to reduce false alarms
* **Single-screen interactive dashboard**
* **Trend visualization with annotated values**
* **Animated capacity utilization indicator**
* **Operator alert recommendations (decision support, not control)**


## 4.System Architecture

```
Passenger Data (Simulated Real-Time)
        ↓
Data Preprocessing & Normalization
        ↓
LSTM Prediction Model
        ↓
Prediction Stabilization (Blending)
        ↓
Crowding Risk Assessment
        ↓
Waiting Time Estimation
        ↓
Dashboard Visualization & Operator Alerts
```


## 5.Dataset Used

**Primary Dataset:**
Metro Interstate Traffic Volume Dataset
Source: UCI Machine Learning Repository

* Contains traffic volume, time, weather, and holiday information
* Traffic volume is used as a **proxy for passenger demand**
* Real-time behavior is simulated using **sequential time-series replay**

This simulation-based approach is widely adopted in intelligent transportation system research when live sensor data is unavailable.


## 6.Machine Learning Model

* **Model Type:** Long Short-Term Memory (LSTM)
* **Input:** Passenger counts from recent time intervals
* **Output:** Predicted passenger load for the next 10–15 minutes
* **Training:** Historical data with normalization
* **Loss Function:** Mean Squared Error (MSE)

To improve operational reliability, the raw AI prediction is combined with recent observations using a **weighted blending strategy**, reducing prediction spikes and false high-risk alerts.


## 7.Risk Classification Logic

Crowding risk is calculated as:

```
Risk = Effective Passenger Load / Vehicle Capacity
```

| Risk Level | Description                                         |
| ---------- | --------------------------------------------------- |
| Normal     | Load within safe operating capacity                 |
| Moderate   | Rising load; congestion likely if trend continues   |
| High       | Overcrowding imminent; proactive action recommended |



## 8.Dashboard Overview

The Streamlit-based dashboard provides:

* Recent passenger trend visualization
* Predicted future load
* Risk level indicators
* Estimated waiting time
* Capacity utilization bar
* Animated bus indicator for intuitive understanding

The dashboard is designed to fit on a **single screen**, making it suitable for **control-room-style monitoring**.

1.Dashboard

<img width="1147" height="564" alt="image" src="https://github.com/user-attachments/assets/f111f360-2df7-4e36-bda3-676ef08b7e53" />

2.Normal Load Alert

<img width="1120" height="557" alt="image" src="https://github.com/user-attachments/assets/31609d2a-e1e4-4cc1-b8c4-1e3f7e6cc9a8" />

3.High Risk Alert

<img width="1146" height="558" alt="image" src="https://github.com/user-attachments/assets/fb18fcfe-b3ed-4b1a-99ce-11f89a4ef6b0" />


## 9.How the System Works (Operational Flow)

1. Recent passenger counts are received (simulated sensor input)
2. The AI model predicts near-future passenger load
3. Prediction is stabilized using recent observations
4. Crowding risk and waiting time are computed
5. Visual alerts and recommendations are generated for operators


## 10.Results & Observations

* The system successfully identifies **rising congestion trends**
* Moderate and high-risk conditions are detected **before overcrowding occurs**
* Prediction stabilization significantly reduces false alarms
* Visual indicators improve interpretability and response readiness

> The results demonstrate the feasibility of AI-assisted proactive transport management.



## 11.Technologies Used

* **Programming Language:** Python
* **Machine Learning:** TensorFlow / Keras
* **Data Processing:** Pandas, NumPy
* **Visualization & UI:** Streamlit, Matplotlib
* **Dataset Source:** UCI Machine Learning Repository


## 12.Future Enhancements

* Integration with live passenger counting sensors (CCTV, IR, smart ticketing)
* City-wide multi-route modeling
* Reinforcement learning for scheduling optimization
* Mobile app integration for passenger notifications
* Cloud deployment for real-time scalability


