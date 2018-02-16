from datetime import datetime


class StockRaw(object):
    def __init__(self, symbol, daily_data):
        self.symbol = symbol
        self.daily_data = daily_data

    def __str__(self):
        return '{0} report {1}\n'.format(self.symbol.upper(), datetime.now().strftime("%Y-%m-%d %H:%M")) + \
               '\tAverage Volume - {0}\n'.format(self.average_volume) + \
               '\tNumber of Volume Spikes - {0}\n'.format(self.number_of_volume_spikes) + \
               '\tMax price $ {0}\n'.format(self.max_price) + \
               '\tMin price $ {0}\n'.format(self.min_price) + \
               '\tChange    $ {0}\n'.format(self.change_for_period) + \
               '\tMax range $ {0}\n'.format(self.max_day_range) + \
               '\tMax + day $ {0}\n'.format(self.max_positive_day_change) + \
               '\tMax - day $ {0}\n'.format(self.max_negative_day_change)


    def total_vol(self):
        res = 0
        for day in self.daily_data:
            res = res + day.volume_
        self.total_volume = res
        return res

    def avg_vol(self):
        if 'total_volume' not in locals():
            total_vol = self.total_vol()
        self.average_volume = total_vol / len(self.daily_data)
        return self.average_volume

    def count_vol_spikes(self, spike_multiplier):
        if 'average_volume' not in locals():
            avg_vol = self.avg_vol()
        number_of_volume_spikes = 0
        for day in self.daily_data:
            if day.volume_ > avg_vol * spike_multiplier:
                number_of_volume_spikes += 1
        self.number_of_volume_spikes = number_of_volume_spikes
        return number_of_volume_spikes

    def calculate_limits(self):
        max_ = 0
        min_ = 10000
        change_ = self.daily_data[-1].open_ - self.daily_data[0].close_
        max_positive_day_change = 0
        max_negative_day_change = 10000
        max_day_range = 0
        for day in self.daily_data:
            if day.high_ > max_:
                max_ = day.high_
            if day.low_ < min_:
                min_ = day.low_
            if day.high_ - day.low_ > max_day_range:
                max_day_range = day.high_ - day.low_
            if day.close_ - day.open_ > max_positive_day_change:
                max_positive_day_change = day.close_ - day.open_
            elif day.close_ - day.open_ < max_negative_day_change:
                max_negative_day_change = day.close_ - day.open_
        self.min_price = min_
        self.max_price = max_
        self.max_positive_day_change = max_positive_day_change
        self.max_negative_day_change = max_negative_day_change
        self.change_for_period = change_
        self.max_day_range = max_day_range

    def _perfom_full_analysis(self):
        self.total_vol()
        self.avg_vol()
        self.calculate_limits()
        self.count_vol_spikes(4)