print("Welcome to the exam elibility checker")
Medical=input("Do you have any medical cause Y or N : ")
attendence=int(input("Enter your attendence percentage: "))
if Medical == 'Y':
    print ("You are allowed to do the exam")
else:
    if attendence>=75:
     print ("You are allowed to do the exam")
    else:
     print ("You are not allowed")   