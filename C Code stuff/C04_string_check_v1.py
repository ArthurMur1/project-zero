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


#main routine here
yes_no_list = ['yes', 'no']
payment_list = ['cash', 'credit']

like_coffee = string_check (question="Do you like coffee? ",
                            yes_no_list , num_letters=1)
print (f"You chose {like_coffee}")
choose_level = string_check (question= "Choose a level: ", valid_ans_list=['easy', 'medium', 'hard'])
print (f"You chose {choose_level}")