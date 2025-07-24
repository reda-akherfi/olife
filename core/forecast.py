import pandas as pd
from statsforecast import StatsForecast
from statsforecast.models import AutoARIMA

def forecast_weight(df: pd.DataFrame, horizon: int = 14):
    """
    df: DataFrame with columns ['ds','y']  ('ds' datetime, 'y' float)
    returns df_forecast with 'ds' future dates and 'y' prediction
    """
    sf = StatsForecast([AutoARIMA(season_length=7)], freq="D")
    return sf.forecast(df, h=horizon)
