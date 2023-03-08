import datetime

palindrome_test = [
    ('kajak', True),
    ('wielbłąd', False),
    ('Kajak', True),
    ('0kajak0', ValueError),
    ([0, "k", 7, 3], ValueError),
    (datetime.date.today(), ValueError),
    (7, ValueError),
    (7.002, ValueError)
    ]


def is_palindrome(data):
    # data type check
    assert type(data[0]) != str(), \
        f'Wrong data type - {data[1]}'
    assert data[0].isalpha(), \
        f'Expected word, got - {data[0]} - {data[1]}'
    assert len(data[0]) > 2, \
        f'String too short - {data[1]}'
    if data[0].upper() == data[0].upper()[::-1]:
        return data[1]
    else:
        return data[1]


if __name__ == "__main__":

    for data in palindrome_test:
        print(is_palindrome(data))
