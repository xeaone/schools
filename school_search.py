from tools import format, schools, stateName

lowerMatches = ['school', 'high', 'elementary']

def search_schools(search: str):
    searchText = search.lower().strip()
    searchText = searchText.replace(',')
    searchParts = searchText.split()

    results:list[str] = []
    rows = schools()

    for row in rows:

        name = row[3]
        nameText = name.lower().strip()
        nameParts = nameText.split()

        city = row[4]
        cityText = city.lower().strip()
        cityParts = cityText.split()

        state = row[5]
        stateText = stateName(state.lower().strip())
        stateParts = stateText.split()

        compareParts = []
        compareParts.extend(nameParts)
        compareParts.extend(cityParts)
        compareParts.extend(stateParts)
        compareParts = list(set(compareParts))

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

    position = 0
    for result in results:
        position += 1
        print(f'{position}. {result["name"]}\n\t{result["city"]}, {result["state"]}')
        if position == 3: break
        # print(format(result))
