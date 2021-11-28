# Chained Conditional
def flow_if(bank_account):
    if bank_account > 1000000:
        print('Bye bye suckers!!')
    elif bank_account < 0:
        print('Will any suckers loan me money?')
    else:
        print("We are all poor together! Let's party in a park over marshmellows.")


flow_if(300000)

print('\n')

# Nested Conditional
def big_flow_if(taxes_due, overdue):
    if overdue == True:
        if taxes_due > 10000:
            print('You are going to jail soon!')
        elif 10000 > taxes_due > 1000:
            print('We are thinking your car would look nice in our inspectors yard')
        else:
            print("We'll give you some time, before we call the cops!")
    else:
        print("We are all friends, but don't ever be late")


big_flow_if(10001, True)
big_flow_if(1001, True)
big_flow_if(1001, False)
print('\n')


# Give your own example of a nested conditional that can be modified to become a single conditional, and show the equivalent single conditional.
def compare_words(word1, word2):
    if len(word1) > 3:
        if len(word2) > 3:
            print(f"{word1} is equal in size to {word2}")
        else:
            print(f"{word1} isn't equal in size to {word2}")
    else:
        print('They are not the same size!')


def compare_words2(word1, word2):
    if len(word1) > 3 and len(word2) > 3:
        print(f"{word1} is equal in size to {word2}")
    else:
        print(f"{word1} isn't equal in size to {word2}")


compare_words('jeff', 'jeff')
compare_words('jeff', 'jennifer')
print('\n')

compare_words2('jeff', 'jeff')
compare_words2('jeff', 'jennifer')

print('-----------------\n')