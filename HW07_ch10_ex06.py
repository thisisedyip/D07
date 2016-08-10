# I want to be able to call is_sorted from main w/ various lists and get
# returned True or False.
# In your final submission:
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()

def is_sorted(input_list):
	input_sort = sorted(input_list)
	if input_sort == input_list:
		return True
	else:
		return False




##############################################################################
def main():
    pass  # Call your function(s) here.
    is_sorted([1, 2, 2])
    is_sorted(['b', 'a'])

if __name__ == '__main__':
    main()


    
