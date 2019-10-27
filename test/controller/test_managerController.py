from unittest import TestCase
from vrb.controller import ManagerController
from vrb.domain import *


class TestManagerController(TestCase):

    def setUp(self) -> None:
        self._controller = ManagerController("../file.json")

    def test_load_members(self):
        self.assertIsInstance(self._controller, ManagerController)
        self._controller.load_members()
        self.assertEqual(len(self._controller._members), 1)

    def test_get_member_none(self):
        result = self._controller.get_member("STUARTSALLY2426")
        self.assertIsNone(result)

    def test_get_member(self):
        self._controller.load_members()
        result = self._controller.get_member("STUARTSALLY2426")
        self.assertIsInstance(result, Member)
        self.assertIsInstance(result, GoldMember)

    #
    # def test_add_member(self):
    #     self.fail()
    #
    # def test_delete_member(self):
    #     self.fail()
    #
    # def test_update_membership_level(self):
    #     self.fail()
    #
    def test_get_member_list(self):
        self._controller.load_members()
        members = self._controller.get_member_id_list()
        self.assertIsInstance(members, list)

    #
    def test_get_member_count_for_type(self):
        self._controller.load_members()
        result = self._controller.get_member_count_for_type(MemberType.GOLD_MEMBER)
        self.assertEqual(result, 1)
    #
    # def test_create_address(self):
    #     self.fail()
