#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

bill = float(input("What was the total bill? "))
tip = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
split = float(input("How many people to split the bill? "))
pay = (bill*((100+tip)/100))/split

# pay = round(pay,2)        #not perfect, ex: $2.60-->$2.6, $3.145-->$3.14
pay = "{:.2f}".format(pay)  #better, always at 2 decimal places
print(f"Each person should pay: ${pay}")
