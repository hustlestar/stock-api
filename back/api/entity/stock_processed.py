class StockProcessed:
    def __init__(self, stock_raw):
        self.stock_raw = stock_raw
        self.first_open_price = 0
        self.last_close_price = 0
        self.max_price = 0
        self.min_price = 100000
        self.change_for_period = 0
        self.change_percent = 0
        self.max_positive_day_change = 0
        self.max_negative_day_change = 100000
        self.max_day_range = 0

        self.total_vol = 0
        self.avg_volume = 0
        self.spike_multipliers_list = [3, 4, 5, 10]
        self.vol_spikes_list = None
        self.process_raw_stock()

    def __str__(self):
        big_str = str(self.stock_raw) + '\n' \
                  + '\tstart open price    : ' + str(self.first_open_price) + '\n' \
                  + '\tlast close price    : ' + str(self.last_close_price) + '\n' \
                  + '\tmaximum price       : ' + str(self.max_price) + '\n' \
                  + '\tminimum price       : ' + str(self.min_price) + '\n' \
                  + '\tchange for period $ : ' + str(self.change_for_period) + '\n' \
                  + '\tchange for period % : {0:.2f}% \n'.format(self.change_percent) \
                  + '\tmax day range       : ' + str(self.max_day_range) + '\n' \
                  + '\tmax day gain        : ' + str(self.max_positive_day_change) + '\n' \
                  + '\tmax day loss        : ' + str(self.max_negative_day_change) + '\n' \
                  + '\t---------------------------------------------------------------\n' \
                  + '\tavg day volume      : ' + str(self.avg_volume) + '\n'
        for i, val in enumerate(self.spike_multipliers_list):
            big_str = big_str + \
                    '\tn vol spike x{0}     : {1}\n'.format(str(val).rjust(2, ' '), self.vol_spikes_list[i])
        return big_str

    def process_raw_stock(self):
        self.first_open_price = self.stock_raw.daily_data[-1].open_
        self.last_close_price = self.stock_raw.daily_data[0].close_
        self.change_for_period = self.last_close_price - self.first_open_price
        self.change_percent = self.change_for_period / self.first_open_price * 100
        for day in self.stock_raw.daily_data:
            self.total_vol += day.volume_
            if day.high_ > self.max_price:
                self.max_price = day.high_
            if day.low_ < self.min_price:
                self.min_price = day.low_
            if day.high_ - day.low_ > self.max_day_range:
                self.max_day_range = day.high_ - day.low_
            if day.close_ - day.open_ > self.max_positive_day_change:
                self.max_positive_day_change = day.close_ - day.open_
            elif day.close_ - day.open_ < self.max_negative_day_change:
                self.max_negative_day_change = day.close_ - day.open_

        self.avg_volume = self.total_vol / len(self.stock_raw.daily_data)
        self.vol_spikes_list = self.count_vol_spikes(self.stock_raw.daily_data, self.avg_volume,
                                                     self.spike_multipliers_list)
        print str(self.vol_spikes_list)

    def count_vol_spikes(self, daily_data, avg_vol, spike_multipliers_list):
        number_of_volume_spikes = [0 for m in spike_multipliers_list]
        for day in daily_data:
            for i, mult in enumerate(spike_multipliers_list):
                if day.volume_ > avg_vol * mult:
                    number_of_volume_spikes[i] += 1
        return number_of_volume_spikes
