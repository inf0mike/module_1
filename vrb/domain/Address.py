class Address(object):

    def __init__(self, line1: str, line2: str, line3: str, line4: str, post_code: str):
        self._line1 = line1
        self._line2 = line2
        self._line3 = line3
        self._line4 = line4
        self._post_code = post_code

    def __str__(self):
        return self.formatted_address

    def __repr__(self):
        return "{0}, {1}, {2}, {3}, {4}".format(
            self.line1, self.line2, self.line3, self.line4, self.post_code
        )

    @property
    def formatted_address(self) -> str:
        return "{0}\n{1}\n{2}\n{3}\n\n{4}".format(
            self._line1, self._line2, self._line3, self._line4, self._post_code
        )

    @property
    def post_code(self) -> str:
        return self._post_code

    @post_code.setter
    def post_code(self, post_code: str):
        self._post_code = post_code

    @property
    def line1(self) -> str:
        return self._line1

    @line1.setter
    def line1(self, value: str):
        self._line1 = value

    @property
    def line2(self) -> str:
        return self._line2

    @line2.setter
    def line2(self, value: str):
        self._line2 = value

    @property
    def line3(self) -> str:
        return self._line3

    @line3.setter
    def line3(self, value: str):
        self._line3 = value

    @property
    def line4(self) -> str:
        return self._line4

    @line4.setter
    def line4(self, value: str):
        self._line4 = value
