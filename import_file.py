import csv

def imp():
    #which file to import
    new_csv = input("Which file would you like to import? ")

    #open new file as read and old file as append
    with open(new_csv, 'r') as in_file, open("transaction_records.csv", 'a') as out_file:
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
                print(line[0], " is a duplicate")
                continue
            else:
                writer.writerow(line)
                list_lines.append(line)

    print("imported")

    out_file.close()
    in_file.close()



        

