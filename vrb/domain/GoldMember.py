from .Member import Member


class GoldMember(Member):
    def __init__(self, first_name, last_name, date_of_birth, unique_id=None):
        super().__init__(first_name, last_name, date_of_birth, unique_id)
        self._booking_threshold = 10
        self._booking_timescale_months = 12

    @property
    def booking_threshold(self):
        return self._booking_threshold

    @booking_threshold.setter
    def booking_threshold(self, value):
        self._booking_threshold = value

    @property
    def booking_timescale_months(self):
        return self._booking_timescale_months

    @booking_timescale_months.setter
    def booking_timescale_months(self, value):
        self._booking_timescale_months = value
