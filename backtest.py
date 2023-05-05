import pandas as pd
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px

# Calculate profit and loss
def calculate_pnl(data):
    pnl = []
    position = None
    entry_price = None
    for i, row in data.iterrows():
        if row['signal'] == 'buy':
            position = 'Long'
            entry_price = row['close']
        elif row['signal'] == 'sell':
            position = 'Short'
            pnl.append(row['close'] - entry_price if position == 'Long' else entry_price - row['close'])
            entry_price = None
            position = None
    
    return pnl


#checking winning and loosing streaks
def plot_winning_losing_percentage(pnl):
    # Calculate winning and losing percentages
    winning_trades = sum(pl > 0 for pl in pnl)
    losing_trades = sum(pl < 0 for pl in pnl)
    total_trades = len(pnl)
    winning_percentage = (winning_trades / total_trades) * 100 if total_trades > 0 else 0
    losing_percentage = (losing_trades / total_trades) * 100 if total_trades > 0 else 0

    # Create a data frame for the percentages
    data = {
        'type': ['Winning Trades', 'losing Trades'],
        'percentage': [winning_percentage, losing_percentage]
    }
    df = pd.DataFrame(data)

    # chart
    fig = px.pie(df, names='type', values='percentage', title='Winning and Losing Trades Percentage')

    
    st.plotly_chart(fig)
