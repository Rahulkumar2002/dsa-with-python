from jovian.pythondsa import evaluate_test_cases, evaluate_test_case

tests = []

test = {
    'input': {
        'cards': [13, 10, 7, 4, 3, 1, 0],
        'query': 7
    },
    'output': 2
}

tests.append(test)

# query in the middle of the list cards.

tests.append({
    'input': {
        'cards': [10, 9, 8, 4, 3, 2, 1],
        'query': 4
    },
    'output': 3
})

# query is the last element in the cards.

tests.append({
    'input': {
        'cards': [10, 9, 8, 4, 3, 2, 1],
        'query': 1
    },
    'output': 6
})

# list card contain one element which is query.

tests.append({
    'input': {
        'cards': [10, 9, 8, 4, 3, 2, 1],
        'query': 10
    },
    'output': 0
})

# list card doesn't contain number query.

# tests.append({
#     'input': {
#         'cards': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'],
#         'query': 9
#     },
#     'output': -1
# })

# list card is empty.

tests.append({
    'input': {
        'cards': [],
        'query': 7
    },
    'output': -1
})

# list cards containing repeating number.

tests.append({
    'input': {
        'cards': [10, 9, 9, 9, 9, 8, 4, 3, 3, 3, 3, 2, 1],
        'query': 4
    },
    'output': 6
})

# The number query occurs more than one position in the card.

tests.append({
    'input': {
        'cards': [10, 9, 9, 9, 9, 8, 4, 3, 3, 3, 3, 2, 1],
        'query': 4
    },
    'output': 6
})

# The number query occurs more than one position in the card.

tests.append({
    'input': {
        'cards': [10, 9, 9, 9, 8, 4, 4, 4, 4, 4, 3, 3, 3, 3, 2, 1],
        'query': 4
    },
    'output': 5
})

# Large test cases :

large_test = {
    'input': {
        'cards': list(range(10000000, 0, -1)),
        'query': 2
    },
    'output': 9999998
}

# Helper function for checking the first occurence of the query.
# Rule of thumb is a function shouldn't be more than 8 line of code.


def test_location(cards, query, mid):
    mid_number = cards[mid]
    # print(f"mid : {mid} , query : {query} , mid_number : {mid_number}")
    if (mid_number == query):
        if(mid-1 >= 0 and cards[mid-1] == query):
            return 'left'
        else:
            return 'found'
    elif (mid_number < query):
        return 'left'
    elif(mid_number > query):
        return 'right'


def locate_card(cards, query):
    lo, hi = 0, len(cards) - 1

    while lo <= hi:
        # print(f"lo : {lo} , hi : {hi}")
        mid = (lo + hi) // 2
        result = test_location(cards, query, mid)

        if(result == "found"):
            return mid
        elif(result == 'left'):
            hi = mid - 1
        elif(result == 'right'):
            lo = mid + 1
    return -1


# evaluate_test_cases(locate_card, tests)
result, passed, runtime = evaluate_test_case(
    locate_card, large_test, display=False)
print(f"result : {result} , passed : {passed} , runtime : {runtime}")
