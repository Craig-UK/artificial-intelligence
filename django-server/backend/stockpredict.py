import numpy as np, numpy.random
import pandas as pd
import datetime as dt
import yfinance as yf
yf.pdr_override()
from pandas_datareader import data as web
from prophet import Prophet

def CalcWeights(emotion: str, sentiment: str):
    emotion_dict = {
        "Angry": 4,
        "Disgust": 5,
        "Fear": 6,
        "Happy": 10,
        "Neutral": 8,
        "Sad": 7,
        "Surprised": 9 
    }

    sentiment_dict = {
        "Extremely negative": -4,
        "Very negative": -3,
        "Negative": -2,
        "Slightly negative": -1,
        "Neutral": 0,
        "Slightly positive": 1,
        "Positive": 2,
        "Very positive": 3,
        "Extremely positive": 4 
    }

    res = emotion_dict[emotion] + sentiment_dict[sentiment]

    if res < 0:
        res = 0
    
    if res > 12:
        res = 12

    print(res)

    return res - 1




def Predict(ticker: str, emotion: str, sentiment: str):

    start = dt.datetime(2020, 1, 1)
    end = dt.datetime.now()

    increment = [-48, -40, -32, -24, -16, -8, 8, 16, 24, 32, 40, 48]

    # Write alogirthm here

    index_inc = CalcWeights(emotion=emotion, sentiment=sentiment)

    print(index_inc)

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
        #value *= 16 # value *= increment[RESULT FROM ALGORITHM]
        value *= increment[index_inc]

        values = np.sort(value[1])
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