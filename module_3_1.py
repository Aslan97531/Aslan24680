
# Online Python - IDE, Editor, Compiler, Interpreter

calls = 0

def count_calls():
    global calls
def string_info(string):
    global calls
    title = ()
    for i in string:
        title = (len(string), string.upper(), string.lower())
    calls += 1
    return title



def is_contains(string, list_to_search):
    global calls
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
    calls += 1   
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

count_calls()