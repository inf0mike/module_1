from .Member import Member


# Silver Member class offers no additional functionality at this time
class SilverMember(Member):

    def __init__(self, first_name: str, last_name: str, date_of_birth: str, unique_id: str = None,
                 joined_date: str = None):
        super().__init__(first_name, last_name, date_of_birth, unique_id, joined_date)
