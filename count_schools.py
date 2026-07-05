import csv
import json
from tools import format

# read file with correct encoding
stream = open('./school_data.csv', encoding='cp1252', newline='')
reader = csv.reader(stream, delimiter=',')

# What city has the most schools in it? How many schools does it have in it?
# How many unique cities have at least one school in it?

def print_counts():

    headers:list[str] = None

    totalSchools:int = 0
    schoolsByState = {}
    schoolsByLocale = {}
    mostSchools = 

    for row in reader:

        # capture headers and skip counting
        if not headers:
            headers = row
            print(headers)
            continue

        if len(headers) != len(row):
            raise Exception('row length not valid')

        # row values
        state = row[5]
        locale = row[8]

        # if locale == 'N': print(row)

        # How many total schools are in this data set?
        totalSchools+=1

        # How many schools are in each state?
        if state in schoolsByState:
            schoolsByState[state] += 1
        else:
            schoolsByState[state] = 1

        # How many schools are in each Metro-centric locale?
        if locale in schoolsByLocale:
            schoolsByLocale[locale] += 1
        else:
            schoolsByLocale[locale] = 1


        # print(row)

    print(f'Total Schools: {totalSchools}')
    print(f'Schools by State: {format(schoolsByState)}')
    print(f'Schools by Metro-centric locale: {format(schoolsByLocale)}')

print_counts()