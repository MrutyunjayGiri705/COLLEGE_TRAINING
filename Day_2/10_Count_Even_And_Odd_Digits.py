n = 12345678
digit_count = 0
even_count = 0
odd_count = 0

while n > 0:
    digit_count += 1
    digit = n % 10
    if digit % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
    n //= 10

print( digit_count)
print( even_count)
print( odd_count)
