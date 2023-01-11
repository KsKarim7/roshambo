# a = (input("1st number:"))
# b = (input("2nd number:"))
# floordivision = a // b
# print("floordivision", floordivision)

# print('Khaled')

givenInputs = int(input("Number of seconds?"))
# convertToMinute = givenInputs // 60
convertToDay = givenInputs // 86400

# if (givenInputs % 86400 >= 1):
print(convertToDay, 'Days')
if (givenInputs % 3600 > 0):
    remainingHours = givenInputs - (convertToDay * 86400)
    convertToHour = remainingHours // 3600
    print(convertToHour, 'Hours')
if (givenInputs % 86400 > 0):
    remainingMinutes = givenInputs - \
        (convertToDay * 86400) - (convertToHour * 3600)
    convertToMinutes = remainingMinutes // 60
    print(convertToMinutes, 'minutes')
# if (remainingMinutes % 60 > 0):
#     remainingSeconds = givenInputs - \
#         (convertToDay * 86400) - (convertToHour * 3600) - (convertToMinutes * 60)
#     convertToSeconds = remainingMinutes // 1
#     print(convertToSeconds, 'seconds')


# if (givenInputs % 60 >= 1):
#     print(convertToMinute, 'minutes')
#     if (givenInputs % 3600 >= 1):
#         remainingSeconds = givenInputs - convertToMinute * 60
#         convertToHour = remainingSeconds // 3600
#         print(convertToHour, 'Hours')
#         if (givenInputs % 86400 >= 1):
#             remainingMinutes = givenInputs - convertToHour * 3600
#             convertToDay = remainingMinutes // 86400
#             print(convertToDay, 'days')


# print(convertToMinute, 'minutes')
