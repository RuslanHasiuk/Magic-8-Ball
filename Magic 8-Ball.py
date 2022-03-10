import random

print('''What if the asker does not provide a name, such that the value of name is an empty string?
Let\'s add logic for this:
- If the name is an empty string or string is a whitespace -  it will only print the question.
- Else, the player’s name and question are both printed.
''')

name = ' '
question = 'Will i earn my first million in 2022?'
answer = ''

random_number = random.randint(1, 11)

print(f'random number is: {random_number}\n') #it will print random int number from defined range

if not len(name) or name.isspace():
    question = f'Question: {question}'
else:
    question = f'{name} asks: {question}'


if random_number == 1:
  answer = "Yes - definitely"
elif random_number == 2:
  answer = "It is decidedly so"
elif random_number == 3:
  anwer = "Without a doubt."
elif random_number == 4:
  answer = "Reply hazy, try again."
elif random_number == 5:
  answer = "Ask again later."
elif random_number == 6:
  answer = "Better not tell you now."
elif random_number == 7:
  answer = "My sources say no."
elif random_number == 8:
  answer = "Outlook not so good."
elif random_number == 9:
  answer = "Very doubtful."
elif random_number == 10:
  answer = "ooh yup baby"
elif random_number == 11:
  answer = 'Hm, nice question'
else:
   answer = "Error"

print(question)
print("Magic 8-Ball's answer:", answer)

