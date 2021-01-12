#!/usr/bin/env python3

#  for i in range (10):
#   print("Hello, Word!")


# x = ["Now","we","are","cooking!"]
# type(x)
# len(x)


# def get_word(sentence, n):
# 	# Only proceed if n is positive 
# 	if n > 0:
# 		words = sentence.split()
# 		# Only proceed if n is not more than the number of words 
# 		if n <= len(words):
# 			return(words[n-1])
# 	return("")
# print(get_word("This is a lesson about lists", 4)) # Should print: lesson
# print(get_word("This is a lesson about lists", -4)) # Nothing
# print(get_word("Now we are cooking!", 1)) # Should print: Now
# print(get_word("Now we are cooking!", 5)) # Nothing


# age=int(input('Введите Ваш возрост: '))
# if age >= 18:
# 	print('Welcome!')
# else:
# 	print(f'Sorry! Приходите к нам через {18-age} лет')


# for i in range(1,10):
# 	for j in range(2,10):
# 		print(f'{i}x{j}={i*j}\t',end='')
# 	print('')
# else:
# 	print('Well done!')


# def skip_elements(elements):
# 	# Initialize variables
# 	new_list = []
# 	i = 0
# 	# Iterate through the list
# 	for word in range (0,len(elements),2):
# 		# Does this element belong in the resulting list?
# 		if i < len(elements):
# 			# Add this element to the resulting list
# 			new_list.append(elements[word])
# 		# Increment i
# 		i += 1
# 	return new_list

# print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g'] print(skip_elements([
# 'Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach'] print(
# skip_elements([])) # Should be []


# def skip_elements(elements):
# 	# Initialize variables
# 	new_list = []
# 	i = 0
# 	# Iterate through the list
# 	for word in elements:
# 		# Does this element belong in the resulting list?
# 		if i == 0 or i % 2 == 0:
# 			# Add this element to the resulting list
# 			new_list.append(word)
# 		# Increment i
# 		i += 1
# 	return new_list

# print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g'] print(skip_elements([
# 'Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach'] print(
# skip_elements([])) # Should be []


# def skip_elements(elements):
# 	# code goes here
# 	new_list = []
# 	for index, word in enumerate(elements):
# 	    if index == 0 or index % 2 == 0:
# 		    new_list.append(word)
# 	return new_list

# print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g'] print(skip_elements([
# 'Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']


# def odd_numbers(n):
# 	return [x for x in range (1, n+1) if x % 2 != 0]

# print(odd_numbers(5))  # Should print [1, 3, 5]
# print(odd_numbers(10)) # Should print [1, 3, 5, 7, 9]
# print(odd_numbers(11)) # Should print [1, 3, 5, 7, 9, 11]
# print(odd_numbers(1))  # Should print [1]
# print(odd_numbers(-1)) # Should print []


# filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# # Generate newfilenames as a list containing the new filenames
# # using as many lines of code as your chosen method requires.
# newfilenames = [filename.replace('.hpp','.h') for filename in filenames]
# print(newfilenames)
# # Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]


# text = "hello how are you"
# say = ""
# words = text.split()
# for word in words:
# 	say += word[1:] + word[0] + 'ay' + ' '
# print(say)


# def pig_latin(text):
#   say = ""
#   # Separate the text into words
#   words = text.split()
#   for word in words:
#     # Create the pig latin word and add it to the list
#     say += word[1:] + word[0] + 'ay' + ' '
#     # Turn the list back into a phrase
#   return say

# print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
# print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"


# def octal_to_string(octal):
#     result = ""
#     value_letters = [(4,"r"),(2,"w"),(1,"x")]
#     # Iterate over each of the digits in octal
#     for permissions in [int(n) for n in str(octal)]:
#         # Check for each of the permissions values
#         for value, letter in value_letters:
#             if permissions >= value:
#                 result += letter
#                 permissions -= value
#             else:
#                 result += "-"
#     return result

# print(octal_to_string(755)) # Should be rwxr-xr-x
# print(octal_to_string(644)) # Should be rw-r--r--
# print(octal_to_string(750)) # Should be rwxr-x---
# print(octal_to_string(600)) # Should be rw-------


# def group_list(group, users):
#   members = '{}: {}'.format(group, ', '.join(users))
#   return members

# print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # Should be "Marketing: Mike, Karen, Jake, Tasha"
# print(group_list("Engineering", ["Kim", "Jay", "Tom"])) # Should be "Engineering: Kim, Jay, Tom"
# print(group_list("Users", "")) # Should be "Users:"


# def guest_list(guests):
# 	for name, age, profession in guests:
# 		# ___
# 		print('{} is {} years old and works as {}'.format(name,age,profession))

# guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])

# #Click Run to submit code
# """
# Output should match:
# Ken is 30 years old and works as Chef
# Pat is 35 years old and works as Lawyer
# Amanda is 25 years old and works as Engineer
# """


# toc = {"Introduction":1, "Chapter 1":4, "Chapter 2":11, "Chapter 3":25, "Chapter 4":30}
# toc["Epilogue"] = 39 # Epilogue starts on page 39
# toc["Chapter 3"] = 24 # Chapter 3 now starts on page 24
# print(toc) # What are the current contents of the dictionary?
# print('{}'.format("Chapter 5" in toc))    # Is there a Chapter 5?


# cool_beasts = {"octopuses":"tentacles", "dolphins":"fins", "rhinos":"horns"}
# for keys, values in cool_beasts.items():
#     print("{} have {}".format(keys, values))


# wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
# for key, values in wardrobe.items():
# 	for value in values:
# 		print("{} {}".format(value, key))


# def email_list(domains):
# 	emails = []
# 	for domain, users in domains.items():
# 	  for user in users:
# 	    emails.append('{}@{}'.format(user, domain))
# 	return(emails)

# print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon",
# "jean.grey"], "hotmail.com": ["bruce.wayne"]}))


# def groups_per_user(group_dictionary):
#     user_groups = {}
#     # Go through group_dictionary
#     for groups in group_dictionary:
#         # Now go through the users in the group
#         for user in group_dictionary[groups]:
#             if user not in user_groups:
#                 user_groups[user] = []
#             if groups not in user_groups[user]:
#                 user_groups[user].append(groups)
#         # Now add the group to the the list of
#     # groups for this user, creating the entry
#     # in the dictionary if necessary
#
#     return (user_groups)
#
#
# print(groups_per_user({"local": ["admin", "userA"], "public": ["admin", "userB"], "administrator": ["admin"]}))

# wardrobe = {'shirt': ['red', 'blue', 'white'], 'jeans': ['blue', 'black']}
# new_items = {'jeans': ['white'], 'scarf': ['yellow'], 'socks': ['black', 'brown']}
# wardrobe.update(new_items)
# print(wardrobe)


# def add_prices(basket):
# 	# Initialize the variable that will be used for the calculation
# 	total = 0
# 	# Iterate through the dictionary items
# 	for price in basket.values():
# 		# Add each price to the total calculation
# 		# Hint: how do you access the values of
# 		# dictionary items?
# 		total += price
# 	# Limit the return value to 2 decimal places
# 	return round(total, 2)
#
# groceries = {"bananas": 1.56, "apples": 2.50, "oranges": 0.99, "bread": 4.59,
# 	"coffee": 6.99, "milk": 3.39, "eggs": 2.98, "cheese": 5.44}
#
# print(add_prices(groceries)) # Should print 28.44


# host_addresses = {"router": "192.168.1.1", "localhost": "127.0.0.1", "google": "8.8.8.8"}
# print(host_addresses.keys())


# colors = ["red", "white", "blue"]
# colors.insert(2, "yellow")
# print(colors)


# def format_address(address_string):
#   # Declare variables
#   house_number = ''
#   street_name = ''
#   # Separate the address string into parts
#   address_string = address_string.split(' ')
#   # Traverse through the address parts
#   for element in address_string:
#     # Determine if the address part is the
#     if element.isdigit():
#     # house number or part of the street name
#       house_number += element
#   # Does anything else need to be done 
#   # before returning the result?
#     else:
#       street_name += element + ' '
#   # Return the formatted string  
#   return "house number {} on street named {}".format(house_number, street_name)

# print(format_address("123 Main Street"))
# # Should print: "house number 123 on street named Main Street"

# print(format_address("1001 1st Ave"))
# # Should print: "house number 1001 on street named 1st Ave"

# print(format_address("55 North Center Drive"))
# # Should print "house number 55 on street named North Center Drive"


# def highlight_word(sentence, word):
# 	return sentence[0:sentence.index(word)] + word.upper()+ sentence[sentence.index(word)+len(word):]

# print(highlight_word("Have a nice day", "nice"))
# print(highlight_word("Shhh, don't be so loud!", "loud"))
# print(highlight_word("Automating with Python is fun", "fun"))


# def squares(start, end):
#     lst = []
#     for num in range(start, end+1):
#         num = num**2
#         lst.append(num)
#     return lst

# print(squares(2, 3)) # Should be [4, 9]
# print(squares(1, 5)) # Should be [1, 4, 9, 16, 25]
# print(squares(0, 10)) # Should be [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


# def car_listing(car_prices):
#   result = ""
#   for costs, dollars in car_prices.items():
#     result += "{} costs {} dollars".format(costs, dollars) + "\n"
#   return result

# print(car_listing({"Kia Soul":19000, "Lamborghini Diablo":55000, "Ford Fiesta":13000, "Toyota Prius":24000}))


# def combine_guests(guests1, guests2):
#   # Combine both dictionaries into one, with each key listed 
#   # only once, and the value from guests1 taking precedence
#   guests = guests1
#   for friend, guest in guests2.items():
# 	  if friend not in guests:
# 		  guests[friend] = guest
#   return guests

# Rorys_guests = { "Adam":2, "Brenda":3, "David":1, "Jose":3, "Charlotte":2, "Terry":1, "Robert":4}
# Taylors_guests = { "David":4, "Nancy":1, "Robert":2, "Adam":1, "Samantha":3, "Chris":5}

# print(combine_guests(Rorys_guests, Taylors_guests))


# def count_letters(text):
#   result = {}
#   text = text.lower()
#   # Go through each letter in the text
#   for letter in text:
#     # Check if the letter needs to be counted or not
#     if letter.isalpha():
#     # Add or increment the value in the dictionary
#       count = text.count(letter)
#       result[letter] = count
#   return result

# print(count_letters("AaBbCc"))
# # Should be {'a': 2, 'b': 2, 'c': 2}

# print(count_letters("Math is fun! 2+2=4"))
# # Should be {'m': 1, 'a': 1, 't': 1, 'h': 1, 'i': 1, 's': 1, 'f': 1, 'u': 1, 'n': 1}

# print(count_letters("This is a sentence."))
# # Should be {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}


# class Flower:
#   color = 'unknown'

# rose = Flower()
# rose.color = 'red'

# violet = Flower()
# violet.color = 'blue'

# this_pun_is_for_you = Flower()

# print("Roses are {},".format(rose.color))
# print("violets are {},".format(violet.color))
# print(this_pun_is_for_you)


# # define a basic city class
# class City:
# 	name = ""
# 	country = ""
# 	elevation = 0 
# 	population = 0

# # create a new instance of the City class and
# # define each attribute
# city1 = City()
# city1.name = "Cusco"
# city1.country = "Peru"
# city1.elevation = 3399
# city1.population = 358052

# # create a new instance of the City class and
# # define each attribute
# city2 = City()
# city2.name = "Sofia"
# city2.country = "Bulgaria"
# city2.elevation = 2290
# city2.population = 1241675

# # create a new instance of the City class and
# # define each attribute
# city3 = City()
# city3.name = "Seoul"
# city3.country = "South Korea"
# city3.elevation = 38
# city3.population = 9733509

# def max_elevation_city(min_population):
# 	# Initialize the variable that will hold 
# # the information of the city with 
# # the highest elevation 
# 	return_city = City()

# 	# Evaluate the 1st instance to meet the requirements:
# 	# does city #1 have at least min_population and
# 	# is its elevation the highest evaluated so far?
# 	if city1.population >= min_population and city1.elevation > return_city.elevation:
# 		return_city = city1
# 	# Evaluate the 2nd instance to meet the requirements:
# 	# does city #2 have at least min_population and
# 	# is its elevation the highest evaluated so far?
# 	if city2.population >= min_population and city2.elevation > return_city.elevation:
# 		return_city = city2
# 	# Evaluate the 3rd instance to meet the requirements:
# 	# does city #3 have at least min_population and
# 	# is its elevation the highest evaluated so far?
# 	if city3.population >= min_population and city3.elevation > return_city.elevation:
# 		return_city = city3

# 	#Format the return string
# 	if return_city.name:
# 		return '{}, {}'.format(return_city.name, return_city.country)
# 	else:
# 		return ""

# print(max_elevation_city(100000)) # Should print "Cusco, Peru"
# print(max_elevation_city(1000000)) # Should print "Sofia, Bulgaria"
# print(max_elevation_city(10000000)) # Should print ""
# print(max_elevation_city(9000000)) # Should print ""


# # “If you have an apple and I have an apple and we exchange these apples then
# # you and I will still each have one apple. But if you have an idea and I have
# # an idea and we exchange these ideas, then each of us will have two ideas.”
# # George Bernard Shaw

# class Person:
#     apples = 0
#     ideas = 0

# johanna = Person()
# johanna.apples = 1
# johanna.ideas = 1

# martin = Person()
# martin.apples = 2
# martin.ideas = 1

# def exchange_apples(you, me):
# #Here, despite G.B. Shaw's quote, our characters have started with       #different amounts of apples so we can better observe the results. 
# #We're going to have Martin and Johanna exchange ALL their apples with #one another.
# #Hint: how would you switch values of variables, 
# #so that "you" and "me" will exchange ALL their apples with one another?
# #Do you need a temporary variable to store one of the values?
# #You may need more than one line of code to do that, which is OK. 
#     # exchange = 1
#     # me.apples += exchange - 1
#     # you.apples += exchange - 1
#     # return you.apples, me.apples
#     exchange=you.apples
#     you.apples=me.apples
#     me.apples=exchange
#     return you.apples, me.apples

# def exchange_ideas(you, me):
#     #"you" and "me" will share our ideas with one another.
#     #What operations need to be performed, so that each object receives
#     #the shared number of ideas?
#     #Hint: how would you assign the total number of ideas to 
#     #each idea attribute? Do you need a temporary variable to store 
#     #the sum of ideas, or can you find another way? 
#     #Use as many lines of code as you need here.
#     you.ideas += me.ideas
#     me.ideas = you.ideas
#     return you.ideas, me.ideas

# exchange_apples(johanna, martin)
# print("Johanna has {} apples and Martin has {} apples".format(johanna.apples, martin.apples))
# exchange_ideas(johanna, martin)
# print("Johanna has {} ideas and Martin has {} ideas".format(johanna.ideas, martin.ideas))


# class Bird:
#     color = ''
#     number = ''

# bluejay = Bird()
# bluejay.color = 'red'
# bluejay.number = 0
# print(bluejay.color, bluejay.number)


# class Dog:
#     years = 0
#     def dog_years(self):
#         return self.years * 7

# fido = Dog()
# fido.years = 3
# print(fido.dog_years()) 


# class Apple:
#      def __init__(self, color, flavor):
#          self.color = color
#          self.flavor = flavor
#      def __str__(self):
#          return "This apple is {} and its flavor is {}".format(self.color, self.flavor)

# jonagold = Apple("red", "sweet")
# print(jonagold)

# help(Apple)


# class Elevator:
#     def __init__(self, bottom, top, current):
#         """Initializes the Elevator instance."""
#         self.bottom = bottom
#         self.top = top
#         self.current = current
#     def up(self):
#         """Makes the elevator go up one floor."""
#         while self.current < self.top:
#             self.current += 1
#             break
#         return self.current
#     def down(self):
#         """Makes the elevator go down one floor."""
#         while self.current > self.bottom:
#             self.current -= 1
#             break
#         return self.current
#     def go_to(self, floor):
#         """Makes the elevator go to the specific floor."""
#         if self.bottom <= floor <= self.top:
#             self.current = floor
#         return  self.current
#     def __str__(self):
#         return "Current floor: {}".format(self.current)

# elevator = Elevator(-1, 10, 0)
# # elevator.up() 
# # elevator.current #should output 1

# # elevator.down() 
# # elevator.current #should output 0

# # elevator.go_to(10) 
# # elevator.current #should output 10

# # Go to the top floor. Try to go up, it should stay. Then go down.
# elevator.go_to(10)
# elevator.up()
# elevator.down()
# print(elevator.current) # should be 9
# # Go to the bottom floor. Try to go down, it should stay. Then go up.
# elevator.go_to(-1)
# elevator.down()
# elevator.down()
# elevator.up()
# elevator.up()
# print(elevator.current) # should be 1

# elevator.go_to(5)
# print(elevator)


# class Clothing:
#   stock={ 'name': [],'material' :[], 'amount':[]}
#   def __init__(self,name):
#     material = ""
#     self.name = name
#   def add_item(self, name, material, amount):
#     Clothing.stock['name'].append(self.name)
#     Clothing.stock['material'].append(self.material)
#     Clothing.stock['amount'].append(amount)
#   def Stock_by_Material(self, material):
#     count=0
#     n=0
#     for item in Clothing.stock['material']:
#       if item == material:
#         count += Clothing.stock['amount'][n]
#         n+=1
#     return count

# class shirt(Clothing):
#   material="Cotton"
# class pants(Clothing):
#   material="Cotton"

# polo = shirt("Polo")
# sweatpants = pants("Sweatpants")
# polo.add_item(polo.name, polo.material, 4)
# sweatpants.add_item(sweatpants.name, sweatpants.material, 6)
# current_stock = polo.Stock_by_Material("Cotton")
# print(current_stock)


# Begin Portion 1#
# import random

# class Server:
#     def __init__(self):
#         """Creates a new server instance, with no active connections."""
#         self.connections = {}

#     def add_connection(self, connection_id):
#         """Adds a new connection to this server."""
#         connection_load = random.random()*10+1
#         # Add the connection to the dictionary with the calculated load
#         if connection_id != None:
#             self.connections[connection_id] = connection_load

#     def close_connection(self, connection_id):
#         """Closes a connection on this server."""
#         # Remove the connection from the dictionary
#         if connection_id != None:
#             del self.connections[connection_id]

#     def load(self):
#         """Calculates the current load for all connections."""
#         total = 0
#         # Add up the load for each of the connections
#         for connection in self.connections:
#             total += self.connections[connection]
#         return total

#     def __str__(self):
#         """Returns a string with the current load of the server"""
#         return "{:.2f}%".format(self.load())

# #End Portion 1#

# server = Server()
# server.add_connection("192.168.1.1")
# # server.add_connection("192.168.1.2")
# print(server)
# print(server.load())

# server.close_connection("192.168.1.1")
# print(server.load())


# #Begin Portion 2#
# class LoadBalancing:
#     def __init__(self):
#         """Initialize the load balancing system with one server"""
#         self.connections = {}
#         self.servers = [Server()]

#     def add_connection(self, connection_id):
#         """Randomly selects a server and adds a connection to it."""
#         server = random.choice(self.servers)
#         # Add the connection to the dictionary with the selected server
#         # Add the connection to the server
#         server.add_connection(connection_id)
#         self.ensure_availability()

#     def close_connection(self, connection_id):
#         """Closes the connection on the the server corresponding to connection_id."""
#         # Find out the right server
#         # Close the connection on the server
#         # Remove the connection from the load balancer
#         for server in self.servers:
#             if connection_id in server.connections:
#                 server.close_connection(connection_id)
#                 break

#     def avg_load(self):
#         """Calculates the average load of all servers"""
#         # Sum the load of each server and divide by the amount of servers
#         total_load = 0
#         total_server = 0
#         for server in self.servers:
#             total_load += server.load()
#             total_server += 1
#         return total_load/total_server

#     def ensure_availability(self):
#         """If the average load is higher than 50, spin up a new server"""
#         if self.avg_load() > 50:
#             self.servers.append(Server())

#     def __str__(self):
#         """Returns a string with the load for each server."""
#         loads = [str(server) for server in self.servers]
#         return "[{}]".format(",".join(loads))
# #End Portion 2#


# l = LoadBalancing()
# l.add_connection("fdca:83d2::f20d")
# print(l.avg_load())

# l.servers.append(Server())
# print(l.avg_load())

# l.close_connection("fdca:83d2::f20d")
# print(l.avg_load())

# for connection in range(20):
#     l.add_connection(connection)
# print(l)

# print(l.avg_load())


# Here are all the installs and imports you will need for your word cloud script and uploader widget

# !pip install wordcloud
# !pip install fileupload
# !pip install ipywidgets
# !jupyter nbextension install --py --user fileupload
# !jupyter nbextension enable --py fileupload

# import wordcloud
# import numpy as np
# from matplotlib import pyplot as plt
# from IPython.display import display
# import fileupload
# import io
# import sys

# # This is the uploader widget

# def _upload():

#     _upload_widget = fileupload.FileUploadWidget()

#     def _cb(change):
#         global file_contents
#         decoded = io.StringIO(change['owner'].data.decode('utf-8'))
#         filename = change['owner'].filename
#         print('Uploaded `{}` ({:.2f} kB)'.format(
#             filename, len(decoded.read()) / 2 **10))
#         file_contents = decoded.getvalue()

#     _upload_widget.observe(_cb, names='data')
#     display(_upload_widget)

# _upload()

# def calculate_frequencies(file_contents):
#     # Here is a list of punctuations and uninteresting words you can use to process your text
#     punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
#     uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
#     "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
#     "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
#     "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
#     "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]

#     # LEARNER CODE START HERE

#     #wordcloud
#     cloud = wordcloud.WordCloud()
#     cloud.generate_from_frequencies()
#     return cloud.to_array()

# # Display your wordcloud image

# myimage = calculate_frequencies(file_contents)
# plt.imshow(myimage, interpolation = 'nearest')
# plt.axis('off')
# plt.show()


# ar = [1,2,3,4,10,11]
# print(len(ar))

# def simpleArraySum(ar):
#     sum = 0
#     for i in range(len(ar)):
#         sum = sum + ar[i]
#     return sum

# result = simpleArraySum(ar)
# print(result)
