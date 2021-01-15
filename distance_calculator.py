import sys
import random
import operator
import csv

from haversine import haversine

places_random_dictionary = {}


def places_dictionary(random_argument):
	"""Generates dictionary with a number of random places"""

	index = 0
	random_positive_argument = abs(random_argument)
	for place in range(0, random_positive_argument):
		key_string = "place" + str(index)
		places_random_dictionary[key_string] = [round(random.uniform(-90.00000, 90.00000), 5), round(random.uniform(-180.00000, 180.00000), 5)]
		index += 1
	
	return places_random_dictionary

def places_from_file():
	"""Generates dictionary with places from the file"""

	with open("places.csv", mode="r") as my_file:
		reader = csv.reader(my_file)
		next(reader)
		places_from_file_dictionary = {rows[0]:[float(rows[1]),float(rows[2])] for rows in reader}
		
	return places_from_file_dictionary


def distances_between_places():
	"""Prints distances between all pairs of dictionary in ascending order. 
		Prints average distance of all distances of all pairs. Prints pair and corresponding
		distance having the distance closest to the average distance.  """

	next_key = 1
	new_empty_dictionary = {}
	distance_sum = 0
	
	if len(sys.argv) == 1:
		dictionary = places_from_file()
						
	elif len(sys.argv) == 2:
		try:
			int(sys.argv[1])
			random_argument = int(sys.argv[1])
			dictionary = places_dictionary(random_argument)
			if int(sys.argv[1]) == 0 or int(sys.argv[1]) == 1 or int(sys.argv[1]) == -1:
				sys.exit()
		except:
			print("You should use one optional integer argument which is not -1, 0 or 1. ")	
			sys.exit()
	else:
		print("You should use one optional integer argument which is not -1, 0, 1. ")
		sys.exit()

	list_of_dictionary_keys = list(dictionary.keys())

	for entry_in_dictionary in dictionary:
		for second_entry in list_of_dictionary_keys[next_key:]:
			distance = haversine(dictionary[entry_in_dictionary], dictionary[second_entry])
			rounded_distance = round(distance, 1)
			new_empty_dictionary[rounded_distance] = [entry_in_dictionary, second_entry]
		next_key += 1

	data = sorted(new_empty_dictionary.items())
	list_of_keys = []

	for element in data:
		distance_sum += element[0]
		print("{element[1][0]:<23}{element[1][1]:<23}{element[0]}km".format(element=element)) 
		list_of_keys.append(element[0])

	average_distance = round((distance_sum/len(data)), 1)
	closest_value = min(list_of_keys, key=lambda x:abs(x-average_distance))
	closest_pair = new_empty_dictionary[closest_value]
	
	print("Average distance: " + str(average_distance) + " km.  Closest pair: " + str(closest_pair[0]) + " - "+  str(closest_pair[1]) + " "+ str(closest_value) + " km." )

if __name__ == "__main__":
	distances_between_places()

		
	
