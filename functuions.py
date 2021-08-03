# def function_name (parameter_a, parameter_b):
#     print((parameter_a + parameter_b) / (parameter_a * 1.4))

# x = function_name(7,4)

# print(x)

# # random numbers

from random import randint

def roll_dice(number, sides, bonus):
    # number an dsides - xdy - 2d6, 3d8, 2d10
    #bonus is added to the reault of rolling those x dice

    result = bonus
    for x in range (0, number):
        result += randint(1, sides)

    return result

print(roll_dice(2,6,1))
