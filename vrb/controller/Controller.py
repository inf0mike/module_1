from vrb.domain import *
from vrb.repo import MemberRepoImpl


class ManagerController(object):
    _members: list

    def __init__(self):
        super().__init__()
        self._members = []
        self._repository = None

    def load_members(self):
        if self._repository is None:
            self._repository = MemberRepoImpl("/Users/mike/file.json")
        self._members = self._repository.read_all()

    def get_member(self, member_id):
        candidate: Member
        result = None
        if self._members is not None:
            for candidate in self._members:
                if candidate.id == member_id:
                    result = candidate
        return result

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

    def add_member(self, first_name, last_name, date_of_birth, address, level=MemberType.SILVER_MEMBER):
        member = self._generate_member(first_name, last_name, date_of_birth, level, None)
        member.add_address(address)
        self._members.append(member)

    def delete_member(self, member_id):
        pass

    def update_membership_level(self, member_id, level):
        member = self.get_member(member_id)
        new_member = self._generate_member(member.first_name, member.last_name, member.date_of_birth, level, member.id)

    def get_member_id_list(self):
        result = []
        for member in self._members:
            result.append(member.id)
        return result

    def get_member_grid(self):
        result = []
        for member in self._members:
            result.append((member.id, member.first_name, member.last_name, member.__class__.__name__))
        return result

    def get_member_dict(self):
        result = {}
        for member in self._members:
            result[member.id] = member
        return result

    def get_member_count(self):
        return len(self._members)

    def get_member_count_for_type(self, member_type):
        member: Member
        value = 0
        for member in self._members:
            if member.__class__.__name__ == member_type:
                value += 1
        return value

    def add_address_to_member(self, line1, line2, line3, line4, post_code, member_id):
        member = self.get_member(member_id)
        member.add_address(Address(line1, line2, line3, line4, post_code))
