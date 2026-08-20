n = 67
Flag = False
for i in range(2,7):
    if n % i == 0:
        Flag = True
if Flag:
     print("not prime")
else:
     print("prime")