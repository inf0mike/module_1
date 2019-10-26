from vrb.domain import Member
from tinydb import TinyDB, Query
from tinydb.database import Table
import jsonpickle


class MemberRepoImpl(object):
    # _db: TinyDB | Table | None

    def __init__(self, data_path):
        super().__init__()
        self._data_path = data_path
        self._db = None

    def open_database(self) -> None:
        self._db = TinyDB(self._data_path)
        print("Data source ({0}) opened, records: {1} ".format(self._data_path, len(self._db)))

    def read_all(self) -> list:
        if not self._db:
            self.open_database()
        records = self._db.all()
        members = []
        # Here we need to reconstitute the objects.
        for record in records:
            print("Loaded {0}".format(record["member_id"]))
            member = jsonpickle.decode(record["data"])
            members.append(member)
        return members

    def store_member(self, member: Member) -> None:
        # store_member will insert a member record into data table, if
        # there is an existing record, it will remove it before the new insert
        # thus negating the need for an update method
        query = Query()
        # build the data structure to store
        record = {
            "member_id": member.id,
            "data": jsonpickle.encode(member)
        }

        # Remove any existing entry
        removed_ids = self._db.remove(query.member_id == member.id)
        if len(removed_ids) > 0:
            print("Number of entries removed: {0}".format(len(removed_ids)))

        # Insert the new record
        self._db.insert(record)

    def store_all(self, members: list):
        for member in members:
            if isinstance(member, Member):
                self.store_member(member)

    def delete_member(self, member: Member) -> None:
        query = Query()
        self._db.remove(query.member_id == member.id)
