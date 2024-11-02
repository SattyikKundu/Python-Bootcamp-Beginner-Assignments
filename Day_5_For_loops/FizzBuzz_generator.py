# FizzBuzz game --- this program question can be asked in interview

all_nums = 0
for num in range(1, 100):

    if (num % 3 == 0) and (num % 5 == 0): # this condition 1st since other would run before otherwise
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
