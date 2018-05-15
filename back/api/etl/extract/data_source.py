import requests

from decorators import singleton

@singleton
class AlphaVantageAPI:
    def __init__(self, props):
        self.api_key = props.get('api.key')
        self.file_format = props.get('file.format')

    def get_data_for_ticker(self, ticker):
        url = "https://www.alphavantage.co/query?" + \
              "function=TIME_SERIES_DAILY&" + \
              "symbol={0}&".format(ticker) + \
              "datatype={0}&".format(self.file_format) + \
              "apikey={0}".format(self.api_key)
        response = requests.get(url)
        html = response.content
        return html


def get_data_alpha_vantage(ticker, props):
    url = "https://www.alphavantage.co/query?" + \
          "function=TIME_SERIES_DAILY&" + \
          "symbol={0}&".format(ticker) + \
          "datatype={0}&".format(props.get('file.format')) + \
          "apikey={0}".format(props.get('api.key'))
    response = requests.get(url)
    html = response.content
    return html


def read_transaction_log(file_path):
    with open(file_path, 'r') as log:
        line_list = log.readlines()

    return line_list
