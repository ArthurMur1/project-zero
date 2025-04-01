def int_check(question):
    """Checks if the users enter an integer that is more than 0"""

    error = "Oops - please enter a integer more than 0"
    
    while True:
        response = input(question).lower()
        
        try:
            #change the response to an integer and check its more than 0
            response = int(response)
        
            return response
        
        except ValueError:
            print(error)

#main routine

#loop for testing
while True:
    print ()

    #ask user for their name
    name = input ("Name: ")
    # ask their age and check its between 12 and 120
    age = int_check("Age: ")

    #output error message / success message
    if age < 12:
        print(f"{name} is too young")
    elif age > 120:
        print(f"{name} is to0 old")
        con
    else:
        print(f"{name} bought a ticket")
        
:

    