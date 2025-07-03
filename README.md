# 🚨 Women Safety Analysis in India (2018)

A **Streamlit dashboard** that visualizes crime statistics affecting women across Indian states using real data from the **National Crime Records Bureau (NCRB) 2018**.



---

## 🔍 Features

- 📊 Visual comparison of states based on women's safety
- 🔢 Safety score based on normalized crime rate
- 🟢 Top 10 safest states and 🔴 riskiest states for women
- 📌 State-wise breakdown: Total cases, victims, and safety score
- 💡 Clean, interactive, and beginner-friendly UI

---

## 📁 Dataset

- Source: National Crime Records Bureau (2018)
- Columns:
  - `State`
  - `Total_Cases`
  - `Total_Victims`
  - `Female_Population`
  - `Cases_per_1000_Females`
  - `Victims_per_1000_Females`
  - `Women_Safety_Score` (calculated using MinMaxScaler)

---

## 🚀 How to Run Locally

### 1. Clone the repo

```bash
git clone https://github.com/Kaur-rav01/women-safety-dashboard.git
cd women-safety-dashboard
