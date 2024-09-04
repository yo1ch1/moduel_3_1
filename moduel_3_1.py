calls = 0

def count_calls():
    global calls
    calls += 1


def string_info(sting):
    count_calls()
    list_1= []
    long = len(sting)
    up = sting.upper()
    low = sting.lower()
    list_1.append(long)
    list_1.append(up)
    list_1.append(low)
    return (tuple(list_1))


def is_contains(string, list_to_search):
    count_calls()
    a = string.lower()
    b = list_to_search_1 = [a.lower() for a in list_to_search]
    if a in b:
        i = True
    else:
        i = False
    return (i)


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)

