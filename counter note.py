print("Welcome to the notecounter from ALLIED BANK")
amount=int(input("Enter the amount") )
Note_1000=amount//1000
Note_500=(amount % 1000)//500
Note_100=((amount % 1000)% 500)//100
print("No. of 1000 note:")