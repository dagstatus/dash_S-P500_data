import pandas as pd
import plotly.graph_objects as go

class MakeGraph:
    def __init__(self):
        self.result = None
        self.df = self.open_csv()

    def open_csv(self):
        df = pd.read_csv(r'DWND/A.csv')
        return df

    def get_columns(self):
        return self.df.columns.tolist()

    def make_grap_one_column(self, need_column='Close'):
        fig = go.Figure(
            go.Scatter(
                x=self.df['Date'],
                y=self.df[need_column]
            )
        )

        fig.update_layout(template='plotly_dark')
        return fig
