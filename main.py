"""
A module for generating a map with 10 nearest movies
"""
from data_reader import read_data, select_year
from locations_finder import coord_finder, find_nearest_movies
from map_generator import generate_map

def start():
    year = int(input("Please enter a year you would like to have a map for:"))
    user_location = tuple(int(loc) for loc in input("Please enter your location (format: lat, long):").split(','))
    movie_data = read_data("smaller_locations.list")
    n_year_movies = select_year(movie_data,year)
    all_movie_locations = coord_finder(n_year_movies)
    nearest_movie_locations = find_nearest_movies(all_movie_locations, user_location)
    generate_map(nearest_movie_locations,user_location)
    return "Open map.html to enjoy the map."

if __name__=="__main__":
    start()