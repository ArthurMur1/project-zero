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

like_coffee = string_check (question="Do you like coffee? ", valid_ans_list=['yes', 'no'], num_letters=1 )

print (f"You chose {like_coffee}")
pay_method = string_check (question= "Payment Method: ", valid_ans_list=['card', 'cash'],num_letters=2)
print (f"You chose {pay_method}")


CHILD_PRICE = 7.50
ADULT_PRICE = 18.50
SENIOR_PRICE = 6.50
CREDIT_SURCHARGE = 0.05

#list to hold ticket detail
all_names = []
all_ticket_cost = []
all_surcharges = []

mini_movie_dict = {
    'Name': all_names,
    'Ticket Price': all_ticket_cost,
    'Surcharge': all_surcharges
}

make_statement (statement= "Mini-Movie Fundraser")

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

def int_check(question):

#main routine
    def currency(x):
        return "${:.2f}".format(x)
#initialise ticket numbers
MAX_TICKETS = 5
tickets_sold = 0

#initialise variables
payment_ans = ('cash', 'credit')



make_statement(statement= "Mini-Movie Fundraiser Program", decoration="🍿" )

print()
want_instructions = string_check("Do you want to see the instructions")

if want_instructions == 'yes':
    instructions()

print()

while tickets_sold < MAX_TICKETS:
    name = input ("Name: ")

    #if name is exit code, break out of loop
    if name == "xxx":
        break

    tickets_sold +=1

    if tickets_sold == MAX_TICKETS:
        print(f"You have sold all the tickets (ie: {MAX_TICKETS} tickets")
    else:
        print (f"You have sold {tickets_sold} / {MAX_TICKETS} tickets.")