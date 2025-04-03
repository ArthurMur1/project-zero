def int_check(question):
    """Checks if the users enter an integer"""

    error = "Oops - please enter a integer"
    
    while True:

        try:
            response = int(input(question))

            return response
        
        except ValueError:
            print (error)

while True:
    print ()

    # ask user for their name
    name = input ("Name: ") # replace with call to 'not blank' function
    # asj for their age and check its between 12 and 120
    age = int_check ("Age: ")

    # output error message / success message
    if age < 12:
        print (f"{name} is too young")
        continue
    elif age > 120:
        print (f"name{name} is too old")
        continue
    else:
        print (f"{name} bought a ticket")

    