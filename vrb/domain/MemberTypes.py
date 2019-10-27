from enum import Enum


class MemberType(Enum):
    # Enum for member types.
    GOLD_MEMBER = "GoldMember"
    SILVER_MEMBER = "SilverMember"
    PLATINUM_MEMBER = "PlatinumMember"

    # A static method to return an Enum for a given integer
    @staticmethod
    def get_type_from_value(value: int) -> Enum:
        if value == 2:
            return MemberType.PLATINUM_MEMBER
        if value == 1:
            return MemberType.GOLD_MEMBER
        return MemberType.SILVER_MEMBER
