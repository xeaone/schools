import time
from tools import schools, stateName

lowerMatches = ['school', 'high', 'elementary']
rows = schools()

def search_schools(search: str):
    start_time = time.perf_counter()

    searchText = search.lower()
    searchParts = searchText.split()
    results:list[str] = []

    for row in rows:

        name = row[3]
        nameText = name.lower()
        nameParts = nameText.split()

        city = row[4]
        cityText = city.lower()
        cityParts = cityText.split()

        state = row[5]
        stateText = stateName(state.lower())
        stateParts = stateText.split()

        compareParts = []
        compareParts.extend(nameParts)
        compareParts.extend(cityParts)
        compareParts.extend(stateParts)
        compareParts = list(set(compareParts))

        # score the strings and handle lower search values
        score = 0
        for comparePart in compareParts:
            if comparePart in searchParts:
                if comparePart in lowerMatches:
                    score += 1
                else:
                    score += 2

        if score > 0:
            results.append({
                'name': name,
                'city': city,
                'state': state,
                'score': score,
                'searchParts': searchParts,
                'compareParts': compareParts,
            })

    results.sort(key=lambda item: item['score'], reverse=True)

    # print results
    end_time = time.perf_counter()
    process_time = round(end_time - start_time, 3)

    print(f'\nResults for "{search}" (search took: {process_time}s)')

    position = 0
    for result in results:
        position += 1
        print(f'{position}. {result["name"]}\n\t{result["city"]}, {result["state"]}')
        if position == 3: break
