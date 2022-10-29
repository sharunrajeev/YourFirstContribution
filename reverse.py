num = 1234
reversed = 0

while num != 0:
    digit = num % 10
    reversed = reversed * 10 + digit
    num //= 10

print("Reversed Number: " + str(reversed))
