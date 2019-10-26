from .Address import Address
from datetime import datetime


class Member(object):
    def __init__(self, first_name: str, last_name: str, date_of_birth: str, unique_id: str = None):
        super().__init__()

        def generate_id():
            self._id = "{0}{1}{2}".format(
                last_name.upper(),
                first_name.upper(),
                str(int(datetime.now().timestamp()))[-4:]
            )

        self._first_name = first_name
        self._last_name = last_name
        self._date_of_birth = date_of_birth
        self._address_list = []
        if unique_id is None:
            generate_id()
        else:
            self._id = unique_id

    def add_address(self, address):
        if isinstance(address, Address):
            self._address_list.append(address)
        else:
            raise RuntimeError

    def get_address_list(self):
        return self._address_list

    def remove_address(self, address):
        self._address_list.remove(address)

    @property
    def get_full_name(self):
        return "{0} {1}".format(self._first_name, self._last_name)

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        self._first_name = first_name

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        self._last_name = last_name

    @property
    def date_of_birth(self):
        return self._date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, date_of_birth):
        self._date_of_birth = date_of_birth

    @property
    def id(self):
        return self._id
