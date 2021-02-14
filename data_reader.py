"""
Processes locations.list
"""
import re
def raw_line_formatter(raw_line:str):
    """
    Convers raw line into a tuple (name, year, location)
    >>> raw_line_formatter('"#15SecondScare" (2015) {Its Me Jessica (#1.5)}\tCoventry, West Midlands, England, UK')
    ('"#15SecondScare"', 2015, 'Coventry, West Midlands, England, UK')
    """
    line_list = raw_line.split("\t")

    if line_list[0].find("(1") == -1 and line_list[0].find("(2") == -1:
        return ("Film year unknown", 9999, "None")

    pattern = '\d\d\d\d'
    year = re.findall(pattern, line_list[0])[0]
    year_pos = line_list[0].find(year) -2
    name = line_list[0][:year_pos-1]
    # year = int(line_list[0][year_pos+1:year_pos+5])

    if "(" in line_list[-1]:
        location = line_list[-2]
    else:
        location = line_list[-1].rstrip()
    return (name, int(year), location)

# print(raw_line_formatter('"#15SecondScare" (2015) {Its Me Jessica (#1.5)}\tCoventry, West Midlands, England, UK'))
def read_data(database:str):
    """
    Reads location database and returns a list of tuples (name, year, location)
    """
    data_obj = open(database, "r", encoding="utf-8", errors="ignore")
    data_list = [raw_line_formatter(line) for line in list(data_obj)[14:-1]]
    print("Data read")
    return data_list

def select_year(movie_list:list, year:int):

    n_year_movies = []
    for movie in movie_list:
        if year in movie:
            n_year_movies.append((movie[0],movie[-1]))
    return n_year_movies

# data = read_data("locations.list")
# print(select_year(data,2012))