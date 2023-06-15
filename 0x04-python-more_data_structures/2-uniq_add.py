#/usr/bin/python3
def uniq_add(my_list=[]):
    result = set(my_list)
    return sum(result)

my_list = [1, 2, 3, 1, 4, 2, 5]
print(uniq_add(my_list))
