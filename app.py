import pandas as pd
import streamlit as st
import plotly.graph_objects as go
from datetime import datetime
from strategy import moving_average_crossover,validate_data_types
from backtest import display_pl_table,calculate_pnl,plot_winning_losing_percentage


st.title('Moving Average Crossover Strategy')

#little description about the strategy
def describe_strategy():
    st.write("my trading strategy is based on the moving average crossover. "
             "I used a short-term (8-day) and a long-term (20-day) moving average "
             "of the closing prices of the security. When the short-term moving "
             "average crosses above the long-term moving average, we enter a long position. "
             "Conversely, when the short-term moving average crosses below the long-term moving average, "
             "we enter a short position. We hold our position until the next crossover occurs.")

describe_strategy() 

uploaded_file = st.file_uploader('Choose an Excel file', type='xlsx')

if uploaded_file is not None:
    data = pd.read_excel(uploaded_file)

    #data validation fxn
    validate_data_types(data)

    #MA fxn
    data = moving_average_crossover(data)


    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data.index, y=data['close'], mode='lines', name='Price'))
    fig.add_trace(go.Scatter(x=data.index, y=data['8-day MA'], mode='lines', name='8-day MA'))
    fig.add_trace(go.Scatter(x=data.index, y=data['21-day MA'], mode='lines', name='21-day MA'))
    fig.add_trace(go.Scatter(x=data[data['signal']=='buy'].index, y=data[data['signal']=='buy']['close'], mode='markers', name='Buy', marker=dict(color='green', size=10)))
    fig.add_trace(go.Scatter(x=data[data['signal']=='sell'].index, y=data[data['signal']=='sell']['close'], mode='markers', name='Sell', marker=dict(color='red', size=10)))

    fig.update_layout(title='Moving Average Crossover', xaxis_title='Date', yaxis_title='Price')
    st.plotly_chart(fig)

    # Calculating profit and loss
    pnl = calculate_pnl(data)

 
    # Plotting the winning and losing percentages
    plot_winning_losing_percentage(pnl)
