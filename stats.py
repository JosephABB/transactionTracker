import csv

def stats_funct():
    #if transaction data is loaded
    try:
        counter = 0
        usd = 0.0
        with open("transaction_records.csv", "r") as file:
            reader = csv.reader(file)
            for line in reader:
                counter += 1
                if line[2] == "PENDING":
                    usd += int(line[4])
            print("Number of lifetime transactions:", counter)
            print("Total dollar amount pending:", usd)
    except:
        print("Sorry, no transaction data was loaded yet. Please try again.")
