from vrb.domain import Member
from tinydb import TinyDB, Query, storages
import jsonpickle


# We are using TinyDB, a document style "nosql" data store that will store serialised python objects.
# Python objects are serialised and de-serialised using the "jsonpickle" third party library

# Member repository implmentation Class
# Python does not have interfaces to adhere to so we simple build on "object"
class MemberRepoImpl(object):
    # type hint
    _db: TinyDB

    # Constructor
    def __init__(self, data_path, memory=False):
        super().__init__()

        # Initialise private properties
        self._data_path = data_path
        self._db = None
        self._memory = memory

    # python destructor.  If this object is destroyed, ensure the DB file is closed
    def __del__(self) -> None:
        if __name__ == '__main__':
            self.close_database()

    # allow user of repo to manually request closure of the DB file
    def close_database(self) -> None:
        if self._db is not None:
            print("Closing database")
            self._db.close()

    # user of repo can call open_database before attempting IO.
    def open_database(self) -> None:
        if self._memory:
            self._db = TinyDB(storage=storages.MemoryStorage)
        else:
            self._db = TinyDB(self._data_path)
        print("Data source ({0}) opened, records: {1} ".format(self._data_path, len(self._db)))

    # reads all serialised object data from the configured database file and re-constitutes the objects
    # into python list which is then returned to the caller
    def read_all(self) -> list:
        # ensure the database is opened
        if not self._db:
            self.open_database()
        records = self._db.all()

        members = []
        # Here we need to reconstitute the objects.
        for record in records:
            # decode the serialised object to re-constitute
            member = jsonpickle.decode(record["data"])
            members.append(member)
        # return the list
        return members

    # store_member will insert a member record into data table, if
    # there is an existing record, it will remove it before the new insert
    # thus negating the need for an update method
    def store_member(self, member: Member) -> None:
        if not self._db:
            self.open_database()

        query = Query()
        # build the data structure to store
        record = {
            "member_id": member.id,
            "data": jsonpickle.encode(member)
        }

        # Remove any existing entry
        removed_ids = self._db.remove(query.member_id == member.id)
        if len(removed_ids) == 0:
            print("Warning: no records removed")
        # Insert the new record
        self._db.insert(record)

    # given a list of members, call store_member for each of them to store them in the database
    def store_all(self, members: list) -> None:
        for member in members:
            # A quick check to ensure the data types are as expected
            if isinstance(member, Member):
                self.store_member(member)

    # delete a member from the physical data store
    def delete_member(self, member: Member) -> None:
        if not self._db:
            self.open_database()
        query = Query()
        self._db.remove(query.member_id == member.id)
