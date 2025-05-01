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


#initialise variables / non default options for string checker
payment_ans = ('cash','credit')
#loop for test
while True:
    print()

    #ask for their name (and check its not blank)
    name = not_blank ("Name: ")

    #ask for their age and check its berween 12 and 120
    age = num_check ("Age: ")

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

#initialise ticket numbers
    payment_ans = ('cash', 'credit')

    #Ticket Price List
    CHILD_PRICE = 7.50
    ADULT_PRICE = 10.50
    SENIOR_PRICE = 6.50

    # credit card surcharge (currently 5%)
    CREDIT_SURCHARGE = 0.05

    #loop for testing purposes...
    while True:
        print()
        if age < 12:
            print (f"{name} is too young")
            continue

        #child ticket price is $7.50
        elif 12 <= age < 16:
            ticket_price = CHILD_PRICE

        #adult ticket price is ($10.50)
        elif 16 <= age < 65:
            ticket_price = ADULT_PRICE

        #senior citizen ticket ($6.50)
        elif 65 <= age < 121:
            ticket_price = SENIOR_PRICE

        else:
            print(f"{name} is too old")
            continue

        #ask user for paymrnt method (cash / credit / ca / cr)
        if pay_method == "cash":
            surcharge = 0

        #if paying by credit, calculate surcharge
        else:
            surcharge = ticket_price * CREDIT_SURCHARGE

    #calculate total payable...
        total_to_pay = ticket_price + surcharge

        print (f"{name}'s ticket cost ${ticket_price:.2f}, they paid by {pay_method} "
            f"so the surcharge is ${surcharge:.2f}/n"
            f"The total payable is ${total_to_pay:.2f}/n")
    
    