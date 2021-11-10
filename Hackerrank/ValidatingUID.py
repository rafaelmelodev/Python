# Validating Unique Identification Number (UID)

# Number of inputs
n = input() 

i = 0

while (i < int(n)):
    # Receive new UID
    UID = input()
    # Capital letters
    cap = 0
    # Digits
    dig = 0
    Verification = "Invalid"
    # Number of characters
    NumberCharac = len(UID)
    # Check if it is alpha numeric
    alfaNumeric = UID.isalnum()
    
    # Number of upper letters
    for c in UID:
        if c.isupper():
            cap += 1
    # Number of digits
    for d in UID:
        if d in "0123456789":
            dig += 1
    
    # Verifying the validity
    if cap >= 2:
        if dig >= 3:
            if NumberCharac == 10:
                if alfaNumeric:
                    if len(set(UID)) == len(UID): # No repeated characters
                        Verification = "Valid"
    
    i += 1
    print(Verification)