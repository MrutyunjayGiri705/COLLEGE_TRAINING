n = 12345

s = str(n)


if len(s) == 1:
    result = n
else:
    
    swapped = s[-1] + s[1:-1] + s[0]
    result = int(swapped)

print("Original number:", n)
print("After swapping:", result)
