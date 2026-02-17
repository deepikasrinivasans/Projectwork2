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

### 1.System Home Page:
<img width="1918" height="993" alt="public1" src="https://github.com/user-attachments/assets/e1bd3084-acd5-4f9e-80dd-d81c221b3329" />

### 2. Real-Time Dashboard
<img width="1890" height="907" alt="pp2 1" src="https://github.com/user-attachments/assets/fb3a9758-cdfd-4703-87a4-031e28a68e05" />

### 3.Live Bus Tracking Map
<img width="1882" height="686" alt="pp4" src="https://github.com/user-attachments/assets/b17017c1-7e4b-4f39-99bb-436b3f50c5f0" />

### 4. AI Prediction & Passenger Trend graph
<img width="1915" height="712" alt="public 4" src="https://github.com/user-attachments/assets/c3092d04-ac39-467a-a706-03aec92797c0" />

### 5. Alert & Dispatch Recommendation
<img width="1903" height="993" alt="public 5" src="https://github.com/user-attachments/assets/d2d72cff-6699-4b91-9a91-db8d67cee808" />





## 9.How the System Works (Operational Flow)

1. Recent passenger counts are received (simulated sensor input)
2. The AI model predicts near-future passenger load
3. Prediction is stabilized using recent observations
4. Crowding risk and waiting time are computed
5. Visual alerts and recommendations are generated for operators



## 10.Technologies Used

* **Programming Language:** Python
* **Machine Learning:** TensorFlow / Keras
* **Data Processing:** Pandas, NumPy
* **Visualization & UI:** Streamlit, Matplotlib
* **Dataset Source:** UCI Machine Learning Repository
  
## 11.Results & Observations

* The system successfully identifies **rising congestion trends**
* Moderate and high-risk conditions are detected **before overcrowding occurs**
* Prediction stabilization significantly reduces false alarms
* Visual indicators improve interpretability and response readiness

> The results demonstrate the feasibility of AI-assisted proactive transport management.

## 12.Future Enhancements

* Integration with live passenger counting sensors (CCTV, IR, smart ticketing)
* City-wide multi-route modeling
* Reinforcement learning for scheduling optimization
* Mobile app integration for passenger notifications
* Cloud deployment for real-time scalability
  


