def string_check(question, valid_answers=('yes','no'),
                 num_letters=1):
    """Checks if the users enter the full word or the 'n' letters/s of a word from a list of valid responses """


    while True:

        response = input (question).lower()

        for item in valid_answers:

            #check if response is the whole word
            if response == item:
                return item
            
            #check if its the first letter
            elif response == item[ :num_letters]:
                return item
                        
        print (f"Please choose an option from {valid_ans_list}")


#main routine here
payment_ans = ['cash','credit']

want_instructions = string_check ("Do you want to see the instructions? ")
print (f"You chose {want_instructions}")
pay_method = string_check (question= "Payment Method: ", payment_ans ,num_letters=2)
print (f"You chose {pay_method}")




    
