records = dict()

while True:
    print('===== Record Keeping App =====')
    print('a. Add Data')
    print('b. Delete Data')
    print('c. End')
    action = input('Select action: ')

    if action == 'a':
        key = input('Enter a key: ')
        value = input('Enter a value: ')
        records[key] = value
        print(records)

    elif action == 'b':
        key = input('Enter a key: ')
        if key in records:
            del records[key]
            print(records)

    elif action == 'c':
        print('THANK YOU')
        break

    else:
        print('Invalid input. Choose action a, b, or c')

