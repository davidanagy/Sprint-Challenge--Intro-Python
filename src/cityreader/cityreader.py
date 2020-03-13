# Create a class to hold a city location. Call the class "City". It should have
# fields for name, lat and lon (representing latitude and longitude).
class City:
    def __init__(self, name, lat, lon):
        self.name = name
        self.lat = lat
        self.lon = lon

# We have a collection of US cities with population over 750,000 stored in the
# file "cities.csv". (CSV stands for "comma-separated values".)
#
# In the body of the `cityreader` function, use Python's built-in "csv" module 
# to read this file so that each record is imported into a City instance. Then
# return the list with all the City instances from the function.
# Google "python 3 csv" for references and use your Google-fu for other examples.
#
# Store the instances in the "cities" list, below.
#
# Note that the first line of the CSV is header that describes the fields--this
# should not be loaded into a City object.
cities = []

def cityreader(cities=[]):
    # TODO Implement the functionality to read from the 'cities.csv' file
    # For each city record, create a new City instance and add it to the 
    # `cities` list
    import csv
    # This website was helpful:
    # https://www.geeksforgeeks.org/working-csv-files-python/
    # Though it looks like it's out of date,
    # since I need the double underscores around "next"
    # (discovred by looking at the documentation here--
    # https://docs.python.org/3/library/csv.html)
    with open('cities.csv', 'r') as csvfile:
        cityreader = csv.reader(csvfile)
        fields = cityreader.__next__()
        relevant_field_nums = {}
        # "Enumerate" creates a list of tuples, with the first
        # value being a number that goes up by one.
        # See this useful Medium post for more info on using it in loops:
        # https://medium.com/better-programming/stop-using-range-in-your-python-for-loops-53c04593f936
        for num, field in enumerate(fields):
            # get the positions of the three relevant columns
            if field in ['city', 'lat', 'lng']:
                # add field name as the key, and position as the value
                relevant_field_nums[field] = num
        name_num = relevant_field_nums['city']
        lat_num = relevant_field_nums['lat']
        lon_num = relevant_field_nums['lng']
        for row in cityreader:
            # At first I failed; I had to test some stuff in the command line
            # to realize I needed to convert the strings to floats...
            city = City(row[name_num], float(row[lat_num]), float(row[lon_num]))
            cities.append(city)

    return cities

cityreader(cities)

# Print the list of cities (name, lat, lon), 1 record per line.
for c in cities:
    print(c.name, c.lat, c.lon)

# STRETCH GOAL!
#
# Allow the user to input two points, each specified by latitude and longitude.
# These points form the corners of a lat/lon square. Pass these latitude and 
# longitude values as parameters to the `cityreader_stretch` function, along
# with the `cities` list that holds all the City instances from the `cityreader`
# function. This function should output all the cities that fall within the 
# coordinate square.
#
# Be aware that the user could specify either a lower-left/upper-right pair of
# coordinates, or an upper-left/lower-right pair of coordinates. Hint: normalize
# the input data so that it's always one or the other, then search for cities.
# In the example below, inputting 32, -120 first and then 45, -100 should not
# change the results of what the `cityreader_stretch` function returns.
#
# Example I/O:
#
# Enter lat1,lon1: 45,-100
# Enter lat2,lon2: 32,-120
# Albuquerque: (35.1055,-106.6476)
# Riverside: (33.9382,-117.3949)
# San Diego: (32.8312,-117.1225)
# Los Angeles: (34.114,-118.4068)
# Las Vegas: (36.2288,-115.2603)
# Denver: (39.7621,-104.8759)
# Phoenix: (33.5722,-112.0891)
# Tucson: (32.1558,-110.8777)
# Salt Lake City: (40.7774,-111.9301)

# TODO Get latitude and longitude values from the user
input1 = input('\nEnter lat1,lon1: ')
input2 = input('Enter lat2,lon2: ')
lat1, lon1 = input1.split(',')
lat2, lon2 = input2.split(',')
def cityreader_stretch(lat1, lon1, lat2, lon2, cities=[]):
    # within will hold the cities that fall within the specified region
    within = []

    # TODO Ensure that the lat and lon valuse are all floats
    # Go through each city and check to see if it falls within 
    # the specified coordinates.
    if float(lat1) <= float(lat2):
        # If they're equal, we'll just only return a city with that
        # precise latitude, so this is fine.
        lower_lat = float(lat1)
        upper_lat = float(lat2)
    else:
        lower_lat = float(lat2)
        upper_lat = float(lat1)

    if float(lon1) <= float(lon2):
        lower_lon = float(lon1)
        upper_lon = float(lon2)
    else:
        lower_lon = float(lon2)
        upper_lon = float(lon1)

    for city in cities:
        if ((city.lat > lower_lat) and (city.lat < upper_lat) and
           (city.lon > lower_lon) and (city.lon < upper_lon)):
           within.append(city)

    return within

within = cityreader_stretch(lat1, lon1, lat2, lon2, cities)
for city in within:
    print(f'{city.name}: ({city.lat}, {city.lon})')
