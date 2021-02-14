"""
Finding 10 nearest locations
"""
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
from data_reader import read_data, select_year

data = read_data("locations.list")
print(select_year(data,2012)[:30])
# data = [('nOfficially Your', 'Kota Kelaurga Resort, Laiya, San Juan, Batangas, Philippines'),
#         ('nOfficially Your', 'Legaspi Towers, Roxas Boulevard, Manila, Metro Manila, Philippines'),
#         ('nOfficially Your', 'Intramuros, Manila, Metro Manila, Philippines'),
#         (' solo questione di punti di vist', "Firenzuola's lake, Umbria, Italy"),
#         (' solo questione di punti di vist', 'Fogliano, Umbria, Italy'),
#         (' solo questione di punti di vist', 'Naples, Campania, Italy'),
#         (' solo questione di punti di vist', 'Naples, Campania, Italy')]
data = [('"#ByMySide', 'Alessandria, Piedmont, Italy'), ('"#LakeShow', 'El Segundo, California, USA'), ('"#LdnOnt', 'London, Ontario, Canada'), ('"#NerdNoise', 'Los Angeles, California, USA'), ('"10 Reviews in 10 Minutes', 'Norwich, Norfolk, England, UK'), ('"10 Reviews in 10 Minutes', 'Norwich, Norfolk, England, UK'), ('"10 Things I Hate', 'Washington, USA'), ('"10 Things I Hate', 'Steilacoom, Washington, USA'), ('"10 Things I Hate', 'Los Angles, California, USA'), ('"100 Bullets D\'Argento', 'Rome, Lazio, Italy'), ('"13 Steps Down', 'Notting Hill, London, England, UK'), ('"13 Steps Down', 'Ireland'), ('"13 Steps Down', 'England, UK'), ('"13 Steps Down', 'England, UK'), ('"18.0', 'Seville, Seville, Andaluca, Spain'), ('"2 Shot the Show', 'New York City, New York, USA'), ('"2012 Aussie Millions Poker Championship" (2013) {(#1.1', 'Melbourne, Australia'), ('"2012 Aussie Millions Poker Championship" (2013) {(#1.10', 'Melbourne, Australia'), ('"2012 Aussie Millions Poker Championship" (2013) {(#1.2', 'Melbourne, Australia'), ('"2012 Aussie Millions Poker Championship" (2013) {(#1.3', 'Melbourne, Australia'), ('"2012 Aussie Millions Poker Championship" (2013) {(#1.4', 'Melbourne, Australia'), ('"2012 Aussie Millions Poker Championship" (2013) {(#1.5', 'Melbourne, Australia'), ('"2012 Aussie Millions Poker Championship" (2013) {(#1.6', 'Melbourne, Australia'), ('"2012 Aussie Millions Poker Championship" (2013) {(#1.7', 'Melbourne, Australia'), ('"2012 Aussie Millions Poker Championship" (2013) {(#1.8', 'Melbourne, Australia'), ('"2012 Aussie Millions Poker Championship" (2013) {(#1.9', 'Melbourne, Australia'), ('"2012 ECAC Men\'s Hockey Championship" (201', 'Atlantic City, New Jersey, USA'), ('"2012 Presidential Debates" (2012) {(#1.1', 'Magness Center, University of Denver - 2240 E. Buchtel Boulevard, Denver, Colorado, USA'), ('"2012 Presidential Debates" (2012) {(#1.2', 'David S. Mack Sports and Exhibition Complex, Hofstra University - 245 N. Hofstra Avenue, Hempstead, New York, USA'), ('"2012 Presidential Debates" (2012) {(#1.3', 'Wold Performing Arts Center, Lynn University - 3601 N. Military Trail, Boca Raton, Florida, USA')]

def coord_finder(movie_list):
    geolocator = Nominatim(user_agent="nearby seymovies")
    movie_loc_list = []
    loc_dict = {}
    for movie in movie_list:
        loc = loc_dict.get(movie[1], False)  # check if this is a new location
        if not loc:  # if this is a new location entry
            loc_dict[movie[1]] = geolocator.geocode(movie[1])
            loc = loc_dict.get(movie[1])
        if loc:  # if geopy found the location
            loc = loc.point[:-1]
        movie_loc_list.append((movie[0], loc))

    print(movie_loc_list)
    # geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)
    # movie_locations = [(movie[0], geolocator.geocode(movie[1])) for movie in movie_list]
    # locations_dict = dict()
    # for movie in movie_list:
    #     location = locations_dict.get(movie[1])

    # movie_locations = [(loc[0], [loc[1].point[:-1]]) for loc in movie_locations if loc[1]]
    # full_movie_data = zip(movie_list[0],movie_locations)
    # for movie in movie_list:
    #     print(movie)
    #     loc_name = movie[1]
    #     location = geolocator.geocode(loc_name)
    #     movie[1] = (location.latitude, location.longitude)
        # print(movie_list)
    return movie_loc_list
print(coord_finder(data))