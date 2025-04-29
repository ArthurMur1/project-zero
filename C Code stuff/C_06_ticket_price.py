

#main routine

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

    print (f"{name}'s ticket cost ${ticket_price:.2f}, they paid by {payment_method} "
           f"so the surcharge is ${surcharge:.2f}/n"
           f"The total payable is ${total_to_pay:.2f}/n")