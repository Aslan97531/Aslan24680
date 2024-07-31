calls = 0

def count_calls():
    global calls
    calls += 1
def string_info(string):
    count_calls()
    title = ()
    for i in string:
        title = (len(string), string.upper(), string.lower())

    return title

def is_contains(string, list_to_search):
    count_calls()
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
    return c

result1 = string_info('Capybara')
print(result1)
result2 = string_info('Armageddon')
print(result2)
result3 = is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])
print(result3)
result4 = is_contains('cycle', ['recycling', 'cyclic'])
print(result4)
print(calls)












