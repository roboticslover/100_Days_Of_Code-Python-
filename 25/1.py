# making changes in tuple
countries = ("India", "Spain", "USA")
temp = list(countries)
temp.append("Korea")
countries = tuple(temp)
print(countries)

# appending two tuples for making changes
countries2 = ("Brics", "Nato")
World = countries+countries2
print(World)
