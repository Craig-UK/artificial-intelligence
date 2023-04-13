import numpy as np, numpy.random
import pandas as pd
import datetime as dt
import yfinance as yf
yf.pdr_override()
from pandas_datareader import data as web
from prophet import Prophet

def Predict(ticker: str):

    start = dt.datetime(2020, 1, 1)
    end = dt.datetime.now()

    try:
        data = web.get_data_yahoo(ticker.upper(), start, end)

        data.to_csv("stock_data.csv")
        data = pd.read_csv("stock_data.csv")
        data = data[["Date", "Close"]]
        data.columns = ["ds", "y"]
        prophet = Prophet(daily_seasonality=True)
        prophet.fit(data)
        future_dates = prophet.make_future_dataframe(periods=30)
        predictions = prophet.predict(future_dates)
        pred_month = predictions["yhat"][-30:]
        old_arr = []
        full_arr = []
        for x in pred_month:
            old_arr.append(x)
        for x in predictions["yhat"][-120:]:
            full_arr.append(x)
        value = np.random.dirichlet((2, 16), 30).transpose()
        value *= 16

        values = np.sort(value[0])
        same_one = []

        for i,x in enumerate(pred_month):
            if i == 0:
                same_one.append(x)
            else:
                same_one.append(x + values[i])
        original_values = full_arr.copy()
        full_arr[-30:] = same_one

        return original_values, full_arr
    except:
        return "Invalid Ticker"