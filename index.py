from dash import Dash, html, dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate
import plotly.graph_objects as go
import pandas as pd

from base import make_graph, list_companies, base_func

app = Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])

GraphClass = make_graph.MakeGraph()
ListCompaniesClass = list_companies.ListCompanies()
BaseClass = base_func.BaseFunc()

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),
    dcc.Dropdown(id='list_companies', options=BaseClass.make_list_to_dropdown(
        ListCompaniesClass.df_companies['Name'].tolist(),
        ListCompaniesClass.df_companies['Symbol'].tolist()
    ),
                 clearable=True),
    dcc.Graph(
        id='graph_close_price'
    )
])


@app.callback(Output('graph_close_price', 'figure'),
              Input('list_companies', 'value'))
def update_figure(company_name_symb):
    if company_name_symb:
        return GraphClass.make_grap_one_column(company_name_symb, 'Close')
    else:
        fig = go.Figure()
        fig.update_layout(template='plotly_dark')
        return fig


if __name__ == '__main__':
    app.run_server(debug=True)
