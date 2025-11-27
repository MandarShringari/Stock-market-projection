import plotly.graph_objects as go
import pandas as pd 
from datetime import datetime 

class Stockdata ():
    def __init__(self):
        self.df = pd.read_csv('file1.csv')
        self.fig = go.Figure(data=[go.Candlestick(x=self.df['Date'],
                             open = self.df['Open'],
                             high = self.df['High'],
                             low = self.df['Low'],
                             close = self.df['Close'])])
        self.fig.show()
Stockdata()
