





weather = "cold"

# if it's cold:
#take jacket
if weather == "cold":
    print("wear a jacket")

# if it's sunny: boolean value true - next line
# lets go to the beach
elif weather == "sunny":
	print("let's go to the beach")

# if its raining bring a raincoat
elif weather == "rainy":
    print("wear a raincoat")

else:
    print("wear whatever you want")


print("enter your age")
age = int(input())

if age >= 117:
    print("Please re-enter your age")
elif age >= 18:
    print("You can buy any ticket")
elif  16 <= age < 18:
    print("you can buy a general ticket")
elif   12 <= age < 16:
    print("you can't watch restricted content")
else:
    print("you can only watch PG movies")





