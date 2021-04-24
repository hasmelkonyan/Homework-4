# Write a function that will return the count of given character in the given string
def num_of_characters(str):
    count = 0
    for each_member in str:
        if each_member != ' ':
            count += 1

    return count


print(num_of_characters("Winter is coming."))
print(num_of_characters("I’m not going to stop the wheel. I’m going to break the wheel."))


# Write a function that will return count of characters till the given one

def count_till_one(str1):
    count1 = 0
    for each_character in str1:
        if each_character != ' ':
            if each_character != "1":
                count1 += 1
            else:
                break
    return count1


print(count_till_one("Fire cannot kill a 1 dragon."))


# Write a function that will return the factorial of a given number

def factorial(number):
    sum = 2
    if 0 <= number <= 2:
        sum = number
    else:
        for x in range(2, number, 1):
            sum = sum * (x + 1)
    return sum


print(factorial(1))


# Write a function that will return true if the number is bouquet and false if not. The result of function should be
# used in another one which will power up the number by 3

def is_even(number2):
    even = True
    if number2 % 2 == 1:
        even = False
    return even

print(is_even(4))

def cubes(number3):
    if is_even(number3) == True:
        return number3**3

print(cubes(4))
