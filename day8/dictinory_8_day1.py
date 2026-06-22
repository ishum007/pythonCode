dog = {}
dog = {
    "name": "Buddy",
    "age": 3,
    "breed": "Golden Retriever",
    "color": "Golden",
}
student = {
    "first_name": "Ishika",
    "last_name": "Mahajan",
    "gender": "Female",
    "age": 20,
    "marital_status": "Single",
    "skills": ["Python", "Java", "C++"],
    "country": "India",
    "city": "Pathankot",
    "address": "mamoon" ,
}
print("Dog Dictionary:", dog)
print("Student Dictionary:", student)
print("length of student dictionary:", len(student))
print("value of skills in student dictionary:", student['skills'])
print("type of skills in student dictionary:", type(student['skills']))
student['skills'].append('JavaScript')
print("student dictionary after adding JavaScript to skills:", student)
print("keys of student dictionary:", student.keys())
print("values of student dictionary:", student.values())
print("items of student dictionary:", student.items())
del student["address"]
print("student dictionary after deleting address:", student)
del dog
