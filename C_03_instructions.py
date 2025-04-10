
def make_statement(statement, decoration):






def string_check(question, valid_answers=('yes','no'),
                num_letters=1):
    def string_check(question, valid_ans_list, num_letters):
    """Checks if the users enter the full word or the first letter of a word from a list of valid responses"""


    while True:

        response = input (question).lower()

        for item in valid_ans_list:

            #check if response is the whole word
            if response == item:
                return item
            
            #check if its the 'n' letters
            elif response == item[:num_letters]:
                return item
            
        print (f"Please choose an option from {valid_ans_list}")


def instructions():
make_statement(statement="Instrutions",decoration="ℹ️")

print
        
#maim routine

make_statement(statement= "Mini-Movie Fundraiser Program", decoration="🍿" )

print()
want_instructions = string_check("Do you want to see the instructions")

if want_instructions == 'yes'
    instructions()

print("program continues...")