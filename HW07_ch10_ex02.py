# I want to be able to call capitalize_nested from main w/ various lists
# and get returned a new nested list with all strings capitalized.
# Ex. ['apple', ['bear'], 'cat']
# Verify you've tested w/ various nestings.
# In your final submission:
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()

def capitalize_nested(nested_list):
    new = []
    for each in nested_list:
        if isinstance(each, list):
            new.append(capitalize_nested(each))
        else:
            new.append(each.upper())
    return new



    


##############################################################################
def main():
    pass  # Call your function(s) here.
    print(capitalize_nested(['apple', ['bear'], 'cat']))

if __name__ == '__main__':
    main()

