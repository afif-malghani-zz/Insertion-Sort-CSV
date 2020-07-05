# Import external modules
import insertion
import csv

# create list to recieve data
extracted_data = []

# extract data into list
with open('file.csv') as f:
    data = csv.reader(f)
    for row in data:
        extracted_data.append(row)

while(1):
    print("Chose colomn to sort:")

    # Increase the number of columns to match the input file
    print("1. " + str(extracted_data[0][1]) + "\n" +"2. " + str(extracted_data[0][2]) + "\n" + "Enter `e` as an input to exit")
    try:
        choice = int(input(""))
        if choice >=1 and choice < 3:
            isorted = insertion.Sort(extracted_data, choice)
        else:
            print("invalid column number")
    except:
        if choice == "e" or choice == "E":
            break
        else:
            print("Invalid input")