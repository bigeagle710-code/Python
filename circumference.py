def get_circumference(radius):
    return 2 * 3.14 * radius

user_radius = float(input("Enter the radius of the circle: "))

result = get_circumference(user_radius)
print(f"The circumference is: {result:.2f}")