num = int(input("Enter a number: "))
sum_divi= 0

for i in range(1, num):
    if num % i == 0:
        sum_divi += i

if sum_divi== num:
    print( "Perfect Number")
else:
    print( "Not a Perfect Number")
