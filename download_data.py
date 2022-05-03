from kaggle.api.kaggle_api_extended import KaggleApi
api = KaggleApi()
api.authenticate()


def download_data_sp_500():
    """
    Download sp 500 prices to DWND folder
    :return:
    """
    try:
        api.dataset_download_files('rprkh15/sp500-stock-prices', unzip=True, path='DWND')
        return True
    except Exception as ex:
        print(ex)
        return False
