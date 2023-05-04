import pandas as pd
import streamlit as st
import plotly.graph_objects as go
from datetime import datetime

#changing the datatypes in the case where the datatypes are not in the right format
def validate_data_types(df):
    try:
        df[['open', 'high', 'low', 'close']] = df[['open', 'high', 'low', 'close']].astype(float)
        df['volume'] = df['volume'].astype(int)
        df['datetime'] = pd.to_datetime(df['datetime'])
        df['instrument'] = df['instrument'].astype(str)
        df.set_index('datetime', inplace=True)
    except Exception as e:
        st.error(f"Error: {e}")
        st.stop()

#moving average crossover
def moving_average_crossover(data):
    data['8-day MA'] = data['close'].rolling(window=8).mean()
    data['21-day MA'] = data['close'].rolling(window=21).mean()
    data['signal'] = 'hold'
    data.loc[(data['8-day MA'] > data['21-day MA']) & (data['8-day MA'].shift() < data['21-day MA'].shift()), 'signal'] = 'buy'
    data.loc[(data['8-day MA'] < data['21-day MA']) & (data['8-day MA'].shift() > data['21-day MA'].shift()), 'signal'] = 'sell'
    return data
