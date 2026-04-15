import numpy as np

# Marks of 5 students in 3 subjects (rows = students, columns = subjects)
marks = np.array([
    [78, 85, 90],
    [65, 70, 60],
    [88, 92, 95],
    [50, 45, 55],
    [72, 80, 68]
])

print("Marks Matrix:\n", marks)

# 1. Total marks per student
total_marks = np.sum(marks, axis=1)
print("\nTotal Marks per Student:", total_marks)

# 2. Average marks per student
average_marks = np.mean(marks, axis=1)
print("\nAverage Marks per Student:", average_marks)

# 3. Topper (highest total)
topper_index = np.argmax(total_marks)
print("\nTopper is Student Index:", topper_index)

# 4. Subject-wise average
subject_avg = np.mean(marks, axis=0)
print("\nSubject-wise Average:", subject_avg)

# 5. Pass/Fail (pass if all subjects >= 50)
pass_fail = np.all(marks >= 50, axis=1)
print("\nPass/Fail Status:", pass_fail)

# 6. Standard deviation (performance consistency)
std_dev = np.std(marks, axis=1)
print("\nStandard Deviation per Student:", std_dev)