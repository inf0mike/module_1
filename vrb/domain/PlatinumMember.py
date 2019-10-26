from .Member import Member


class PlatinumMember(Member):
    def __init__(self, first_name, last_name, date_of_birth, unique_id=None):
        super().__init__(first_name, last_name, date_of_birth, unique_id)
        self._membership_fee = 100

    @property
    def membership_fee(self):
        return self._membership_fee

    @membership_fee.setter
    def membership_fee(self, value):
        self._membership_fee = value
