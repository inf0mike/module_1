from .Member import Member


class GoldMember(Member):
    # Gold Member class adds booking threshold and timescale values that can be used
    # to ensure the member meets the requirements for this level of membership

    def __init__(self, first_name: str, last_name: str, date_of_birth: str, unique_id: str = None,
                 joined_date: str = None):
        super().__init__(first_name, last_name, date_of_birth, unique_id, joined_date)

        # default values for requirements
        self._booking_threshold = 10
        self._booking_timescale_months = 12

    @property
    def booking_threshold(self) -> int:
        return self._booking_threshold

    @booking_threshold.setter
    def booking_threshold(self, value: int) -> None:
        self._booking_threshold = value

    @property
    def booking_timescale_months(self) -> int:
        return self._booking_timescale_months

    @booking_timescale_months.setter
    def booking_timescale_months(self, value: int) -> None:
        self._booking_timescale_months = value
