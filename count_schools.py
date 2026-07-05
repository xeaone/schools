from tools import format, schools

def print_counts():
    rows = schools()

    uniqueSchools = 0
    totalSchools:int = 0
    schoolsByState = {}
    schoolsByLocale = {}
    schoolsByCity = {}

    for row in rows:

        # row values
        city = row[4]
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

        # collect city
        if city in schoolsByCity:
            schoolsByCity[city] += 1
        else:
            schoolsByCity[city] = 1
            # How many unique cities have at least one school in it?
            uniqueSchools += 1

        # print(row)

    # What city has the most schools in it? How many schools does it have in it?
    schoolsByCitySorted = sorted(schoolsByCity.items(), key=lambda item: item[1], reverse=True)
    mostSchoolsByCity = schoolsByCitySorted[0]

    print(f'Total Schools: {totalSchools}')
    print(f'Schools by State: {format(schoolsByState)}')
    print(f'Schools by Metro-centric locale: {format(schoolsByLocale)}')
    print(f'City with most schools: {mostSchoolsByCity[0]} ({mostSchoolsByCity[1]} Schools)')
    print(f'Unique Schools: {uniqueSchools}')
