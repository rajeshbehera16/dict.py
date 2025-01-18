student = {
    "name": "John",
    "age": 20,
    "grade": "A",
    "subjects": ["Math", "Science", "History"]
}
print("Original dictionary:", student)
print("Student's name:", student["name"])
print("Student's grade:", student["grade"])
student["school"] = "Greenwood High"
print("After adding 'school':", student)
student["grade"] = "A+"
print("After updating 'grade':", student)
removed_value = student.pop("age")
print("Removed 'age':", removed_value)
print("After removing 'age':", student)
last_item = student.popitem()
print("Removed last item:", last_item)
print("After popitem():", student)
if "name" in student:
    print("'name' key exists in the dictionary")
address = student.get("address", "Not provided")
print("Address:", address)
print("\nIterating over keys:")
for key in student.keys():
    print(key)
print("\nIterating over values:")
for value in student.values():
    print(value)
print("\nIterating over key-value pairs:")
for key, value in student.items():
    print(f"{key}: {value}")
additional_info = {"age": 21, "hobby": "Reading"}
student.update(additional_info)
print("\nAfter merging with additional_info:", student)
squares = {x: x ** 2 for x in range(1, 6)}
print("\nDictionary of squares:", squares)
student.clear()
print("After clearing the dictionary:", student)
