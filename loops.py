
list_data = [1, 2, 3, 4, 5]

print(list_data)

# for loops

for number in list_data:
    if number == 3:
        print ("found 3")
    elif number > 3:
        print ("you have passed 3")
    else:
        print ("too soon")


student_1 = {
    "name": "Mohamed",
    "stream" : "DevOps",
    "completed_lessons" : 4

}

# create a dictionary student data
# iterate through the dict
# loop print all keys
# print values and keys

for x in student_1:
    # print(x)
    # print(student_1[x])
    if x == "name":
        print(f"Your name is {student_1[x]}")
    elif x == "stream":
        print(f"You study {student_1[x]}")
    elif x == "completed_lessons":
        print(f"You completed {student_1[x]} lessons")
















