immutable_var = (2,'Summer',True)
print(immutable_var)
# immutable_var[0] = 1  #TypeError: 'tuple' object does not support item assignment
mutable_list = [5,7,'Winter',False]
print(mutable_list)
mutable_list[2] = 'Actor'
print(mutable_list)
