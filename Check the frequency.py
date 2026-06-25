test_dict = {'Codingal':3, 'is':2, 'best':2, 'for':2, 'Coding':1}
print("The dictionary is:", test_dict)
k = int(input("Enter the value to check its frequency: "))
res = list(test_dict.values()).count(k)
print("The frequency of", k, "is", res)