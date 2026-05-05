string = input("Enter the word you want : ")
char = input("Enter your own character : ")
i = 0
count = 0
while(i < len(string)):
  if(string[i] == char):
    count = count + 1
  i = i + 1
print("The total number of Times",char,"has Occured=",count)