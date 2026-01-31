import json

file_json = 'students.json'
new_json = 'new_data.json'

try:
    with open(file_json, 'r') as file:
        students = json.load(file)
        
        for student in students:
            grades = student["grades"]
            average = sum(grades) / len(grades)
            student["average_grade"] = round(average, 2)

        with open(new_json, "w") as file:
            json.dump(students, file, indent=2)

except EnvironmentError:
    print("error")
except json.JSONDecodeError:
    print("error")