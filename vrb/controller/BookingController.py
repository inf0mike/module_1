class BookingController(object):
    # BookingController is a STUB component only and not part of the current solution
    # It is required because we want to test some functionality that is reliant on this data

    def __init__(self):
        self._stub_data = {
            "STUARTMICHAEL": {
                "bookings": [
                    {"date": "2019-09-26"},
                    {"date": "2019-09-25"},
                    {"date": "2019-09-25"},
                    {"date": "2019-09-25"},
                    {"date": "2019-09-25"},
                    {"date": "2019-09-25"},
                    {"date": "2019-09-25"},
                    {"date": "2019-09-25"},
                    {"date": "2019-09-25"},
                    {"date": "2019-09-25"},
                    {"date": "2019-09-25"},
                    {"date": "2019-09-24"}
                ],
                "fee_paid": 100
            },
            "SALLY": {
                "bookings": [
                    {"date": "2019-09-25"},
                    {"date": "2019-09-25"},
                    {"date": "2019-09-25"},
                    {"date": "2019-09-24"}
                ],
                "fee_paid": 100
            }
        }

    def get_bookings_for(self, member_id: str) -> list:
        data = self._get_data_for(member_id)
        if "bookings" in data.keys():
            return data['bookings']
        else:
            return []

    def get_fees_paid_for(self, member_id: str) -> str:
        data = self._get_data_for(member_id)
        if "fee_paid" in data.keys():
            return str(data['fee_paid'])
        else:
            return "0"

    def _get_data_for(self, member_id: str) -> dict:
        result = {}
        for key in self._stub_data.keys():
            if key in member_id:
                result = self._stub_data[key]
        return result
