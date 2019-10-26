from .Member import Member


class SilverMember(Member):
    def __init__(self, first_name, last_name, date_of_birth, unique_id=None):
        super().__init__(first_name, last_name, date_of_birth, unique_id)
