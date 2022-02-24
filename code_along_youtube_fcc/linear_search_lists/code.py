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

tests.append({
    'input': {
        'cards': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'],
        'query': 9
    },
    'output': -1
})

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
        'cards': [10, 9, 9, 9, 9, 8, 4, 3, 4, 4, 3, 3, 3, 2, 1],
        'query': 4
    },
    'output': 6
})


def locate_card(cards, query):
    # Function no. zero
    # position = 0
    # if(len(cards) == 0):
    #     return -1
    # while True:
    #     if(cards[position] == query):
    #         return position

    #     position = position + 1

    #     if (position == len(cards)):
    #         return -1

    # Adding feature to check for empty cards deck :
    position = 0
    while position < len(cards):
        if(cards[position] == query):
            return position
        position += 1
    return -1


# def check_test_case(function, dictionary):
#     #     cards = dictionary['input']['cards']
#     #     query = dictionary['input']['query']
#     output = dictionary['output']

#     result = function(**dictionary['input'])
#     if(result == output):
#         return 'PASSED'
#     else:
#         return 'FAILED'


# ans = check_test_case(locate_card, test)

# print(ans)

# evaluate_test_case(locate_card, test)
evaluate_test_cases(locate_card, tests)
