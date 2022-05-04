import pandas as pd
import plotly.graph_objects as go


class MakeGraph:
    def __init__(self):
        self.result = {}
        # self.df = self.open_csv()

    def check_company_in_cache(self, company_name_symbol):
        df = self.result.get(company_name_symbol, False)
        if not isinstance(df, pd.DataFrame):
            df = self.open_csv(company_name_symbol)
            self.result[company_name_symbol] = df
        return df

    def open_csv(self, company_name_symbol):
        df = pd.read_csv(rf'DWND/{company_name_symbol}.csv')
        return df

    # def get_columns(self):
    #     return self.df.columns.tolist()

    def make_grap_one_column(self, company_symbol, need_column='Close'):
        df = self.check_company_in_cache(company_symbol)
        fig = go.Figure(
            go.Scatter(
                x=df['Date'],
                y=df[need_column]
            )
        )

        fig.update_layout(template='plotly_dark',
                          title=self.title_graph_dict(need_column))
        return fig

    def title_graph_dict(self, title_name):
        dict_names = {
            'Date': 'The date is in the format yy-mm-dd',
            'Open': 'Price of the stock when the market opens',
            'High': 'Highest price reached in the day',
            'Low': 'Lowest price reached in the day',
            'Close': 'Price of the stock when the market closes',
            'Volume': 'Number of shares traded in a day',
            'Dividends': 'The dividends of the stock',
            'Stock Splits': '''The stock splits of the company. In a stock split, a company divides its existing stock 
            into multiple shares to boost liquidity.'''
        }
        return dict_names.get(title_name, 'No title')
