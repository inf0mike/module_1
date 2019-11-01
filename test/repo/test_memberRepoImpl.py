from unittest import TestCase
from unittest.mock import patch
from vrb.repo.MemberRepoImpl import MemberRepoImpl
from vrb.domain import *

from tinydb.database import Table, TinyDB

address1 = Address("A1", "A2", "A3", "A4", "AP")
address2 = Address("B1", "B2", "B3", "B4", "BP")
gold_member = GoldMember("GF", "GL", "GD")
silver_member = SilverMember("SF", "SL", "SD")
gold_member.add_address(address1)
silver_member.add_address(address2)


class TestMemberRepoImpl(TestCase):

    def setUp(self) -> None:
        self._database = MemberRepoImpl(".", memory=True)
        self._database.open_database()
        self._database.store_all([gold_member, silver_member])

    def tearDown(self) -> None:
        self._database.close_database()

    @patch("vrb.repo.TinyDB", autospec=True)
    def test_open_database(self, tiny_db):
        self.assertEqual(self._database._data_path, ".")
        self.assertIsNotNone(self._database._db)
        self.assertIsInstance(self._database._db, TinyDB)

    @patch("vrb.repo.TinyDB", autospec=True)
    def test_store_member(self, tinydb):
        self._database.store_member(gold_member)

