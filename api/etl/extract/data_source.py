import requests

# TODO: Make a class
def get_data_alpha_vantage(ticker, props):
    url = "https://www.alphavantage.co/query?" + \
          "function=TIME_SERIES_DAILY&" + \
          "symbol={0}&".format(ticker) + \
          "datatype={0}&".format(props.get('file.format')) + \
          "apikey={0}".format(props.get('api.key'))
    #response = urllib2.urlopen(url)
    response = requests.get(url)
    #html = response.read()
    html = response.content
    # print html
    return html