import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import plotly.figure_factory as ff

df = pd.read_csv('data.csv')

def hist(x, y=None, color=None, barmode='relative', histfunc=None, nbins=None, log_y=False):
    return px.histogram(df, x=x, y=y, color=color, barmode=barmode, histfunc=histfunc, nbins=nbins, log_y=log_y) 

def violin(y, x=None, color=None, box=True, points="all"):
    return px.violin(df, y=y, x=x, color=color, box=box, points=points)