n=int(input())
a=int(input())
least_number=a
for i in range (n-1):
    b=int(input())
    if b<least_number:
        least_number=b
print(least_number)
