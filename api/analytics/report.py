

def print_only_interesting(stocks, number_of_volume_spikes=0,
                           change_for_period=0.0,
                           max_day_range=0.0):
    interesting_stocks = []
    for s in stocks:
        if s.number_of_volume_spikes >= number_of_volume_spikes \
                and s.change_for_period >= change_for_period \
                and s.max_day_range >= max_day_range:
            print s
            interesting_stocks.append(s)
    return interesting_stocks


def analyze(s):
    pass