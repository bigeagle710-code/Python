rows = 5

print("Normal Triangle:")
for i in range(1, rows + 1):
    print('*' * i)

print("\nMirrored Triangle:")
for i in range(1, rows + 1):
    print(' ' * (rows - i) + '*' * i)