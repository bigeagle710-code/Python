limit = int(input("Enter a number: "))
odd_numbers = [x for x in range(limit) if x % 2 != 0]
print("Odd numbers list:", odd_numbers)
fruits = ["apple", "banana", "cherry", "melon", "pineapple"]
capitalized_fruits = [fruit.capitalize() for fruit in fruits]
print("original fruits:", fruits)
print("updated fruits:", capitalized_fruits)