def string_check (question, valid_answers=('yes', 'no'),
    num_letters=1):

def not_blank(question):

def int_check(question):

#main routine

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