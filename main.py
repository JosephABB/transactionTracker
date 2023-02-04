import csv
import contLoop

print("Welcome to the transaction tracker!")
funct = input("What would you like to perform (import/statistics)? ")

#check if user wants to continue 
cont = True
#check if prompt is invalid
inv = False

while cont:
    if funct.lower().strip() == "import":
        #code for import function
        if inv == False:
            print("importing")
        cont, funct, inv = contLoop.cont_anlys()
    elif funct.lower().strip() == "statistics":
        #code for statistics function
        if inv == False:
            print("statistics-ing")
        cont, funct, inv = contLoop.cont_anlys()
    else:
        #input not valid
        print("INVALID FUNCTION")
        funct = input("What would you like to perform (import/statistics)? ")
        continue
        
print("Session terminated")
