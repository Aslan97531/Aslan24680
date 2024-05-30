my_dict = {'Alex':1999, 'Frank':1993, 'Ricky':1996}
print(my_dict)
print(my_dict['Frank'])
my_dict['Rose'] = 1997
print(my_dict['Rose'])
my_dict.update({'Felix':1995, 'Luis':1998})
print(my_dict)
a = my_dict.pop('Frank')
print(my_dict)
print(a)

my_set = {0,1,4,1,2,0,'Strike',True}
print(my_set)
my_set.update({7,'Sun'})
print(my_set)
my_set.discard('Strike')
print(my_set)

