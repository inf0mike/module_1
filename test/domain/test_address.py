from unittest import TestCase
from vrb.domain import Address


class TestAddress(TestCase):

    def setUp(self) -> None:
        self.address = Address(
            "Address 1",
            "Address 2",
            "Address 3",
            "Address 4",
            "POST CODE"
        )

    def test_formatted_address(self):
        expected = "Address 1\n" \
                   "Address 2\n" \
                   "Address 3\n" \
                   "Address 4\n" \
                   "\n" \
                   "POST CODE"
        self.assertEqual(self.address.formatted_address, expected)

    def test_post_code(self):
        self.assertEqual(self.address.post_code, "POST CODE")
        self.address.post_code = "NEW_CODE"
        self.assertEqual(self.address.post_code, "NEW_CODE")

    def test_line1(self):
        self.assertEqual(self.address.line1, "Address 1")
        self.address.line1 = "New 1"
        self.assertEqual(self.address.line1, "New 1")

    def test_line2(self):
        self.assertEqual(self.address.line2, "Address 2")
        self.address.line2 = "New 2"
        self.assertEqual(self.address.line2, "New 2")

    def test_line3(self):
        self.assertEqual(self.address.line3, "Address 3")
        self.address.line3 = "New 3"
        self.assertEqual(self.address.line3, "New 3")

    def test_line4(self):
        self.assertEqual(self.address.line4, "Address 4")
        self.address.line4 = "New 4"
        self.assertEqual(self.address.line4, "New 4")
