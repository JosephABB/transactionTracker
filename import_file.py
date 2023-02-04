import csv

def imp(csv_file):
    #open main csv file
    with open("transaction_records.csv", 'a') as file:
         writer = csv.writer(file, lineterminator = "\n")

         #open new csv file
         with open(csv_file, "r") as new_file:
            reader = csv.reader(new_file)
            #iterate through new file and append to old file
            for row in reader:
                writer.writerow(new_file)
        
        #close old file
         file.close()



        

