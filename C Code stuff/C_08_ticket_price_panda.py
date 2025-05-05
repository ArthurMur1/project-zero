import pandas
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


def string_check(question, valid_ans_list, num_letters):
    """Checks if the users enter the full word"""


    while True:

        response = input (question).lower()

        for item in valid_ans_list:

            #check if response is the whole word
            if response == item:
                return item
            
            #check if its the first letter
            elif response == item[ :num_letters]:
                return item
                        
        print (f"Please choose an option from {valid_ans_list}")


#main routine here
yes_no_list = ['yes', 'no']
payment_list = ['cash','credit']

like_coffee = string_check (question="Age?  ", valid_ans_list=['yes', 'no'], num_letters=1 )

print (f"You chose {like_coffee}")
pay_method = string_check (question= "Payment Method: ", valid_ans_list=['card', 'cash'],num_letters=2)

if pay_method == "cash":
    surcharge = 0

payment_ans = ('cash', 'credit')

#ticket price list
CHILD_PRICE = 7.50
ADULT_PRICE = 10.50
SENIOR_PRICE = 6.50

#CREDIT CARD SURCHARGE (currently 5%)
CREDIT_SURCHARGE = 0.5


all_names = []
all_ticket_costs = []
all_surcharges = []

mini_movie_dict = {
    'Name': all_names,
    'Ticket Price': all_ticket_costs,
    'Surcharge': all_surcharges
}
#loop for testing

#coming back to this later