import pandas as pd

class ListCompanies:
    def __init__(self):
        self.df_companies = pd.read_csv(r'company_names/list_companies.csv')
