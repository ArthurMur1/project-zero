def not_blank (question):
    """Checks the users answer isnt blank"""

    while True:
        response = input(question)

        if response != "":
            return response
        
        print ("sorry this can't be blank. Please try again.\n")



#main routine starts here
who = not_blank ("please enter your name: ")
print (f"hello {who}")