import time
from tools import schools_parse, state_name

lower_matches = ['school', 'high', 'elementary']

def search_schools(search: str):
    schools = schools_parse()

    start_time = time.perf_counter()

    search_text = search.lower()
    search_tokens = search_text.split()
    results:list[str] = []

    for school in schools:

        name = school[3]
        name_text = name.lower()
        name_tokens = name_text.split()

        city = school[4]
        city_text = city.lower()
        city_tokens = city_text.split()

        state = school[5]
        state_text = state_name(state.lower())
        state_tokens = state_text.split()

        school_tokens = []
        school_tokens.extend(name_tokens)
        school_tokens.extend(city_tokens)
        school_tokens.extend(state_tokens)
        school_tokens = list(set(school_tokens))

        # score the words
        score = 0
        for school_part in school_tokens:
            if school_part in search_tokens:
                # treat common values as a lower score
                if school_part in lower_matches:
                    score += 1
                else:
                    score += 2

        if score > 0:
            results.append({
                'name': name,
                'city': city,
                'state': state,
                'score': score,
                'search_tokens': search_tokens,
                'school_tokens': school_tokens,
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
