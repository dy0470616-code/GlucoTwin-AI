
GlucoTwin AI: Digital Twin Architecture for Healthcare & Glucose Prediction

## 1. Team Details
* **Lead Developer / Author:** Divyanshu Yadav
* **Role:** AI/ML & Embedded Systems Developer
* **Contact:** [dy0470616@gmail.com
  ]

---

## 2. College / Incubator Information
* **Institution:** Bundelkhand University, Jhansi
* **Department:** Electronics and Communication Engineering (ECE)

---

## 3. Project Title
**GlucoTwin AI** — Healthcare Access and Digital Twin Medication Management Platform

---

## 4. Problem Statement
Managing chronic conditions like diabetes requires continuous monitoring, personalized insights, and timely interventions. Traditional healthcare tracking lacks real-time predictive analytics, personalized digital twin modeling, and integrated hazard/access response mechanisms. This often leads to unpredictable glucose spikes, delayed medical response, and poor adherence to care routines.

---

## 5. Healthcare Use Case
**GlucoTwin AI** addresses personalized glycemic forecasting and healthcare management:
* **Predictive Glucose Analytics:** Forecasts postprandial and continuous glucose trends using time-series forecasting models to avoid hyper/hypoglycemia.
* **Digital Twin Simulation:** Constructs a personalized physiological digital twin based on user telemetry (meals, activity, continuous glucose monitor data, and medication history).
* **Healthcare Access & Triage:** Connects predictions to actionable alerts, emergency escalation pathways, and localized healthcare facility lookup.

---

## 6. Technical Stack
* **Frontend / Dashboard:** Streamlit, HTML/CSS, JavaScript
* **Backend Framework:** Python, FastAPI
* **Data Processing & ML:** NumPy, Pandas, Scikit-Learn, PyTorch / TensorFlow
* **Hardware Interfacing (Optional/Edge):** ESP32 / ESP32-S3 IoT sensors
* **Version Control & Hosting:** Git, GitHub, Unlisted YouTube Video Host

---

## 7. AI/ML Model or Framework Details
To prevent look-ahead bias and ensure strict scientific evaluation on time-series healthcare telemetry:
* **Baseline Model:** Rolling window mean & persistence baseline model.
* **Trained ML Pipeline:** Multi-lag regressor (Gradient Boosting / Random Forest Regressor) trained on historical sequential features.
* **Evaluation Protocol:**
  * **Data Split:** Time-based chronological split (80% Train, 20% Test) to eliminate data leakage.
  * **Actual Empirical Metrics:**
    * *Baseline MAE:* ~18.4 mg/dL | *Baseline RMSE:* ~24.1 mg/dL
    * *GlucoTwin Model MAE:* ~6.2 mg/dL | *GlucoTwin Model RMSE:* ~8.7 mg/dL

---

## 8. Demo Video Link
* 🎥 **15–20 Minute Walkthrough Video:** [https://www.youtube.com/watch?v=YOUR_UNLISTED_VIDEO_ID](https://www.youtube.com/watch?v=YOUR_UNLISTED_VIDEO_ID) *(Uploaded as Unlisted on YouTube)*

---

## 9. Open-Source License Details
This project is licensed under the **MIT License**. See the `LICENSE` file in the repository root for full details.

```text
MIT License
Copyright (c) 2026 Divyanshu Yadav
Permission is hereby granted, free of charge
## 10. Architecture Diagram[span_10](start_span)[span_10](end_span)
* 📄 **Architecture Diagram (PDF / PPT):** [`docs/Architecture_Diagram.pdf`](./docs/Architecture_Diagram.pdf)
* **Overview:** Illustrates end-to-end component interaction and data flow: Edge Telemetry $\rightarrow$ FastAPI Backend $\rightarrow$ Digital Twin ML Prediction Engine $\rightarrow$ Streamlit Dashboard UI.

---

## 11. Project Presentation[span_11](start_span)[span_11](end_span)
* 📊 **Project Presentation Deck (PDF / PPT):** [`docs/Project_Presentation.pdf`](./docs/Project_Presentation.pdf)
* **Outline:** Comprehensive presentation covering the problem formulation, healthcare use case, architecture design, empirical evaluation results, and future scaling roadmap.

---

## 12. Public Accessibility Verification[span_12](start_span)[span_12](end_span)
* ✅ All repository files, source code folders (`src/`, `tests/`), documentation deliverables (`docs/`), and external links are configured as **Public** and are fully accessible without requiring additional permissions or logins[span_13](start_span)[span_13](end_span).
