import timeit

code = '''


def fun():
    sum = 0
    for i in range(1000000):
        sum += i
    return sum
'''

print(timeit.timeit(stmt=code))

# import timeit
#
# mysetup = "from math import sqrt"
# # main code snippet for performance check
# mycode = '''
# def example():
#     mylist = []
#     for x in range(100):
#         mylist.append(sqrt(x))
# '''
# # timeit statement
# print(timeit.timeit(setup=mysetup, stmt=mycode, number=10000))
