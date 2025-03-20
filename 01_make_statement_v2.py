#Function
def make_statement(statement, decoration, lines=1):
    """Creates heading (3 lines), subheadings (2 lines and emphasied text / mini-headings (1 line), Only use emoji for single line statements"""

    middle = f"{decoration * 3} {statement} {decoration * 3}"
    top_bottom = decoration * len(middle)   

    if lines == 1:
        print (middle)
    elif lines == 2:
        print (middle)
        print (top_bottom)

    else:
        print (top_bottom)
        print (middle)
        print (top_bottom)





#Main Routine
make_statement ( statement= "Programming is fun,", decoration= "=",)
make_statement ( statement= "Programming is Still Fun!", decoration= "*",)
make_statement ( statement= "Emoji in action,", decoration= "😎",)
