# from enum import Enum

# from parser import sequence2st


# class State(Enum):
#     INACTIVE = 0
#     ACTIVE = 1


# print(State.ACTIVE.value)


# name = 'khaled'
# print(name)

# print(7 // 2)


# name = "beau is cool"
# print(name[2:9])

# num2 = complex(2, 3)
# print(num2)

# print(abs(-5.5))

# name = input("What is your name?")
# print("My name is " + name)

# cats = ['meaw', 2, 'kitten', False]
# print('meaw' in cats)


# set1 = {'sallu', 'mallu'}
# set2 = {'sallu'}

# intersect = set1 & set2
# print(intersect)

# set1 = {'sallu', 'mallu'}
# set2 = {'sallu'}

# intersect = set1 | set2
# print(intersect)

# function
# def department(name):
#     print('Brac', name)


# department('Cse')
# department('Law')
# department('Pharmacy')

# def hello(name):
#     print('Hello ' + name + '!')
#     return name, 'Beau', 8


# print(hello('Syd'))

# def count():
#     count = 10

#     def increment():
#         nonlocal count
#         count = count + 10
#         print(count)

#     increment()


# count()

# task13
mark = int(input('Provide your mark: '))
if (mark >= 0 and mark <= 100):
    if (mark >= 90):
        print('A')
    elif (mark >= 80 and mark <= 89):
        print('B')
    elif (mark >= 70 and mark <= 79):
        print('C')
    elif (mark >= 60 and mark <= 69):
        print('D')
    elif (mark >= 50 and mark <= 59):
        print('E')
    else:
        print('F')

# task14
distance = int(input('traveled distance in meters: '))
time = int(input('spent time in seconds : '))
