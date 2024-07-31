def print_params(a=1, b='String', c=True):
    print(a, b, c)


values_list = [3.3, False, 'Play']
values_dict = {'a': 'Just', 'b': 8, 'c': 'Family'}
values_list_2 = [54.32, 'Строка']

print_params(b=25)
print_params(c=[1, 2, 3])
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)


def append_to_list(item, list_my=None):
    if list_my is None:
        list_my = []
        list_my.append(item)
        print(list_my)


append_to_list(1)
append_to_list('False')