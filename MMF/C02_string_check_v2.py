def int_check(question):
    def not_blank(question):




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

#initialise variables / non default options for string checker
payment_ans = ('cash','credit')

#loop for test
while True:
    print()

    #ask for their name (and check its not blank)
    name = not_blank ("Name: ")

    #ask for their age and check its berween 12 and 120
    age = int_check ("Age: ")

    #output error message / success message
    if age < 12:
        print(f"{name} is too young ")
        continue
    elif age > 120:
        print (f"{name} is too old")
        continue
    else:
        pass

    # ask user for the payment method (cash / credit / ca / cr)
    pay_method = string_check (question= "Payment Method: ", payment_ans, num_letters=2)
    print (f"{name} Has bought a ticket ({pay_method})")














# want_instructions = string_check ("Do you want to see the instructions? ")
# print (f"You chose {want_instructions}")
# pay_method = string_check (question= "Payment Method: ", payment_ans ,num_letters=2)
# print (f"You chose {pay_method}")




    
