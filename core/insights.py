import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import mean_absolute_percentage_error
from .forecast import forecast_weight

def mood_classifier(df: pd.DataFrame):
    X = df[["weight"]]
    y = df["mood"]
    clf = RandomForestClassifier(max_depth=5, min_samples_leaf=0.1, n_estimators=100)
    clf.fit(X, y)
    return clf

def mape(y_true, y_pred) -> float:
    return mean_absolute_percentage_error(y_true, y_pred)

def generate_insights(df: pd.DataFrame):
    # correlation
    corr = df["weight"].corr(df["mood"], method="spearman")
    # last 14‑day forecast
    fc = forecast_weight(df.rename(columns={"timestamp":"ds","weight":"y"}))[["ds","y"]]
    return {"corr": corr, "forecast": fc}
