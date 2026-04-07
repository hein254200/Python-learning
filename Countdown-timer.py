num = int(input("Enter the number you want to count:"))
counter=1
if num<=0:
    print("invalid number!\n Please enter over 0.")
else:
    while counter<=num:
        print(f"countdown :{num}")
        num-=1
