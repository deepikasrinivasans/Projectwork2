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

<img width="1916" height="1007" alt="OS1" src="https://github.com/user-attachments/assets/a2e17a7e-ef5a-49a2-bf8f-c740a7138243" />


2.Normal Load Alert

<img width="1911" height="987" alt="OS2" src="https://github.com/user-attachments/assets/be9dc532-89ee-44ba-8553-a1edd58147cf" />



3.Moderate Risk Alert

<img width="1908" height="996" alt="OS3" src="https://github.com/user-attachments/assets/4c7c546a-3b43-4a42-9c7d-26916de78a61" />


4. High Risk Alert
   
<img width="1912" height="978" alt="OS4" src="https://github.com/user-attachments/assets/c8da353d-1aa6-4dba-a68a-55e6621b32a5" />


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
  


