# Loop: initialization, condition, increment / decrement

# count = 1
# while count <= 50:
#     print('My name is khan', count)
#     count += 1

# i = 0
# while i < 9:
#     print(i)
#     i += 1

# for k in range(1, 11, 3):
#     print(k)

# while True:
#     name = input('enter the name: ')
#     if name.isalpha():
#         print(f"name:{name}")
#         break
#     else:
#         print('name cannot be an integer')
#         continue


# i = 20
# while i > 5:
#     j = 15
#     print('Rafi ', end='')
#     while j > 10:
#         print('Rocks ', end='')
#         j -= 1
#     i = i - 1
#     print()

# test = 1
# j = 0
# k = 100
# while (k > 0):
#     while (j < k):
#         test = k + j - 21
#         print('test', test)
#         print(str(1 + int(test / 2)))
#         j += 10
#         print('j', j)
#     k -= 10
# test = 1
# j = 0
# k = 100


# task12
# num = int(input())
# while num > 0:
#     num2 = num
#     a = 0
#     while num2 > 0:
#         num2 = num2//10
#         a += 1
#         x = num // 10**(a-1)
#     if (a == 1):
#         print(x)
#     else:
#         print(x, end=',')
#     num = num % 10**(a-1)

# x = 0
# p = 0
# sum = 0
# p = 1
# x = 2
# q = None
# sum = 0
# while p < 12:
#     q = x + p - (sum + 7 / 3) / 3.0 % 2
#     print('q=', q)
#     sum = sum + x + int(q)
#     print('sum=', sum)
#     x += 1
#     print('x=', x)
#     if x > 5:
#         p += 4 / 2
#         print('p=', p)
#     else:
#         p += (3 % 1)
#         print('p=', p)
# sum = int(sum + p)
# print(sum)


# test = ""
# i = 0
# j = 0
# k = 15
# test = "-->"
# while i < 5:
#     j = k - 1
#     k -= 1
#     while j > 10:
#         test = str(i + j) + "-->" + test
#         print(test)
#         j -= 1
#     i += 1

# test = ""
# i = 5
# j = 0
# k = 15
# while (i < 10):
#     k -= 1
#     j = k
#     while (j > 10):
#         if j % 2 == 0:
#             test = "<--"
#             test = test + str(i) + '3' + "-->" + str(j // 3)
#         else:
#             test = "-->"
#             test = "-->" + str((i // 3)) + test + str(j)
#         print(test)
#         j -= 1
#     i += 1

# test = ""
# i = 5
# j = 0
# k = 15
# while i < 10:
#     k -= 1
#     j = k
#     while j > 10:
#         if (j % 2) == 0:
#             test = "<--"
#             test = str(test) + str(i) + str(2) + "-->" + str(int(j / 2))
#         else:
#             test = "-->"
#             test = "-->" + str(int(i / 2)) + str(test) + str(j)
#         print(test)
#         j = j-1
#     i += 1

# print(5//2)
# print(int(5/2))

# x = 0
# p = 0
# sum = 0
# p = 1
# x = 2
# q = 0.0
# sum = 0
# while (p < 10):
#     q = x + p - (sum + int(5 / 3)) / 3.0 % 2
#     print('q', q)
#     sum = sum + x + int(q)
#     x += 1
#     print(sum)
#     if (x > 5):
#         p += int(4 / 2)
#     else:
#         p += 3 % 1
# sum = sum + p
# print(sum)

my_tuple = 1, 3, 4, 5
a, b, c, d = my_tuple
print(a, b, c, d)
