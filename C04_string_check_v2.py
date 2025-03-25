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
levels = ['easy', 'medium', 'hard']

like_coffee = string_check (question="Do you like coffee? ", valid_ans_list=['yes', 'no'])
print (f"You chose {like_coffee}")
choose_level = string_check (question= "Choose a level: ", valid_ans_list=['easy', 'medium', 'hard'])
print (f"You chose {choose_level}")