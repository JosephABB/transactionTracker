import csv

print("Welcome to the transaction tracker!")
funct = input("What would you like to perform (import/statistics)? ")
cont = True
inv = False

while cont:
    if funct.lower().strip() == "import":
        #code for import function
        if inv == False:
            print("importing")
        prompt = input(("Would you like to run any further analyses (yes/no)? "))
        if prompt.lower().strip() == "no":
            cont = False
            inv = False
            continue
        elif prompt.lower().strip() == "yes":
            funct = input("What would you like to perform (import/statistics)? ")
            inv = False
        else:
            print("INVALID RESPONSE")
            inv = True
    elif funct.lower().strip() == "statistics":
        #code for statistics function
        if inv == False:
            print("statistics-ing")
        prompt = input(("Would you like to run any further analyses (yes/no)? "))
        if prompt.lower().strip() == "no":
            cont = False
            inv = False
            continue
        elif prompt.lower().strip() == "yes":
            funct = input("What would you like to perform (import/statistics)? ")
            inv = False
        else:
            print("INVALID RESPONSE")
            inv = True
    else:
        #input not valid
        print("INVALID FUNCTION")
        funct = input("What would you like to perform (import/statistics)? ")
        continue
        
print("Session terminated")
