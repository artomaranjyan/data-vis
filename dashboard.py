from dash import Dash, dcc, html, Input, Output
import numpy as np
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import plotly.figure_factory as ff

external_stylesheets = [
    'https://codepen.io/chriddyp/pen/bWLwgP.css',
    {
        'href': 'https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css',
        'rel': 'stylesheet',
        'integrity': 'sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO',
        'crossorigin': 'anonymous'
    }
]


app = Dash(external_stylesheets = external_stylesheets)

app.layout = html.Div([
    html.A("Human Resources Data Set", href='https://www.kaggle.com/datasets/rhuebner/human-resources-data-set'),
    html.Br(),
    html.A("GitHub", href='https://github.com/artomaranjyan/ysu-data-vis'),
    
    html.Div([
        html.Div([dcc.Graph(id = 'hist')], className='six columns'),
        html.Div([dcc.Graph(id = 'violin')], className='six columns')],
    className='row'),
    
    html.Br(),
    
    html.Div([
        html.Div([dcc.Dropdown(id = 'hist_x', placeholder="x = None", 
                               options = [
                                          {'label': 'x = Sex', 'value': 'Sex'},
                                          {'label': 'x = Salary', 'value': 'Salary'},
                                          {'label': 'x = Position', 'value': 'Position'},
                                          {'label': 'x = Department', 'value': 'Department'},
                                          {'label': 'x = MaritalDesc', 'value': 'MaritalDesc'},
                                          {'label': 'x = CitizenDesc', 'value': 'CitizenDesc'},
                                          {'label': 'x = PerformanceScore', 'value': 'PerformanceScore'},
                                         ],
                               value='Department')], className = 'two columns'),
        html.Div([dcc.Dropdown(id = 'hist_y', placeholder="y = None", 
                               options = [
                                          {'label': 'y = Salary', 'value': 'Salary'},
                                          {'label': 'y = Absences', 'value': 'Absences'},                                   
                                          {'label': 'y = EmpSatisfaction', 'value': 'EmpSatisfaction'},
                                          {'label': 'y = SpecialProjectsCount', 'value': 'SpecialProjectsCount'},
                                         ], 
                               value='Salary')], className = 'two columns'),
        html.Div([dcc.Dropdown(id = 'hist_color', placeholder="color = None", 
                               options = [
                                          {'label': 'color = Sex', 'value': 'Sex'},
                                          {'label': 'color = RaceDesc', 'value': 'RaceDesc'},
                                          {'label': 'color = MaritalDesc', 'value': 'MaritalDesc'},
                                          {'label': 'color = CitizenDesc', 'value': 'CitizenDesc'},
                                          {'label': 'color = HispanicLatino', 'value': 'HispanicLatino'},
                                          {'label': 'color = PerformanceScore', 'value': 'PerformanceScore'},
                                         ], 
                               value='Sex')], className = 'two columns'),
        html.Div(className='one column'),
        html.Div([dcc.Dropdown(id = 'violin_y', placeholder="y = None", 
                               options = [
                                          {'label': 'y = Salary', 'value': 'Salary'},
                                          {'label': 'y = Absences', 'value': 'Absences'},
                                          {'label': 'y = EmpSatisfaction', 'value': 'EmpSatisfaction'},
                                          {'label': 'y = SpecialProjectsCount', 'value': 'SpecialProjectsCount'},
                                         ], 
                               value='Salary')], className = 'two columns'),
        html.Div([dcc.Dropdown(id = 'violin_x', placeholder="x = None", 
                               options = [
                                          {'label': 'x = Sex', 'value': 'Sex'},
                                          {'label': 'x = Salary', 'value': 'Salary'},
                                          {'label': 'x = Position', 'value': 'Position'},
                                          {'label': 'x = Department', 'value': 'Department'},
                                          {'label': 'x = MaritalDesc', 'value': 'MaritalDesc'},
                                          {'label': 'x = CitizenDesc', 'value': 'CitizenDesc'},
                                          {'label': 'x = PerformanceScore', 'value': 'PerformanceScore'},
                                         ], 
                               value='PerformanceScore')], className = 'two columns')], 
    className='row'),

    html.Br(),
    
    html.Div([
        html.Div([dcc.Dropdown(id = 'hist_barmode', placeholder="barmode = relative", 
                               options = [
                                          {'label': 'barmode = relative', 'value': 'relative'},
                                          {'label': 'barmode = group', 'value': 'group'}
                                         ], 
                               value='group')], className = 'two columns'),
        html.Div([dcc.Dropdown(id = 'hist_func', placeholder="histfunc = None", 
                               options = [
                                          {'label': 'histfunc = avg', 'value': 'avg'},
                                         ], 
                               value='avg')], className = 'two columns'),
        html.Div([dcc.Checklist(id = 'hist_logy', 
                                options=[
                                         {'label':' log_y', 'value': '1'},
                                        ], 
                                value = [])], className = 'two columns'),
        html.Div(className='one column'),
        html.Div([dcc.Dropdown(id = 'violin_color', placeholder="color = None", 
                               options = [
                                          {'label': 'color = Sex', 'value': 'Sex'},
                                          {'label': 'color = RaceDesc', 'value': 'RaceDesc'},
                                          {'label': 'color = MaritalDesc', 'value': 'MaritalDesc'},
                                          {'label': 'color = CitizenDesc', 'value': 'CitizenDesc'},
                                          {'label': 'color = HispanicLatino', 'value': 'HispanicLatino'},
                                          {'label': 'color = PerformanceScore', 'value': 'PerformanceScore'},
                                         ], 
                               value='Sex')], className = 'two columns'),
        html.Div([dcc.Checklist(id = 'violin_box', 
                                options=[
                                         {'label':' box', 'value': '1'}
                                        ], 
                                value = ['1'])], className = 'one column'),
        html.Div([dcc.Checklist(id = 'violin_points', 
                                options=[
                                         {'label':' points', 'value': 'all'}
                                        ], 
                                value = [])], className = 'one column')], 
    className = 'row'),
],
className = 'container')


df = pd.read_csv('data.csv')

@app.callback(
    Output("hist", "figure"), 
    Input("hist_x", "value"),
    Input("hist_y", "value"),
    Input("hist_color", "value"),
    Input("hist_barmode", "value"),
    Input("hist_func", "value"),
    Input("hist_logy", "value")
)
def update_hist(hist_x, hist_y, hist_color, hist_barmode, hist_func, hist_logy):
    return px.histogram(df, x=hist_x, y=hist_y, color=hist_color, barmode=hist_barmode, histfunc=hist_func, log_y = bool(hist_logy)) 

    
@app.callback(
    Output("violin", "figure"), 
    Input("violin_y", "value"),
    Input("violin_x", "value"),
    Input("violin_color", "value"),
    Input("violin_box", "value"),
    Input("violin_points", "value"),
)
def update_violin(violin_y, violin_x, violin_color, violin_box, violin_points):
    if not violin_points:
        violin_points = [False]
        
    return px.violin(df, y=violin_y, x=violin_x, color=violin_color, box=bool(violin_box), points=violin_points[0])

if __name__ == "__main__":
    app.run_server(debug=True)
