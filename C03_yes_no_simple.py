#functions here
def yes_no (question):
#checks the user adds a yes no answer

 while True:
    response = input (question).lower()

    if response == "yes" or response == "y":
      return "yes" 
    elif response == "no" or response == "n":
      return "no"
    elif response == " ":
     break
    else:
      print ("please enter yes (y) or no (n). \n")
    

#main Routine
while True:
  want_instructions = yes_no ('do you want to read the instructions? ')
  print (f"you chose {want_instructions}\n")