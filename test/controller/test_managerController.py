from unittest import TestCase, mock
from vrb.controller import ManagerController
from vrb.controller.Controller import MemberRepoImpl
from vrb.domain import *

from unittest.mock import patch

# Initialise some test data to work with
test_member = GoldMember("Sally", "Stuart", "1970-08-10", "STUARTSALLY2426", "2019-10-30")
test_member2 = GoldMember("Mike", "Stuart", "1971-02-24", "STUARTMIKE2338", "2019-10-30")
test_member.create_address("line1", "line2", "line3", "line4", "post_code")
test_member2.create_address("line1", "line2", "line3", "line4", "post_code")


# Enable mocking of the repository class
@patch.object(MemberRepoImpl, "read_all")
class TestManagerController(TestCase):

    # Test setup
    def setUp(self) -> None:
        self._controller = ManagerController("*")

    # Test we can load data from repository
    def test_load_members(self, mock_read):
        mock_read.return_value = [test_member]  # initialise mock data
        self.assertIsInstance(self._controller, ManagerController)  # Assert the controller is created
        self._controller.load_members()
        self.assertEqual(len(self._controller._members), 1)  # Assert the correct amount of data is loaded
        self.assertEqual(self._controller.get_member("STUARTSALLY2426").first_name, "Sally")  # Assert data correct

    # Test we get no results when the repository has not provided data
    def test_get_member_when_data_not_loaded(self, mock_read):
        mock_read.return_value = [test_member]  # initialise mock data
        result = self._controller.get_member("STUARTSALLY2426")
        self.assertIsNone(result)  # Assert there is no data
        mock_read.assert_not_called()  # Assert the repo was not asked to read data from disk

    # Test that requesting a non-existent member we get expected response
    def test_bad_get_member_when_data_is_loaded(self, mock_read):
        mock_read.return_value = [test_member]  # initialise mock data
        self._controller.load_members()
        result = self._controller.get_member("BAD")
        self.assertIsNone(result)  # Assert there is no data
        mock_read.assert_called()  # Assert the repo WAS asked to read data from disk

    # Test that with loaded data we can get an individual member
    def test_get_member(self, mock_read):
        mock_read.return_value = [test_member]  # initialise mock data
        self._controller.load_members()
        result = self._controller.get_member("STUARTSALLY2426")
        self.assertIsInstance(result, Member)  # Assert the data is correct
        self.assertIsInstance(result, GoldMember)  # Assert the data is correct

    # Test that when creating a member, if no level is specified, then silver member is created
    def test_add_member_creates_silver_by_default(self, mock_read):
        new_member_id = self._controller.add_member("first", "last", "1900-01-01")
        self.assertIn("FIRST", new_member_id)
        self.assertIn("LAST", new_member_id)
        member = self._controller.get_member(new_member_id)
        self.assertIsInstance(member, SilverMember)  # Assert the class is correct

    # Test creating Gold member level
    def test_add_member_gold_creates_specified_type(self, mock_read):
        new_member_id = self._controller.add_member("first", "last", "1900-01-01", MemberType.GOLD_MEMBER)
        member = self._controller.get_member(new_member_id)
        self.assertIsInstance(member, GoldMember)  # Assert the class is correct

    # Test creating Gold member level
    def test_add_member_platinum_creates_specified_type(self, mock_read):
        new_member_id = self._controller.add_member("first", "last", "1900-01-01", MemberType.PLATINUM_MEMBER)
        member = self._controller.get_member(new_member_id)
        self.assertIsInstance(member, PlatinumMember)  # Assert the class is correct

    # Enable mocking of the delete_member method on the repository
    # Test deleting a member
    @patch.object(MemberRepoImpl, "delete_member")
    def test_delete_member(self, mock_delete, mock_read):
        mock_delete.return_value = None  # initialise mock data
        mock_read.return_value = [test_member, test_member2]  # initialise mock data
        self._controller.load_members()
        self.assertEqual(len(self._controller.get_member_id_list()), 2)  # Assert the data is correct
        self._controller.delete_member("STUARTSALLY2426")
        mock_delete.assert_called()  # Assert the repo was instructed to delete
        self.assertEqual(len(self._controller.get_member_id_list()), 1)  # Assert the data is correct

    # Test changing of membership level by replacing existing class with new class
    def test_update_membership_level(self, mock_read):
        mock_read.return_value = [test_member, test_member2]  # initialise mock data
        self._controller.load_members()
        self.assertIsInstance(self._controller.get_member("STUARTSALLY2426"), GoldMember)  # Assert  class is correct
        self._controller.update_membership_level("STUARTSALLY2426", MemberType.PLATINUM_MEMBER)  # Make the change
        self.assertIsInstance(self._controller.get_member("STUARTSALLY2426"), PlatinumMember)  # Assert class is correct

    # Test the requesting of a member list
    def test_get_member_list(self, mock_read):
        mock_read.return_value = [test_member, test_member2]  # initialise mock data
        self._controller.load_members()
        members = self._controller.get_member_id_list()
        self.assertIsInstance(members, list)  # Assert the class is correct
        self.assertEqual(len(self._controller.get_member_id_list()), 2)  # Assert the data is correct

    # Test the counting of member types
    def test_get_member_count_for_type(self, mock_read):
        mock_read.return_value = [test_member]  # initialise mock data
        self._controller.load_members()
        result = self._controller.get_member_count_for_type(MemberType.GOLD_MEMBER)
        self.assertEqual(result, 1)  # Assert the data is correct

    # Test unfiltered user data for UI
    def test_get_unfiltered_user_table_data(self, mock_read):
        mock_read.return_value = [test_member, test_member2]  # initialise mock data
        self._controller.load_members()
        data_grid = self._controller.get_filtered_member_display_data()
        self.assertIsInstance(data_grid, list)  # Assert we receive a list
        self.assertEqual(len(data_grid), 2)  # Assert the list contain all of the members

    # Test filtered user data for UI
    def test_get_filtered_user_table_data(self, mock_read):
        mock_read.return_value = [test_member, test_member2]  # initialise mock data
        self._controller.load_members()
        data_grid = self._controller.get_filtered_member_display_data("mike")
        self.assertEqual(len(data_grid), 1)  # Assert the list contain all of the members
        data_grid = self._controller.get_filtered_member_display_data("bob")
        self.assertEqual(len(data_grid), 0)  # Assert the list contain none of the members
