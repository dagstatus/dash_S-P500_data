from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import pandas as pd

from base import make_graph, list_companies, base_func


app = Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])


TestClass = make_graph.MakeGraph()
ListCompaniesClass = list_companies.ListCompanies()
BaseClass = base_func.BaseFunc()

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),
    dcc.Dropdown(id='list_companies', options=BaseClass.make_list_to_dropdown(
        ListCompaniesClass.df_companies['Name'].tolist()
    ),
                  clearable=True),
    dcc.Graph(
        id='example-graph',
        figure=TestClass.make_grap_one_column()
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)