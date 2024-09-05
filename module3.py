calls = 0



def count_calls():
global calls
calls += 1
return calls


def string_info(string):
count_calls()
return (len(string), string.upper(), string.lower())


def is_contains(string, list_to_search):
count_calls()
new_string = string.lower()
new_ist_to_search = [s.lower() for s in list_to_search]
exam = new_string in new_ist_to_search
return exam


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)