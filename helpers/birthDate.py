# import date


class BirthDate:

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def __repr__(self) -> str:
        return "{%2d}/{%2d}/{%2d}".format(self.day, self.month, self.year)