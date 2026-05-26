try:
   number = int(input("Enter the no.: "))
   print("Number entered is",number)

except ValueError as ex:
   print("Except: ",ex)
