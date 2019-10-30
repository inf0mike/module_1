from vrb.domain import *
from vrb.repo import MemberRepoImpl
from enum import Enum


class ManagerController(object):
    # ManagerController is a ROLE controller that is instantiated for membership management role
    # This controller holds the collection of members during the lifecycle of the controller

    # These are type hints for the IDE
    _repository: MemberRepoImpl
    _members: dict

    # A static factory style method to instantiate a new Member Object based on the member type provided
    # if no member type is provided it will generate a silver member by default
    @staticmethod
    def _generate_member(first_name, last_name, date_of_birth,
                         level=MemberType.SILVER_MEMBER, member_id=None):
        if level is MemberType.GOLD_MEMBER:
            member = GoldMember(first_name, last_name, date_of_birth, unique_id=member_id)
        elif level is MemberType.PLATINUM_MEMBER:
            member = PlatinumMember(first_name, last_name, date_of_birth, unique_id=member_id)
        else:
            member = SilverMember(first_name, last_name, date_of_birth, unique_id=member_id)
        return member

    # Constructor
    def __init__(self, data_file: str):
        super().__init__()
        # Initialise our private properties
        self._members = {}
        self._repository = None
        self._data_file = data_file

    # Destructor.  Tell the repository class to close the database
    def __del__(self) -> None:
        if self._repository is not None:
            self._repository.close_database()

    # Request the member objects from the repository
    def load_members(self) -> None:

        # Ensure the repository is instantiated before we attempt to use it
        if self._repository is None:
            self._repository = MemberRepoImpl(self._data_file)

        # Now load all the member objects into the local members dictionary (Java=HashMap)
        member: Member
        for member in self._repository.read_all():
            self._members[member.id] = member

    # request that all member objects from the dict be saved in the physical DB layer
    def save_members(self) -> None:
        self._repository.store_all(list(self._members.values()))

    # Attempt to provide a member object from the dict, return None if we don't have one
    # with a matching ID
    def get_member(self, member_id: str) -> Member:

        try:
            member = self._members[member_id]
        except KeyError:
            member = None
        return member

    # Will create a member object with an address of specified level and add it to the local members dict
    def add_member(self, first_name: str, last_name: str, date_of_birth: str, level=MemberType.SILVER_MEMBER) -> str:
        # generate the member
        member = self._generate_member(first_name, last_name, date_of_birth, level, None)
        # generate the address and add the address to the member
        # member.add_address(Address(line1, line2, line3, line4, post_code))
        # place the new member in the members dict
        self._members[member.id] = member
        # return a reference to the new member
        return member.id

    # Delete a member.  Instruct the repository to immediately delete the member from the physical store
    def delete_member(self, member_id: str) -> None:
        # Pop will retrieve and remove an entry from the dict
        member_to_delete = self._members.pop(member_id, None)
        # now instruct the repo to perform the delete operation
        self._repository.delete_member(member_to_delete)

    # Generate a new member class at the specified level for the specified member_id
    def update_membership_level(self, member_id: str, level: MemberType) -> Member:
        # Get the existing member
        member = self.get_member(member_id)
        # Create a new member object at the requested level
        new_member = self._generate_member(member.first_name, member.last_name, member.date_of_birth, level, member.id)
        # Copy addresses from the old object to the new
        for address in member.get_address_list():
            new_member.add_address(address)
        # replace the object in the dict for the member_id
        self._members[new_member.id] = new_member
        # return a reference to the new object for the caller
        return new_member

    # returns a list of member ids
    def get_member_id_list(self) -> list:
        return list(self._members.keys())

    # returns a list of tuples containing display data for the UI classes that need it.
    # Note, there is no UI code here, only a data structure that is helpful for UI tasks
    # This data can be optionally filtered by substring of first_name or last_name
    def get_filtered_member_display_data(self, search_filter: str = "") -> list:
        result = []
        # Iterate the keys (ids) of our member objects
        for member_id in self._members.keys():
            member: Member = self._members[member_id]
            # only add the member to the result if the filter text appears in first or last name fields
            # using lower() on all strings to ensure case insensitive matching
            if search_filter.lower() in member.first_name.lower() or \
                    search_filter.lower() in member.last_name.lower():
                result.append((member_id, member.first_name, member.last_name, member.__class__.__name__))
        return result

    # return a count of all members
    def get_member_count(self) -> int:
        return len(self._members.keys())

    # return a count of specific member types
    def get_member_count_for_type(self, member_type: MemberType) -> int:
        value = 0
        for member_id in self._members.keys():
            # only count if the class name matches what we asked for
            if self._members[member_id].__class__.__name__ == member_type.value:
                value += 1
        return value

    # Create a new address and add it to the given member_id
    def create_address_for_member(self, line1: str, line2: str, line3: str, line4: str, post_code: str,
                                  member_id: str) -> None:
        member = self.get_member(member_id)
        member.add_address(Address(line1, line2, line3, line4, post_code))
