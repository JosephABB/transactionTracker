import import_file
import stats
import cont_loop

print("Welcome to the transaction tracker!")
funct = input("\nWhat would you like to perform (import/statistics)? ")

#check if user wants to continue 
cont = True
#check if prompt is invalid
inv = False

while cont:

    #code for import function
    if funct.lower().strip() == "import":
        if inv == False:
            import_file.imp()
        cont, funct, inv = cont_loop.cont_anlys()

    #code for statistics function
    elif funct.lower().strip() == "statistics":
        if inv == False:
            stats.stats_funct()
        cont, funct, inv = cont_loop.cont_anlys()

    #input not valid
    else:
        print("INVALID FUNCTION")
        funct = input("What would you like to perform (import/statistics)? ")
        continue
        
print("Session terminated")
