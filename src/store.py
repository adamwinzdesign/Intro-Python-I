class Store: 
  def __init__(self, name, lat, lon, departments):
    self.name = name
    self.location = LatLon(lat, lon)
    self.departments = departments

  def __str__(self):
    return f"Store {self.name}, {self.location}, {self.departments}"

store = Store("LambdaStore", 44.13455, -121.123124, ["Cloting", "Cookware", "Books"])
print(store)

# Adding departments
selection = input("Select the number of a department: ")
print("The user selected " + store.departments[int(selection)])

# adding error handling in case user attempts to access a non-existent department
try:
  # casting will throw an error if user enters a non-integer
  selection = int(selection)
  if selection >= len(store.departments):
    print("That's not a valid department")
  elif selection >= 0 and selection < len(store.departments)
    print("The user selected: " + store.department)
  else:
    print("Depart numbers are positive")
except ValueError:
  print("Please enter your choice as a positive number")