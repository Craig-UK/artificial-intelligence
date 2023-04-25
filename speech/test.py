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
        res == 0
    elif res > 12:
        res == 12

    print(res)

CalcWeights(emotion="Angry", sentiment="Negative")