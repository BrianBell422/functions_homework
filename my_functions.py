# Returning a value from a function

# def greet():
#     return "Hey"

# greeting = greet()
# print(greeting)


# Paramaters and arguments

# def greet(name): 
#   return "Hey " + name

# greeting = greet("Brian")
# print(greeting)


# Multiple parameters

# def greet(name, time_of_day):
#     return "Good " + time_of_day + ", " + name

# greeting = greet('Brian', 'morning')
# print(greeting)


# Laundry

# def wash_clothes(laundry, detergent, water):
#     clean_laundry = laundry + detergent + water
#     return clean_laundry

# clean_tshirt = wash_clothes('dirty tshirt, ', 'liquid detergent, ', 'water')
# print(clean_tshirt)


# Passing variables as arguments

# def greet(name, time_of_day):
#   return "Good " + time_of_day + ", " + name

# name_1 = "Brian"
# time_of_day_1 = "evening"
# greeting = greet(name_1, time_of_day_1)
# print(greeting)

# name_2 = "Ada"
# time_of_day_2 = "afternoon"
# greeting = greet(name_2, time_of_day_2)
# print(greeting)

# Scope

# def greet():
#   words = "Hey"
#   return words

# def greet_two():
#   words = "Hi"
#   return words

# print(greet_two())


# More complex example

chickens = [
  { "name": "Margaret", "age": 2, "eggs": 0 },
  { "name": "Hetty", "age": 1, "eggs": 2 },
  { "name": "Henrietta", "age": 3, "eggs": 1 },
  { "name": "Audrey", "age": 2, "eggs": 0 },
  { "name": "Mabel", "age": 5, "eggs": 1 },
]

def count_eggs( list ):
    total_eggs = 0

    for bird in list:
        total_eggs += bird["eggs"]
        bird["eggs"] = 0 # eggs have been collected

    return f"{total_eggs} eggs collected"

print(count_eggs(chickens))