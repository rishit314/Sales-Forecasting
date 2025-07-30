# 🧾 Sales Forecasting for Streetwear & Sneakers

This project uses historical sales data from a sneakers and streetwear dataset to forecast monthly revenue using **Facebook Prophet**, a robust time series modeling tool. It demonstrates an end-to-end data science pipeline — from preprocessing and aggregation to modeling and visualization.

---

## 📈 Project Goals

- Forecast future monthly sales revenue
- Identify seasonal trends and patterns
- Build an interpretable and deployable forecasting model

---

## 📦 Dataset

- **Name**: `sneakers_streetwear_sales_data.csv`
- **Columns** (assumed):
  - `Date`: Date of transaction
  - `Amount($)`: Total revenue for each transaction


## 🛠 Tech Stack

- Python 3.x  
- [Prophet (by Meta)](https://facebook.github.io/prophet/)
- Pandas, Matplotlib

---

## 🔍 Exploratory Steps

1. Loaded and cleaned the dataset
2. Aggregated daily transactions into **monthly revenue**
3. Visualized overall sales trends

---

## 📉 Forecasting Method

We used **Facebook Prophet** to:
- Model yearly seasonality
- Forecast revenue for the next 6 months
- Visualize trends and components (trend, seasonality, etc.)

---

## 📊 Results

- Accurate forecasts of revenue with confidence intervals
- Clear visualization of trend and seasonal components
- Business-friendly insights into expected growth/decline periods

![Forecast Plot](./images/forecast.png)

---

## 🗃️ Folder Structure

project/
│
├── data 
    └── sneakers_streetwear_sales_data.csv
├── main.py # Main notebook
├── README.md

yaml
Copy
Edit

---

## 🚀 Future Improvements

- Incorporate external regressors (e.g., holidays, promotions)
- Use product-level forecasts (instead of total revenue)
- Compare Prophet to LSTM, ARIMA, and XGBoost models

---

## 🧠 Author

**Rishit Mishra**
[My GitHub Profile](https://github.com/rishit314)

