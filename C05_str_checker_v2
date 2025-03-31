def int_check(question, low, high=None):
    """Checks if the users enter an integer between 2 values"""

    error = "Oops - please enter a integer between {low} and {high}"
    
    while True:

        try:
            #change the response to an integure and check that its more than zero
            response = int(input(question))

            if low <= response <= high:
                return response
            else:
                print (error)
                       
        except ValueError:
            print (error)


#main routine

#loop for testing
while True:
    print ()

    #ask user for an integer
    my_num = int_check(question= "Choose a number: ", low=1, high=10)
    print(f"You chose {my_num}")

    