import numpy as np
data_type = [('name', 'S15'), ('Class', int), ('height', float)]
students_details = [('Fatima', 9, 63), ('Asmaa', 9, 59), ('Roha', 9, 65), ('Mahroosh', 9, 64)]
students = np.array(students_details, dtype=data_type)
print("Original Array:")
print(students)
print("Sort by height")
print(np.sort(students, order='height'))