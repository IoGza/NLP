# Argument, :, then the expression
# Use lambda functions when you need a function for a short period of time
# Also used for when you wish to pass a function as an argument to higher-order functions
remainder = lambda num: num % 2

print(remainder(5))

product = lambda x, y: x * y

print(product(5, 2))


def testfunc(num):
    return lambda x: x * num


result1 = testfunc(6)
result2 = testfunc(100)


print(result1(2))
print(result2(2))


numbers_list = [2, 6, 8, 10, 11, 4, 12, 17, 13, 0, 3, 21]

# Lambda function applied to each element in the list by evaluating if element is greater than 7
# bc numbers_list is an iterable, filter can iterate over each element
filtered_list = list(filter(lambda num: (num > 7), numbers_list))

print(filtered_list)


def addition(n):
    return n + n


numbers = [1, 2, 3, 4]
# Map function carrying out function on each iterable
# Map requires no condition
result = map(addition, numbers)
print(list(result))

numbers = [1, 2, 3, 4]
result = map(lambda num: num + num, numbers)
print(list(result))

numbers2 = [5, 6, 7, 8]
result2 = list(map(lambda x, y: x + y, numbers,numbers2))
print(result2)
