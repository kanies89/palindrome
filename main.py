import datetime

data_no_exception = [
    ('kajak', True),
    ('wielbłąd', False),
    ('Kajak', True),
]

data_raises_exception = [
    ([0, "k", 7, 3], "Wrong data type"),
    (datetime.date.today(), "Wrong data type"),
    (7, "Wrong data type"),
    (7.002, "Wrong data type"),
    ("0kajak0", "Expected word!"),
    ("kk", "String too short, needs to be at least 3 letters")
]


def is_palindrome(data):
    if not isinstance(data, str):
        raise ValueError('Wrong data type')
    if not data.isalpha():
        raise ValueError('Expected word!')
    if not len(data) > 2:
        raise ValueError('String too short, needs to be at least 3 letters')

    data = data.upper()
    return data == data[::-1]


def test_palindrome_raises_exception():
    for test_case, expected in data_raises_exception:
        try:
            is_palindrome(test_case)
        except ValueError as e:
            assert e.args[0] == expected


def test_palindrome_no_exception():
    for test_case, expected in data_no_exception:
        assert is_palindrome(test_case) == expected


if __name__ == "__main__":
    test_palindrome_no_exception()
    test_palindrome_raises_exception()
