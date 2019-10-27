from .Member import Member


# Platinum Member class adds membership fee values that can be used
# to ensure the member meets the requirements for this level of membership
class PlatinumMember(Member):

    def __init__(self, first_name: str, last_name: str, date_of_birth: str, unique_id: str = None,
                 joined_date: str = None):
        super().__init__(first_name, last_name, date_of_birth, unique_id, joined_date)
        self._membership_fee = 100

    @property
    def membership_fee(self) -> int:
        return self._membership_fee

    @membership_fee.setter
    def membership_fee(self, value: int):
        self._membership_fee = value
