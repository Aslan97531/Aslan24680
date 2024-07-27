calls = 0

def count_calls():
    global calls
    a = 0
    b = 0

    def string_info(string):
        nonlocal b
        title = ()
        for i in string:
            title = (len(string), string.upper(), string.lower())

        b += 1
        return title

    result2 = string_info('Capybara')
    print(result2)
    result5 = string_info('Armageddon')
    print(result5)

    def is_contains(string, list_to_search):
        nonlocal a
        c = False
        string = string.lower()
        for i in list_to_search:
            i = i.lower()
            if string == i:
                c = True
                break
                print(c)
            else:
                continue
        a += 1
        return c

    result3 = is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])
    print(result3)
    result4 = is_contains('cycle', ['recycling', 'cyclic'])
    print(result4)
    calls = a + b
    print(calls)

count_calls()










