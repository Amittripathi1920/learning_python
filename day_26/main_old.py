import random

numbers = [1,2,3,4,5]
new_list = [n+1 for n in numbers]
print(new_list)

name = "Amit"
name_list = [i.upper() for i in name]
print(name_list)

num_list = [i*2 for i in range(2,11)]
print(num_list)

names = ["Amit", "Abc", "Def", "GHi", "jk"]
short_name = [name.upper() for name in names if len(name)<3]
print(short_name)

# Dictonary comprehension

students_score = {
    item : random.randint(1,100) for item in names
}

print(students_score)
passed_students = {
    student : v for student, v in students_score.items() if v > 33
}

print(passed_students)

# excercise 1

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# separated_list = 
result = {
    item : len(item) for item in sentence.split(" ")
}

print(result)

# excercise 2

weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

weather_f = {
   day : (temp * 9/5) + 32 for day,temp in weather_c.items()
}

print(weather_f)