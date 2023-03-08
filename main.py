import datetime

palindrome_test = [
    ('kajak', True),
    ('wielbłąd', False),
    ('Kajak', True),
    ('0kajak0', False),
    ([0, "k", 7, 3], False),
    (datetime.date.today(), False),
    (7, False),
    (7.002, False)
]


def is_palindrome(data):
    # data type check
    if not isinstance(data[0], str):
        raise ValueError(f'Wrong data type, provided {data[0]} - {data[1]}')
    if not data[0].isalpha():
        raise ValueError(f'Expected word, got - {data[0]} - {data[1]}')
    if not len(data[0]) > 2:
        raise ValueError(f'String too short, need to be at least 3 letters - {data[1]}')
    if data[0].upper() == data[0].upper()[::-1]:
        return data[1]
    else:
        return data[1]


def test_palindrome():
    try:
        for x in palindrome_test:
            is_palindrome(x)
        assert False, "ValueError expected"
    except ValueError:
        pass


if __name__ == "__main__":
    test_palindrome()
