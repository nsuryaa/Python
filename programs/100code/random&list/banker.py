names_string = "Surya, Siva, Bharath, Tamil"
names = names_string.split(", ")

import random

#Get the total number of items in list

nums_items = len(names)

#Generate random numbers between 0 and the last index

random_choice = random.randint(0,nums_items - 1)

#Pick out random person from list of names using the random number.

person_who_will_pay = names[random_choice]

print(person_who_will_pay + " is going to buy the meal today!")

