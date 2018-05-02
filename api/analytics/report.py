def get_interesting_stocks(stocks_processed, number_of_volume_spikes=0,
                           change_for_period=0.0,
                           max_day_range=0.0):
    interesting_stocks = []
    for stock in stocks_processed:
        if stock.vol_spikes_list[0] >= number_of_volume_spikes \
                and stock.max_day_range >= max_day_range:
            print stock
            interesting_stocks.append(stock)
    return interesting_stocks


def analyze(s):
    pass