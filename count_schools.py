from tools import format_json, schools_parse

def print_counts():
    schools = schools_parse()

    unique_schools = 0
    total_schools:int = 0
    schools_by_state = {}
    schools_by_locale = {}
    schools_by_city = {}

    for school in schools:

        # row values
        city = school[4]
        state = school[5]
        locale = school[8]

        # How many total schools are in this data set?
        total_schools += 1

        # How many schools are in each state?
        if state in schools_by_state:
            schools_by_state[state] += 1
        else:
            schools_by_state[state] = 1

        # How many schools are in each Metro-centric locale?
        if locale in schools_by_locale:
            schools_by_locale[locale] += 1
        else:
            schools_by_locale[locale] = 1

        # collect city
        if city in schools_by_city:
            schools_by_city[city] += 1
        else:
            schools_by_city[city] = 1
            # How many unique cities have at least one school in it?
            unique_schools += 1

    # What city has the most schools in it? How many schools does it have in it?
    schools_by_city_sorted = sorted(schools_by_city.items(), key=lambda item: item[1], reverse=True)
    most_schools_by_city = schools_by_city_sorted[0]

    print(f'Total Schools: {total_schools}\n')
    print(f'Schools by State: {format_json(schools_by_state)}')
    print(f'Schools by Metro-centric locale: {format_json(schools_by_locale)}')
    print(f'City with most schools: {most_schools_by_city[0]} ({most_schools_by_city[1]} Schools)\n')
    print(f'Unique Schools: {unique_schools}\n')
