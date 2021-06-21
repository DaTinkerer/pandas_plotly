import json
import pandas as pd
import plotly.graph_objects as go
import requests
from secrets import key

r = requests.get(f'https://api.twelvedata.com/time_series?&interval=4h&apikey={key}&outputsize=500&symbol=nvda')
res = r.json()

df = pd.json_normalize(res, 'values')
symbol = res['meta']['symbol']
    
    
fig = go.Figure(data=[go.Candlestick(x=df['datetime'],
                    open=df['open'],
                    high=df['high'],
                    low=df['low'],
                    close=df['close'])])
df = df.iloc[::-1]
fig.update_xaxes(
    rangebreaks=[

        dict(bounds=["sat", "mon"]), #hide weekends
        dict(bounds=[16, 9.5], pattern="hour"),  # hide hours outside of 9.30am-4pm

        ]
    )
fig.update_layout(xaxis_rangeslider_visible=False, template="plotly_dark",
                yaxis_title="Price (USD)", xaxis_title="Date", title=symbol)
fig.show()