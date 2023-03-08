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
    # data type check
    if type(data) != str:
        return False
    else:
        for sign in data:
            try:
                # if int in string check
                int(sign)
                number = True
                i += 1

            except ValueError:
                i += 1
                pass

        if number == True and i == len(data):
            return False
        elif number == False and i == len(data):
            # palindrome check
            if data.upper() == data.upper()[::-1] and len(data) > 2:
                return True
            else:
                return False


if __name__ == "__main__":

    for data in palindrome_test:
        print(is_palindrome(data))
