# 8 employees = [
    {"name": "John", "salary": 5000},
    {"name": "Jane", "salary": 7000},
    {"name": "Mike", "salary": 4000}
]---find who is earn user entered salary or above, for example user enter 5000, output is john, jane


employees = [
    {"name": "John", "salary": 5000},
    {"name": "Jane", "salary": 7000},
    {"name": "Mike", "salary": 4000}]
sal=int(input("Enter the salary:"))
for emp in employees:
  if(emp["salary"]>=sal):
       print(emp["name"])