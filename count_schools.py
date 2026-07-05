import csv

# read file with correct encoding
stream = open('./school_data.csv', encoding='cp1252', newline='')
reader = csv.reader(stream, delimiter=' ', quotechar='|')

# How many total schools are in this data set?
# How many schools are in each state?
# How many schools are in each Metro-centric locale?
# What city has the most schools in it? How many schools does it have in it?
# How many unique cities have at least one school in it?

def print_counts():

    for row in reader:
        print(', '.join(row))

print_counts()