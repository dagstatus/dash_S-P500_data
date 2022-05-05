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
    html.Div(children=[
        dcc.Dropdown(id='list_companies', options=BaseClass.make_list_to_dropdown(
            ListCompaniesClass.df_companies['Name'].tolist(),
            ListCompaniesClass.df_companies['Symbol'].tolist()
        ), clearable=True, placeholder='Select company')],
        style={"width": "45%", 'display': 'inline-block'},
    ),
    html.Div(children=[
        dcc.Dropdown(id='list_columns',
                     options=BaseClass.make_list_to_dropdown(
                         ['No columns'], [False]
                     ),
                     clearable=True,
                     multi=True,
                     placeholder='Select columns',
                     # value=False,
                     disabled=True)
    ], style={"width": "45%", 'display': 'inline-block'}
    ),
    html.Div(children=[
        dcc.Graph(
            id='graph_need_columns'
        )],
        style={"width": "100%"}
    )
])


@app.callback(Output('list_columns', 'options'),
              Output('list_columns', 'disabled'),
              Input('list_companies', 'value'))
def update_list_columns(company_name_symb):
    if not company_name_symb:
        return BaseClass.make_list_to_dropdown(['No columns'], [False]), True
    else:
        return BaseClass.make_list_to_dropdown(
            BaseClass.get_columns(
                GraphClass.check_company_in_cache(company_name_symb)),
            BaseClass.get_columns(
                GraphClass.check_company_in_cache(company_name_symb))
        ), False


@app.callback(
    Output('graph_need_columns', 'figure'),
    State('list_companies', 'value'),
    Input('list_columns', 'value')
)
def make_graph(company_name_symb, columns_names):
    if columns_names:
        return GraphClass.make_grap_columns(company_name_symb, columns_names)
    else:
        fig = go.Figure()
        fig.update_layout(template='plotly_dark')
        return fig


if __name__ == '__main__':
    app.run_server(debug=False)
