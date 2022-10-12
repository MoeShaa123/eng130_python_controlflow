# Python Control Flow
## if elif else
### Loops - for loop - while loop
#### Python keywords break - continue etc.


```python
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

```
### Iterating through dictionary

```python
for x in student_1:
    # print(x)
    # print(student_1[x])
    if x == "name":
        print(f"Your name is {student_1[x]}")
    elif x == "stream":
        print(f"You study {student_1[x]}")
    elif x == "completed_lessons":
        print(f"You completed {student_1[x]} lessons")
```

### Age calculator
```python
current_year = int(2022)
print("what is your age")
age = int(input())

birth_year = current_year - age

print (f"You were born in {birth_year}")
```
### Movie age restriction
```python
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

```

