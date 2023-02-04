import import_file
import stats
import cont_loop

print("Welcome to the transaction tracker!")
funct = input("What would you like to perform (import/statistics)? ")

#check if user wants to continue 
cont = True
#check if prompt is invalid
inv = False

while cont:
    #code for import function
    if funct.lower().strip() == "import":
        if inv == False:
            print("importing")
        cont, funct, inv = cont_loop.cont_anlys()
    #code for statistics function
    elif funct.lower().strip() == "statistics":
        if inv == False:
            print("statistics-ing")
        cont, funct, inv = cont_loop.cont_anlys()
    #input not valid
    else:
        print("INVALID FUNCTION")
        funct = input("What would you like to perform (import/statistics)? ")
        continue
        
print("Session terminated")
