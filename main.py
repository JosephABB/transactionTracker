import csv

print("Welcome to the transaction tracker!")
funct = input("What would you like to perform (import/statistics)? ")
cont = True
inv = False

while cont:
    inv = False
    if funct.lower().strip() == "import":
        #code for import function
        print("importing")
        prompt = input(("Would you like to run any further analyses (yes/no)? "))
        if prompt.lower().strip() == "no":
            cont = False
            continue
        else:
            funct = input("What would you like to perform (import/statistics)? ")
            continue
    elif funct.lower().strip() == "statistics":
        #code for statistics function
        print("statistics-ing")
        prompt = input(("Would you like to run any further analyses (yes/no)? "))
        if prompt.lower().strip() == "no":
            cont = False
            continue
        else:
            funct = input("What would you like to perform (import/statistics)? ")
            continue
    else:
        #input not valid
        print("INVALID FUNCTION")
        funct = input("What would you like to perform (import/statistics)? ")
        continue
        
print("Session terminated")
