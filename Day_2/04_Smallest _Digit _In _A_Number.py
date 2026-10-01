n=58329
l=9
while n>0:
    digit=n%10
    if l>digit:
        l=digit
    n=n//10

print(l)