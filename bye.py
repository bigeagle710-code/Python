Valid = False
while not Valid:
    try:
      n=int(input("Enter a no.: "))
      while n%2==0:
       print("bye")
       valid=True
    except ValueError:
        print("It is invalid")     
   