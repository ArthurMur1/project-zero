#functions here
check = ['A','B','C','D','E']
question = "Name? "
def name (question):
 response_amount = '5'
#checks the user adds a yes no answerA

 while True:
    response = input(question).lower()

    if response == "a" or response == "b" or response == "c" or response == "d":
      response = response_amount
      print ("You have sold" + {response_amount} + " a/ 5 \n")
      for item in check:
        print ( response + " / 5")


print(name(question))