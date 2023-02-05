def cont_anlys():
    iterate = True
    while iterate:
        prompt = input(("\nWould you like to run any further analyses (yes/no)? "))
        if prompt.lower().strip() == "no":
            cont = False
            funct = None
            inv = False
            iterate = False
            return (cont, funct, inv)
        elif prompt.lower().strip() == "yes":
            cont = True
            funct = input("\nWhat would you like to perform (import/statistics)? ")
            inv = False
            iterate = False
            return (cont, funct, inv)
        else:
            print("INVALID RESPONSE")

