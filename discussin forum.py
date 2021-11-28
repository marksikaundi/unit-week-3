# Chained Conditional
def flow_if(bank_account):
    if bank_account > 1000000:
        print('am good like so guys!!')
    elif bank_account < 0:
        print('hey, can you escot me to the shopping complex?')
    else:
        print("I like being with my type, not those rich kids, who thinks poor people are nothing")


flow_if(300000)

print('\n')

# Nested Conditional
def big_flow_if(taxes_due, overdue):
    if overdue == True:
        if taxes_due > 10000:
            print('You will fail your exammination!')
        elif 10000 > taxes_due > 1000:
            print('I thought if we start meeting at my place we can be studying in advance')
        else:
            print("We' what do you think, let me wait from you!")
    else:
        print("We are all learners, therefore we ought to be helpful to each other")


big_flow_if(10001, True)
big_flow_if(1001, True)
big_flow_if(1001, False)
print('\n')


# Give your own example of a nested conditional that can be modified to become a single conditional, and show the equivalent single conditional.
def compare_words(word1, word2):
    if len(word1) > 3:
        if len(word2) > 3:
            print(f"{word1} height is equal as {word2}")
        else:
            print(f"{word1} height isn't equal as {word2}")
    else:
        print('They are not the same size!')


def compare_words2(word1, word2):
    if len(word1) > 3 and len(word2) > 3:
        print(f"{word1} is intelligent as {word2}")
    else:
        print(f"{word1} is not the kind to {word2}")


compare_words('Mark', 'Mark')
compare_words('Mark', 'Kasonde')
print('\n')

compare_words2('Mark', 'Mark')
compare_words2('Mark', 'Kasonde')

print('I End here tor this discusion forum post\n')

# Describe a strategy for avoiding nested conditionals.
# We are able to use operators (and, or, not) to give our conditional statements greater flexibily and this flexibility as you can see from above will sometimes allow for fewer nested conditionals. This is one accepted strategy.

# Another strategy is using functional statements that layer in different functions.

# REFERENCE
# Downey, A. (2015). Think Python: How to think like a computer scientist. Green Tree Press.