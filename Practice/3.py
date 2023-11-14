Questions = ['What is your dream?', 'What will u sacrifice for it?']
Answers = ['A.I.', 'life']
price = 0

for i in range(len(Questions)):
    print(Questions[i])
    solution = input('Answer, please: ')
    if solution == Answers[i]:
        price += 100
        print("Correct!")
    else:
        print("Incorrect.")

print("Congratulations! You've earned", price, "$")
