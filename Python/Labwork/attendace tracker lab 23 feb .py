# Attendance Tracker with Consecutive Absence Warning

# Example data: 1 = present, 0 = absent
students_attendance = {
    "Alice": [1, 0, 1, 1, 1, 0, 0],
    "Bob": [1, 1, 1, 1, 1, 1, 1],
    "Charlie": [0, 0, 1, 0, 1, 0, 0],
    "David": [1, 0, 0, 1, 0, 0, 0]
}

def has_consecutive_absence(attendance, n=2):
    """Check if student has n or more consecutive absences"""
    count = 0
    for a in attendance:
        if a == 0:
            count += 1
            if count >= n:
                return True
        else:
            count = 0
    return False

results = {}

for name, attendance in students_attendance.items():
    total_classes = len(attendance)
    presents = sum(attendance)
    percentage = (presents / total_classes) * 100
    low_attendance = percentage < 75
    consecutive_absence_flag = has_consecutive_absence(attendance)

    results[name] = {
        "attendance_percentage": percentage,
        "low_attendance": low_attendance,
        "consecutive_absence_flag": consecutive_absence_flag
    }

# Display Report
print("----- Attendance Report -----")
for name, data in results.items():
    print(f"\nStudent: {name}")
    print(f"Attendance Percentage: {data['attendance_percentage']:.2f}%")
    if data['low_attendance']:
        print("⚠️ Attendance below 75%")
    if data['consecutive_absence_flag']:
        print("⚠️ Warning: Consecutive absences detected")