import random as r

# list of repsonse 
myResponse = ['IT IS CERTAIN', 'YOU MAY RELY ON IT', 'AS I SEE IT, YES', 'OUTLOOK LOOKS GOOD',
              'MOST LIKELY', 'IT IS DECIDELY SO', 'WITHOUT A DOUBT', 'YES, DEFINETLY']

# input from user 
myQuestion = input("What is your question ? \n").lower()

# logic to ansewer and continue asking questions
while myQuestion != "":
    num = r.randint(0, len(myResponse)-1)
    print(myResponse[num])
    myQuestion = input("What is your question ? \n").lower()
else:
    print("A valid response was not entered.")
