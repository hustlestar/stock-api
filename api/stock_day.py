class DailyData(object):
    def __init__(self, date, open_, high_, low_, close_, volume_):
        self.date = date
        self.open_ = open_
        self.high_ = high_
        self.low_ = low_
        self.close_ = close_
        self.volume_ = volume_

    def __str__(self):
        return self.date + \
               '\t open   ' + str(self.open_).ljust(5, '0') + \
               '\t high   ' + str(self.high_).ljust(5, '0') + \
               '\t low    ' + str(self.low_).ljust(5, '0') + \
               '\t close  ' + str(self.close_).ljust(5, '0') + \
               '\t volume ' + str(self.volume_).rjust(10, '.')