# This day focuses on building a silent auction which as many people who want
# can bid on the program and the highest bid wins and gets displayed.


#  Below is an example of a Dictonary for which we can call and use without print statements.
"""

student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

student_grades = {} # Nested lists needs to have the squiggly brackets

for student in student_scores:
  score = student_scores[student]
  if score > 90:
    student_grades[student] = "Outstanding"
  elif score > 80:
    student_grades[student] = "Exceeds Expectations"
  elif score > 70:
    student_grades[student] = "Acceptable"
  else:
    student_grades[student] = "Fail"


print(student_grades) 

"""

"""
# Nesting dictionary inside of a dictionary 

capitals = {
    "Greece" : {"poi visited" : ["Athens", "Pantheon"], "total_visits": 12}
}


# Nesting dictionary inside of lists

capitals = [
    {
      "Country": "Greece", 
      "poi visited": ["Athens", "Pantheon"], 
      "total_visits": 12
    },
    {
      "Country": "Greece", 
      "poi visited": ["Athens", "Pantheon"], 
      "total_visits": 12
    }
     

]
"""


"""

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

def add_new_country(name, visit_count, cities_visited):
  new_country = {}
  new_country["country"] = name
  new_country["visits"] = visit_count
  new_country["cities"] = cities_visited
  travel_log.append(new_country)
  

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)

"""