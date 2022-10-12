

data = 0

while data < 10:
    print(f"it's working - > {data}")
    if data == 5:
        break
    data += 1

user_prompt = True

while user_prompt:
    age = input("please enter your age")
    if age.isdigit():
        user_prompt = False
    else:
        print("please enter your age in digits only")
print(f"your age is {age}")



current_year = int(2022)
print("what is your age")
age = int(input())

birth_year = current_year - age

print (f"You were born in {birth_year}")

