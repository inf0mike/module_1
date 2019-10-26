from vrb.domain import *
from vrb.repo import MemberRepoImpl


class ManagerController(object):
    _repository: MemberRepoImpl
    _members: dict

    def __init__(self):
        super().__init__()
        self._members = {}
        self._repository = None

    def load_members(self):
        if self._repository is None:
            self._repository = MemberRepoImpl("/Users/mike/file.json")
        member: Member
        for member in self._repository.read_all():
            self._members[member.id] = member

    def save_members(self):
        self._repository.store_all(list(self._members.values()))

    def get_member(self, member_id) -> Member:
        try:
            member = self._members[member_id]
        except KeyError:
            member = None
        return member

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

    def add_member(self, first_name, last_name, date_of_birth, line1, line2, line3, line4, post_code,
                   level=MemberType.SILVER_MEMBER) -> Member:
        member = self._generate_member(first_name, last_name, date_of_birth, level, None)
        member.add_address(Address(line1, line2, line3, line4, post_code))
        self._members[member.id] = member
        return member

    def delete_member(self, member_id):
        member_to_delete = self._members.pop(member_id, None)
        self._repository.delete_member(member_to_delete)

    def update_membership_level(self, member_id, level):
        member = self.get_member(member_id)
        new_member = self._generate_member(member.first_name, member.last_name, member.date_of_birth, level, member.id)
        for address in member.get_address_list():
            new_member.add_address(address)
        self._members[new_member.id] = new_member
        return new_member

    def get_member_id_list(self):
        return list(self._members.keys())

    def get_member_grid(self):
        result = []
        for member_id in self._members.keys():
            member: Member = self._members[member_id]
            result.append((member_id, member.first_name, member.last_name, member.__class__.__name__))
        return result

    def get_member_count(self):
        return len(self._members.keys())

    def get_member_count_for_type(self, member_type: MemberType):
        value = 0
        for member_id in self._members.keys():
            if self._members[member_id].__class__.__name__ == member_type.value:
                value += 1
        return value

    def add_address_to_member(self, line1, line2, line3, line4, post_code, member_id):
        member = self.get_member(member_id)
        member.add_address(Address(line1, line2, line3, line4, post_code))
