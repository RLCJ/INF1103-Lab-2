#Activity 1

print("==================================")
print("Welcome here")
print("My first post!")
print("==================================")

#Activity 2

username = "Cool Guy"
bio = "I am a full time blogger!"
followers = 100
#print("Username:", username)
#print("Bio:", bio)
#print("Followers:", followers)

#Activity 3

followers += 50  # Increase followers by 50
print("Day 1 Update:", followers)

followers += 20  # Increase followers by 20
print("Day 2 Update:", followers)

followers -= 10  # Decrease followers by 10
print("Day 3 Update:", followers)

#Activity 4

#username = input("Enter your username: ")
#age = int(input("Enter your age: "))
#category = input("Enter your category: ")

#Activity 5

username = input("Enter Username: ")
age = int(input("Enter Age: "))
category = input("Enter Content Category: ")
print("\nInstagram Profile")
print("==================================")
print("Username:", username)
print("Age:", age)
print("Category:", category)

if age > 40 and category == "music":
    print("So old but a music lover!")
elif category == "music":
    print("You are into music!")
else:
    print("You are not into music..?")