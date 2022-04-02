import csv

"""
This example assumes the CSV file is in the same directory as the
this script.
"""
with open("MOCK_DATA.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)