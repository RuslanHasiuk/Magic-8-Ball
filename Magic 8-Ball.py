import random

name = 'Phil'
question = ''
# Will i earn my first million in 2022?
answer = ''

random_number = random.randint(1, 11)

print(f'random number is: {random_number}\n')  # it will print random int number from defined range

# Logic for answer depending of randomly generated value
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

# Logic to consider cases when some information of user is missing (name, question, both)
if len(name) == 0 and len(question) == 0:
    question = 'Hi there, how can we call you ?!'
elif not len(name) or name.isspace() and len(question) > 0:
    question = f'Question: {question}'
elif len(question) == 0 or question.isspace() and len(name) > 0:
    question = f'{name}, What do You need to know ?'
else:
    question = f'{name} asks: {question}'

# Change/remove the values for the variables "name", "question" and compare the difference in the printed result.
print(question)
print("Magic 8-Ball's answer:", answer)