"""
Finding 10 nearest locations
"""
from math import radians, cos, sin, asin, sqrt
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
from data_reader import read_data, select_year
from geopy.exc import GeocoderUnavailable

# data_rawish = read_data("smaller_locations.list")
# data = select_year(data_rawish, 2014)
# print(data)

def coord_finder(movie_list):
    """
    Finds coords using geopy
    """
    print(len(movie_list), "Movies in the year")
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
                    # print(movie, shorter_loc)
                    loc_dict[movie[1]] = geolocator.geocode(shorter_loc)
            except GeocoderUnavailable:
                loc_dict[movie[1]] = 'unavailable'
        loc = loc_dict.get(movie[1], False)

        if loc and loc != 'unavailable':  # if geopy found the location
            # print(loc.point[:-1])
            loc = loc.point[:-1]
        movie_loc_list.append((movie[0], loc))
    movie_loc_list_clean = [i for i in set(movie_loc_list) if i[1] != None and i[1] != 'unavailable']
    print(len(movie_loc_list_clean), "Locations found")
    print(movie_loc_list_clean)
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
        # print(distance)
    movie_distances = list(zip(movie_loc_list,distances))
    # print(movie_distances)
    return sorted(movie_distances,key = lambda i: i[1])[:10]
movie_locations = [('"#ATown', (30.2711286, -97.7436995)), ('"#ATown', (30.2711286, -97.7436995)), ('"#ATown', (29.8826436, -97.9405828)), ('"#ATown', (30.268603249999998, -97.76277328657375)), ('"#ATown', (30.27213615, -97.7688868111702)), ('"#ATown', (30.3207674, -97.7733474)), ('"#ATown', (30.2711286, -97.7436995)), ('"#ATown', (30.240283, -97.7887279)), ('"#ATown', (30.2020961, -97.6700119)), ('"#Elmira', (42.0897965, -76.8077338)), ('"#Nightstrife', (41.8755616, -87.6244212)), ('"(Des)Encontros', (-23.9661602, -46.3287265)), ('"(Mis)adventure', (34.1729044, -118.3740371)), ('"(Mis)adventure', (34.0536909, -118.242766)), ('"(gli) Imperatori', (41.8933203, 12.4829321)), ('"+27: Social Innovators of South Africa', (-33.928992, 18.417396)), ('"+27: Social Innovators of South Africa', (-26.205, 28.049722)), ('"/Drive on NBCSN', (46.5286176, 10.4532056)), ('"/Drive on NBCSN', (51.3201891, -0.5564726)), ('"/Drive on NBCSN', (24.4538352, 54.3774014)), ('"/Drive on NBCSN', (37.320774, -113.00484758652519)), ('"/Drive on NBCSN', (36.1672559, -115.1485163)), ('"/Drive on NBCSN', (36.2083012, -115.9839128)), ('"/Drive on NBCSN', (36.4951365, -116.421881)), ('"/Drive on NBCSN', (36.4914385, -117.10229360771876)), ('"/Drive on NBCSN', (37.84054795, -119.51658779802511)), ('"10 Films, 1 Box', (34.0536909, -118.242766)), ('"100 Mile Meals', (37.050096, -121.9905908)), ('"15 minutos de fama', (40.7127281, -74.0060152)), ('"2 Awkward Dudes', (40.7127281, -74.0060152))]
print(find_nearest_movies(movie_locations,(36.2672559, -115.1485163)))


