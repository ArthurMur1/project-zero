def num_check(question, num_type, exit_code=None):
    """Checks if the users enter an integer / float that is more than Zero"""
    
    if num_type == "integer":
        error = "Oops - plesae enter a integer more than zero"
        change_to  = int
    else:
        error = "Oops - please enter a number more than zero"
        change_to  = float
   
   
    while True:
        response = input(question).lower()

       #check for the exiting code
        if response == exit_code:
            return response
        

        try:
            #change the response to an integure and check that its more than zero
            response = change_to(response)

            if response > 0:
                return response
            else:
                print (error)
                       
        except ValueError:
            print (error)



#main routine

#loop for testing purposes
while True:
    print()

    my_float = num_check(question= "please enter a number more than 0: ", num_type= "float")
    print(f"Thanks you chose {my_float}")
    print()
    my_int = num_check(question= "Please enter an integer more than 0: ",
                       num_type="integer",exit_code="")
    
    if my_int == "":
        print ("you have chosen infinate mode.")
    else:
        print (f"thanks. you chose {my_int}")


