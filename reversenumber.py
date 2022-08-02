#Reverse an integer.
def reverNumber(num):
    rev = 0
    while num > 0 :
        digit  = num % 10
        rev = (rev*10) + digit
        num = num // 10
    return rev


num = 12345
print(reverNumber(num))
