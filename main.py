# 1. Install Prophet (if needed)
# Uncomment below in Colab or local if Prophet is not installed
# !pip install prophet

# 2. Import libraries
import pandas as pd
import matplotlib.pyplot as plt
from prophet import Prophet

# 3. Load dataset
df = pd.read_csv('data/sneakers_streetwear_sales_data.csv')

# 4. Parse date column (update 'sale_date' and 'revenue' to match your dataset)
df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values('Date')

# 5. Aggregate monthly sales
monthly_sales = df.groupby(pd.Grouper(key='Date', freq='M'))['Amount ($)'].sum().reset_index()

# 6. Rename columns for Prophet
monthly_sales.columns = ['ds', 'y']

# 7. Initialize and fit the Prophet model
model = Prophet()
model.fit(monthly_sales)

# 8. Create future dates (next 6 months)
future = model.make_future_dataframe(periods=6, freq='M')

# 9. Generate forecast
forecast = model.predict(future)

# 10. Plot forecast
fig1 = model.plot(forecast)
plt.title("Sneaker & Streetwear Sales Forecast")
plt.ylabel("Revenue")
plt.xlabel("Date")
plt.show()

# 11. Optional: Plot components (trend, seasonality)
fig2 = model.plot_components(forecast)
