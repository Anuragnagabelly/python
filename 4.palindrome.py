data=input("Enter a word")
temp=0
l=len(data)-1
for i in range(l):
    if(data[i]!=data[l-i]):
        break
    temp=temp+1
if(temp==l):
    print("palindrome")
else:
    print("not palindrome")
        
