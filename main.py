import datetime

palindrome_test = [
    'kajak',
    'wielbłąd',
    'Kajak',
    '0kajak0',
    [0, "k", 7, 3],
    datetime.date.today(),
    7,
    7.002

]


def is_palindrome(data):
    number = False
    i = 0
    if type(data) != str:
        print(False)
    else:
        for sign in data:
            try:
                int(sign)
                number = True
                i += 1

            except ValueError:
                try:
                    float(sign)
                    number = True
                    i += 1

                except ValueError:
                    i += 1
                    pass

        if number == True and i == len(data):
            print(False)
        elif number == False and i == len(data):
            if data.upper() == data.upper()[::-1] and len(data) > 2:
                print(True)
            else:
                print(False)


if __name__ == "__main__":

    for data in palindrome_test:
        is_palindrome(data)
