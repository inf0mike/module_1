from unittest import TestCase
from vrb.domain import *
import re


class TestMember(TestCase):

    # Test setup.  Create some members
    def setUp(self) -> None:
        self.gold_member = GoldMember("gold_first", "gold_last", "gold_dob")
        self.silver_member = SilverMember("silver_first", "silver_last", "silver_dob")
        self.platinum_member = PlatinumMember("platinum_first", "platinum_last", "platinum_dob")
        self.custom_member = PlatinumMember("platinum_first", "platinum_last", "platinum_dob", "custom_id")

    # Test we can create addresses and add them to the member object
    def test_create_address(self) -> None:
        self.gold_member.create_address("1address1", "1address2", "1address3", "1address4", "1postcode")
        self.assertEqual(len(self.gold_member.get_address_list()), 1)  # Address list length should be 1
        self.gold_member.create_address("2address1", "2address2", "2address3", "2address4", "2postcode")
        self.assertEqual(len(self.gold_member.get_address_list()), 2)  # Address list length should be 2

    # Test we can get the address list for a member
    def test_get_address_list(self) -> None:
        self.silver_member.create_address("1address1", "1address2", "1address3", "1address4", "1postcode")
        self.silver_member.create_address("2address1", "2address2", "2address3", "2address4", "2postcode")
        address_list = self.silver_member.get_address_list()
        self.assertEqual(len(address_list), 2)  # Assert length
        self.assertTrue(isinstance(address_list, list))  # Assert type of list
        self.assertTrue(isinstance(address_list[0], Address))  # Assert class of entry is Address
        self.assertTrue(isinstance(address_list[1], Address))  # Assert class of entry is Address

    # Test we can remove addresses
    def test_remove_address(self) -> None:
        new_address1 = self.gold_member.create_address("1address1", "1address2", "1address3", "1address4", "1postcode")
        new_address2 = self.gold_member.create_address("2address1", "2address2", "2address3", "2address4", "2postcode")
        address1 = self.gold_member.get_address_list()[0]
        address2 = self.gold_member.get_address_list()[1]
        self.assertEqual(address1, new_address1)  # Assert data is correct
        self.assertEqual(address2, new_address2)  # Assert data is correct
        self.gold_member.remove_address(address1)
        address_list = self.gold_member.get_address_list()
        self.assertEqual(len(address_list), 1)  # Assert address count is now only 1
        self.assertEqual(address_list[0], new_address2)  # Assert data is correct

    # Test full name
    def test_full_name(self) -> None:
        self.assertEqual(self.platinum_member.get_full_name, "platinum_first platinum_last")
        self.assertEqual(self.gold_member.get_full_name, "gold_first gold_last")

    # Test the auto generation of IDs is as expected
    def test_id(self) -> None:
        regex_string = "^{ln}{fn}[0-9]{num}$" \
            .format(ln=self.silver_member.last_name.upper(),
                    fn=self.silver_member.first_name.upper(),
                    num="{4}")
        pattern = re.compile(regex_string)
        self.assertRegex(self.silver_member.id, pattern)  # Assert data is correct

    # Test Gold Member object have the correct default values
    def test_gold_properties_default(self) -> None:
        self.assertEqual(self.gold_member.booking_threshold, 10)  # Assert data is correct
        self.assertEqual(self.gold_member.booking_timescale_months, 12)  # Assert data is correct

    # Test Platinum Member object has the correct default values
    def test_platinum_properties_default(self) -> None:
        self.assertEqual(self.platinum_member.membership_fee, 100)  # Assert data is correct

    # Test members can be created by providing an ID
    def test_custom_member(self) -> None:
        self.assertEqual(self.custom_member.id, "custom_id")  # Assert data is correct
