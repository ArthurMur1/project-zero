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




    
