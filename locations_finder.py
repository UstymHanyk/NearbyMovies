"""
Finding 10 nearest locations
"""
from math import radians, cos, sin, asin, sqrt
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderUnavailable

def coord_finder(movie_list):
    """
    Finds coords using geopy
    """
    geolocator = Nominatim(user_agent="nearby seymovies")
    movie_loc_list = []
    loc_dict = {}
    for movie in movie_list:
        loc = loc_dict.get(movie[1], False)  # check if this is a new location
        if not loc and loc != 'unavailable':  # if this is a new location entry
            try:
                loc_dict[movie[1]] = geolocator.geocode(movie[1])
                if loc_dict[movie[1]] == None:  # generalize the location if geopy can't find it
                    temp_loc_list = movie[1].split(",")
                    shorter_loc = ", ".join(temp_loc_list[1:])
                    loc_dict[movie[1]] = geolocator.geocode(shorter_loc)
            except GeocoderUnavailable:
                loc_dict[movie[1]] = 'unavailable'
        loc = loc_dict.get(movie[1], False)

        if loc and loc != 'unavailable':  # if geopy found the location
            loc = loc.point[:-1]
        movie_loc_list.append((movie[0], loc))
    movie_loc_list_clean = [i for i in set(movie_loc_list) if i[1] != None and i[1] != 'unavailable']
    return movie_loc_list_clean

def haversine(lat1, lon1, lat2, lon2):
    """
    Finds distance between two points
    https://stackoverflow.com/questions/4913349/haversine-formula-in-python-bearing-and-distance-between-two-gps-points
    """
    r = 6372.8

    d_lat = radians(lat2 - lat1)
    d_lon = radians(lon2 - lon1)
    lat1 = radians(lat1)
    lat2 = radians(lat2)

    a = sin(d_lat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(d_lon / 2) ** 2
    c = 2 * asin(sqrt(a))

    return r * c

def find_nearest_movies(movie_loc_list, user_loc: tuple):
    """
    finds 10 nearest movies
    """
    distances = []
    for movie in movie_loc_list:
        distance = haversine(float(movie[1][0]), float(movie[1][1]), user_loc[0], user_loc[1])
        distances.append(distance)
    movie_distances = list(zip(movie_loc_list,distances))
    print("10 nearest movies found.")
    return sorted(movie_distances,key = lambda i: i[1])[:10]
