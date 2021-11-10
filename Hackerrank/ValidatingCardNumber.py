import re

for i in range(int(input())):
    # removes spaces from beginning and end
    S = input().strip()
    # the "r" in the beginning is making sure that the string is being treated as a "raw string"
    pre_match = re.search(r'^[456]\d{3}(-?)\d{4}\1\d{4}\1\d{4}$',S)
    if pre_match:
        # If you call The group() method with no arguments at all or with 0 as an argument you will get the entire target string.
        # Removes the "-" 
        processed_string = "".join(pre_match.group(0).split('-'))
        # Gets a digit and verifies if the three or more digits coming after are the same
        final_match = re.search(r'(\d)\1{3,}',processed_string)
        if final_match:
            print('Invalid')
        else :
            print('Valid')
    else:
        print('Invalid')
