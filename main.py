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
    while True:
        if type(data) != str:
            print(f'Podane dane nie jest typu string, podano: {type(data)}')
            # data = input("Podaj dane typu string:")
            break
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
                print("Podane słowo nie jest palindromem, podaj palindrom, np. kajak:")
                # data = input("Podane słowo nie jest palindromem, podaj palindrom, np. kajak:")
                i = 0
                number = False
                break
            elif number == False and i == len(data):
                if data.upper() == data.upper()[::-1] and len(data) > 2:
                    print(f"Podane słowo - {data} - jest palindromem.")
                    break
                else:
                    print("Podane słowo nie jest palindromem, podaj palindrom, np. kajak:")
                    # data = input("Podane słowo nie jest palindromem, podaj palindrom, np. kajak:")
                    break

if __name__ == "__main__":
    #palindrome = input("Podaj palindrom:")

    for data in palindrome_test:
        is_palindrome(data)
