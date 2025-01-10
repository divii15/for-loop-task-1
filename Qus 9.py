# 9 voters = [
    {"name": "Alice", "gender": "female", "age": 20, "votes": 3},
    {"name": "Bob", "gender": "male", "age": 17, "votes": 5},
    {"name": "Charlie", "gender": "male", "age": 25, "votes": 2},
    {"name": "Diana", "gender": "female", "age": 16, "votes": 4},
    {"name": "Edward", "gender": "male", "age": 30, "votes": 1}
]----------- display the total vote of male and female, if they are eligible.



voters = [
    {"name": "Alice", "gender": "female", "age": 20, "votes": 3},
    {"name": "Bob", "gender": "male", "age": 17, "votes": 5},
    {"name": "Charlie", "gender": "male", "age": 25, "votes": 2},
    {"name": "Diana", "gender": "female", "age": 16, "votes": 4},
    {"name": "Edward", "gender": "male", "age": 30, "votes": 1}
]
a=0
b=0
for vote in voters:
    if vote["age"] >= 18:  
        if vote["gender"] == "male":
            a += vote["votes"]
        elif vote["gender"] == "female":
            b += vote["votes"]
print("Total votes for female voters is",a)
print("Total votes for male voters is",b)