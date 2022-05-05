import os
from kaggle.api.kaggle_api_extended import KaggleApi

api = KaggleApi()
api.authenticate()

path = 'DWND'
os.makedirs(path, exist_ok=True)
print("The new directory is created!")

def download_data_sp_500():
    """
    Date: Дата в формате гг-мм-дд
    Open: Цена акции при открытии рынка.
    High: Самая высокая цена, достигнутая за день.
    Low: самая низкая цена, достигнутая за день.
    Close: цена акции при закрытии рынка.
    Volume: количество акций, проданных за день.
    Dividends: дивиденды по акциям
    Stock Splits: дробление акций компании. При разделении акций компания делит свои существующие акции на
    несколько акций, чтобы повысить ликвидность.

    Date: The date is in the format yy-mm-dd
    Open: Price of the stock when the market opens
    High: Highest price reached in the day
    Low: Lowest price reached in the day
    Close: Price of the stock when the market closes
    Volume: Number of shares traded in a day
    Dividends: The dividends of the stock
    Stock Splits: The stock splits of the company. In a stock split, a company divides its existing stock into
    multiple shares to boost liquidity.
    Download sp 500 prices to DWND folder
    # https://www.kaggle.com/datasets/rprkh15/sp500-stock-prices
    :return:
    """
    try:
        api.dataset_download_files('rprkh15/sp500-stock-prices', unzip=True, path='DWND')
        return True
    except Exception as ex:
        print(ex)
        return False

if __name__ == '__main__':
    download_data_sp_500()
