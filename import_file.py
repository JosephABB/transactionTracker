import csv

def imp():
    #which file to import
    new_csv = input("\nWhich file would you like to import? ")
    counter = 0

    try:
        #open new file as read and old file as append
        with open(new_csv, 'r') as in_file, open("transaction_records.csv", 'a', newline='') as out_file:
            reader = csv.reader(in_file)
            writer = csv.writer(out_file)

            # create list of value in current records
            list_lines = []
            with open("transaction_records.csv", "r") as current_file:
                reader_old = csv.reader(current_file)
                for line in reader_old:
                    list_lines.append(line)
            current_file.close()

            #check if new file contains id's already in old file
            for line in reader:
                # skip duplicate
                if any(line[0] in sublist for sublist in list_lines): 
                    print("Data for ID", line[0], "already in transaction records.")
                    continue
                else:
                    counter += 1
                    writer.writerow(line)
                    list_lines.append(line)
        out_file.close()
        in_file.close()

        print(counter, "transaction records successfully loaded.")
    except:
        print("Sorry, that file could not be found. Please try again.") 
        



        

