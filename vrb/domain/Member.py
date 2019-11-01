from .Address import Address
from datetime import datetime, date


class Member(object):

    def __init__(self, first_name: str, last_name: str, date_of_birth: str, unique_id: str = None,
                 joined_date: str = None):
        super().__init__()

        # Internal function to generate a unique ID for the new member
        def generate_id() -> None:
            self._id = "{0}{1}{2}".format(
                last_name.upper(),
                first_name.upper(),
                str(int(datetime.now().timestamp()))[-4:]
            )

        # Initialise properties
        self._first_name = first_name
        self._last_name = last_name
        self._date_of_birth = date_of_birth
        self._address_list = []

        # If a unique ID is not given then generate it
        if unique_id is None:
            generate_id()
        else:
            self._id = unique_id

        # If the joining date is not provided then determine it now
        if joined_date is None:
            # Use today's date and store as iso format string
            self._joined_date = date.today().isoformat()
        else:
            self._joined_date = joined_date

    # create a new address for this member
    def create_address(self, line1: str, line2: str, line3: str, line4: str, post_code: str) -> Address:
        new_address = Address(line1, line2, line3, line4, post_code)
        self.add_address(new_address)
        return new_address

    def add_address(self, address: Address) -> None:
        # Validate the type is an Address object and add it to the
        # Addresses for this member
        if isinstance(address, Address):
            self._address_list.append(address)
        else:
            raise RuntimeError

    def get_address_list(self) -> list:
        # Return a list (Array) of Address objects
        return self._address_list

    def remove_address(self, address: Address) -> None:
        # Remove the given Address object from this Members addresses
        self._address_list.remove(address)

    # Getters and Setters for properties
    @property
    def get_full_name(self) -> str:
        # Property provides formatted full name
        return "{0} {1}".format(self._first_name, self._last_name)

    @property
    def first_name(self) -> str:
        return self._first_name

    @first_name.setter
    def first_name(self, first_name: str):
        self._first_name = first_name

    @property
    def last_name(self) -> str:
        return self._last_name

    @last_name.setter
    def last_name(self, last_name: str):
        self._last_name = last_name

    @property
    def date_of_birth(self) -> str:
        return self._date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, date_of_birth: str):
        self._date_of_birth = date_of_birth

    @property
    def id(self) -> str:
        return self._id

    @property
    def joined_date(self) -> str:
        return self._joined_date
