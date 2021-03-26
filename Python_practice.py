# counties = ["Arapahoe","Denver","Jefferson"]
""" if counties[1] != 'Jefferson'

print(counties[2])
 """

""" if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.") """

# "and" operator to determine if two counties, 
# Arapahoe and El Paso, are in the list of counties.
# if one is false then it will return false.

""" if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.") """

# with "or"if one is true then it will return true.
""" if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties.")
else:
    print("Arapahoe and El Paso are not in the list of counties.")  
 """

#  Evaluates a Boolean expression. 
#  The expression is true if the conditional is false.
""" if "Arapahoe" in counties and "El Paso" not in counties:
   print("Only Arapahoe is in the list of counties.")
else:
    print("Arapahoe is in the list of counties and El Paso is not in the list of counties.") """

# Iterate Through Lists and Tuples When there are 
# no more items in the list, the for loop stops.
""" for county in counties:
    print(county) """

# For Loops iterate, or run through, 
# a program a specific number of times before it stops.     
""" for i in range(len(counties)):
    print(counties[i]) """

""" counties_tuple = ("Arapahoe","Denver","Jefferson")  
 for county in counties_tuple:
      print(county)  """

# Iterate Through a Dictionary
# counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

""" for county in counties_dict.keys():
    print(county) """

# Get the Values of a Dictionary
""" for voters in counties_dict.values():
    print(voters) """    

# For the counties list, modify the for 
# loop and use the key, county to reference the value.
""" for county in counties_dict:
    print(counties_dict[county])  """   

# the get method
""" for county in counties_dict:
    print(counties_dict.get(county)) """    

# When we use the items() method, we get 
# the key and the value for each dictionary
# reference them by name, like "county" and "voters"
# The first variable declared in the for loop is assigned to the keys.
# The second variable is assigned to the values.

""" for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")
 """
# voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                # {"county":"Denver", "registered_voters": 463353},
                # {"county":"Jefferson", "registered_voters": 432438}]

# Get Each Dictionary in a List of Dictionaries
""" for county_dict in voting_data:
    print(county_dict)
 """
""" for i in range(len(voting_data)):
      print(voting_data[i])    """ 
""" 
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)   """    

#retrieve the number of registered voters from each dictionary
""" for county_dict in voting_data:
     print(county_dict['registered_voters'])   """

# only want to print the county name from each dictionary
""" for county_dict in voting_data:
    print(county_dict['county'])  """      

# Dependencies are modules and packages, 
# or a programming script that someone else has written 
# that allows you to increase the functional programming 
# of your code, or speed and efficiency.       

# Import the datetime class from the datetime module.
# Use the now() attribute on 
# the datetime class to get the present time.
# Print the present time.
""" import datetime
now = datetime.datetime.now()
print("The time right now is ", now) """

""" import datetime as dt
now = dt.datetime.now()
print("The time right now is ", now) """

