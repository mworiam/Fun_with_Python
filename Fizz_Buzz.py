# fizz_buzz Solution to the fizz_buzz algorithm question

def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
         return "Fizz_Buzz"
    if input % 3 == 0:
         return "Fizz"
    if input % 5 == 0:
         return "Buzz"

    return input


print(fizz_buzz())
