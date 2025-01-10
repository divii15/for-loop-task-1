# 7 students = [
    {"name": "Alice", "age": 20},
    {"name": "Bob", "age": 22},
    {"name": "Charlie", "age": 13}
]----find the person eligible for vote or not


students = [
    {"name": "Alice", "age": 20},
    {"name": "Bob", "age": 22},
    {"name": "Charlie", "age": 13}]
for stu in students:
    if(stu["age"]>=18):
        print(stu["name"],"is eligible for vote.")
    else:
        print(stu["name"],"is not eligible for vote.")

