def exponent(basenumber, powernumber ):
    result = 1
    for index in range(powernumber):
        result *= basenumber
    return result


print(exponent(2, 3))
print(exponent(2, 2))
print(exponent(5, 2))
