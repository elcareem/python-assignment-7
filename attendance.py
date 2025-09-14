"""
Attendance Register

Task:
- Track attendance of students.
- Use a dictionary { "student_id": {"name": str, "present_days": list, "absent_days": list} }
- Functions to mark attendance, check history, and get reports.
- Use your head/logic to mark multiple students at once.
- Use **kwargs for flexible reporting (e.g., only_present=True).

// NOT FOR THIS ASSIGNMENT
Future OOP Extension:
- Student class with mark_present() and mark_absent().
- AttendanceRegister class that manages records.
"""

import datetime

attendance = {}

def register_student(student_id, name):
    """Register a student in the system."""
    if student_id not in attendance:
       attendance.update({student_id: {"name": name}})
    else:
        return "Id exists already"
    return attendance

def mark_present(student_ids):
    """Mark multiple students as present for today."""
    today = str(datetime.date.today())
    # implement logic
    for student_id in student_ids:
        if student_id in attendance:
            if "present_days" in attendance[student_id]:
                attendance[student_id]["present_days"].append(today)
            else:
                attendance[student_id].update({"present_days": [today]})
        else:
            print(f"Id {student_id} not in attendance")


def mark_absent(student_ids):
    
    """Mark multiple students as absent for today."""
    today = str(datetime.date.today())
    #implement logic
    for student_id in student_ids:
        if student_id in attendance:
            if "absent_days" in attendance[student_id]:
                attendance[student_id]["absent_days"].append(today)
            else:
                attendance[student_id].update({"absent_days": [today]})
        else:
            print(f"Id {student_id} not in attendance")

def get_report(**kwargs):
    """Generate attendance report with optional filters."""
    report = {}
    present = False
    absent = False
    # implement logic
    for key, value in kwargs.items():
        if value == True:
            for student, record in attendance.items():
                if "present_days" in record:
                    if key == "only_present":
                        present = True
                        if student in report:
                                report[student].update({"present_days": record["present_days"]})
                        else:
                            report.update({student: {"present_days": record["present_days"]}})
                if "absent_days" in record:
                    if key == "only_absent":
                        absent = True
                        if student in report:
                                report[student].update({"absent_days": record["absent_days"]})
                        else:
                            report.update({student: {"absent_days": record["absent_days"]}})
    return report

register_student("001", "Jane")
register_student("002", "John")
register_student("003", "Janet")

mark_present(['001', '002', '003'])
mark_absent(['001', '002'])

print(get_report( only_absent= True, only_present= True))


