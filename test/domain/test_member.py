from unittest import TestCase
from vrb.domain import *
import re


class TestMember(TestCase):
    def add_addresses(self, member: Member) -> None:
        member.add_address(self.new_address1)
        member.add_address(self.new_address2)

    def setUp(self) -> None:
        self.gold_member = GoldMember("gold_first", "gold_last", "gold_dob")
        self.silver_member = SilverMember("silver_first", "silver_last", "silver_dob")
        self.platinum_member = PlatinumMember("platinum_first", "platinum_last", "platinum_dob")
        self.custom_member = PlatinumMember("platinum_first", "platinum_last", "platinum_dob", "custom_id")
        self.new_address1 = Address("1address1", "1address2", "1address3", "1address4", "1postcode")
        self.new_address2 = Address("2address1", "2address2", "2address3", "2address4", "2postcode")

    def test_add_address(self) -> None:
        self.gold_member.add_address(self.new_address1)
        self.assertEqual(len(self.gold_member.get_address_list()), 1)
        self.gold_member.add_address(self.new_address2)
        self.assertEqual(len(self.gold_member.get_address_list()), 2)

    def test_add_bad_address(self) -> None:
        self.assertRaises(RuntimeError, self.gold_member.add_address, "An Address")

    def test_get_address_list(self) -> None:
        self.add_addresses(self.silver_member)
        address_list = self.silver_member.get_address_list()
        self.assertEqual(len(address_list), 2)
        self.assertTrue(isinstance(address_list, list))
        self.assertTrue(isinstance(address_list[0], Address))
        self.assertTrue(isinstance(address_list[1], Address))

    def test_remove_address(self) -> None:
        self.add_addresses(self.gold_member)
        address1 = self.gold_member.get_address_list()[0]
        address2 = self.gold_member.get_address_list()[1]
        self.assertEqual(address1, self.new_address1)
        self.assertEqual(address2, self.new_address2)
        self.gold_member.remove_address(address1)
        address_list = self.gold_member.get_address_list()
        self.assertEqual(len(address_list), 1)
        self.assertEqual(address_list[0], self.new_address2)

    def test_full_name(self) -> None:
        self.assertEqual(self.platinum_member.get_full_name, "platinum_first platinum_last")
        self.assertEqual(self.gold_member.get_full_name, "gold_first gold_last")

    def test_first_name(self) -> None:
        self.assertEqual(self.silver_member.first_name, "silver_first")

    def test_first_name_set(self) -> None:
        self.silver_member.first_name = "BOB"
        self.assertEqual(self.silver_member.first_name, "BOB")

    def test_last_name(self) -> None:
        self.assertEqual(self.gold_member.last_name, "gold_last")

    def test_last_name_set(self) -> None:
        self.gold_member.last_name = "BUILDER"
        self.assertEqual(self.gold_member.last_name, "BUILDER")

    def test_date_of_birth(self) -> None:
        self.assertEqual(self.platinum_member.date_of_birth, "platinum_dob")

    def test_date_of_birth_set(self) -> None:
        self.platinum_member.date_of_birth = "TODAY"
        self.assertEqual(self.platinum_member.date_of_birth, "TODAY")

    def test_id(self) -> None:
        regex_string = "^{ln}{fn}[0-9]{num}$" \
            .format(ln=self.silver_member.last_name.upper(),
                    fn=self.silver_member.first_name.upper(),
                    num="{4}")
        pattern = re.compile(regex_string)
        self.assertRegex(self.silver_member.id, pattern)

    def test_gold_properties_default(self) -> None:
        self.assertEqual(self.gold_member.booking_threshold, 10)
        self.assertEqual(self.gold_member.booking_timescale_months, 12)

    def test_platinum_properties_default(self) -> None:
        self.assertEqual(self.platinum_member.membership_fee, 100)

    def test_gold_properties_set(self) -> None:
        self.gold_member.booking_timescale_months = 1
        self.gold_member.booking_threshold = 25
        self.assertEqual(self.gold_member.booking_threshold, 25)
        self.assertEqual(self.gold_member.booking_timescale_months, 1)

    def test_platinum_properties_set(self) -> None:
        self.platinum_member.membership_fee = 12
        self.assertEqual(self.platinum_member.membership_fee, 12)

    def test_custom_member(self) -> None:
        self.assertEqual(self.custom_member.id, "custom_id")
