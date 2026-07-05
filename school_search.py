import time
from tools import schools, state_name

lower_matches = ['school', 'high', 'elementary']
rows = schools()

def search_schools(search: str):
    start_time = time.perf_counter()

    search_text = search.lower()
    search_parts = search_text.split()
    results:list[str] = []

    for row in rows:

        name = row[3]
        name_text = name.lower()
        name_parts = name_text.split()

        city = row[4]
        city_text = city.lower()
        city_parts = city_text.split()

        state = row[5]
        state_text = state_name(state.lower())
        state_parts = state_text.split()

        compare_parts = []
        compare_parts.extend(name_parts)
        compare_parts.extend(city_parts)
        compare_parts.extend(state_parts)
        compare_parts = list(set(compare_parts))

        # score the strings and handle lower search values
        score = 0
        for compare_part in compare_parts:
            if compare_part in search_parts:
                if compare_part in lower_matches:
                    score += 1
                else:
                    score += 2

        if score > 0:
            results.append({
                'name': name,
                'city': city,
                'state': state,
                'score': score,
                'search_parts': search_parts,
                'compare_parts': compare_parts,
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
