# I want to be able to call capitalize_nested from main w/ various lists
# and get returned a new nested list with all strings capitalized.
# Ex. ['apple', ['bear'], 'cat']
# Verify you've tested w/ various nestings.
# In your final submission:
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()

def match_ends(words):
    count = 0

    for each in words:
        if len(each) >= 2 and each[0] == each[len(each)-1]:
            count += 1
        else:
            count += 0
    return count

    


##############################################################################
def main():
    pass  # Call your function(s) here.
    print(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']))

if __name__ == '__main__':
    main()

