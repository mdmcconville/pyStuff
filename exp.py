"""
Exponentiation

Calculates x^y where:
    y can be positive, negative, or 0,
    y cannot be fractional,
    x can be positive, negative, 0, or fractional,
    x can be 0 as long as y is not negative.

Currently, raising to roots is not supported.
"""

def power(x, y):
    if (x == 0) and (y < 0):
        print(x, " can't be raised to a negative power.", sep='')
        return
    # Base cases
    if y == 0:
        return 1.0
    elif y == 1:
        return x
    elif y == -1:
        return 1/x
    
    # General case
    # Can't use integer division because negative uses floor rounding
    if y < 0:
        temp = power(x, int(y/2))
    else:
        temp = power(x, y//2)
    # If the exp is evenly divided, multiply the halves
    if y % 2 == 0:
        return temp * temp
    # Multiply the halves times the base
    else:
        if (y >= 0):
            return x * temp * temp
        else:
            return (1/x) * temp * temp
