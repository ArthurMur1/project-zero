#functions here
question = "Name? "
def name (question):
#checks the user adds a yes no answerA

 while True:
    response = input(question).lower()

    if response == "a":
      return "A" 
    elif response == "b":
      return "B"
    elif response == "c":
      return "C" 
    elif  response == "d":
      return "D"
    elif response == "xxx":
     break  
    else:
      print ("You have sold {response} / 5 \n")
    


print(name(question))