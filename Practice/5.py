from random import choice

list = ["Snake", "Water", "Gun"]

User = int(input("Enter your choice---"))
user = list[User]
choice_list = [0, 1, 2]
computer = choice(choice_list)

print(f"user---{user}")
print(f"computer---{list[computer]}")

if user == computer:
    print("Draw")
elif ((user == list[0] and computer == list[2]) or (user == list[1] and computer == list[0]) or (user == list[2] and computer == list[1])):
    print("Lose")
else:
    print("Win")
