import re

def remove_movie_rank(movie):
    pattern = "\d+\."
    movie = re.split(pattern, movie)

    try:
        return movie[1].strip()

    except Exception:
        return movie[0].strip()


def remove_years(movie_list):
    movie_list = movie_list.split("(")

    return movie_list[0].strip()


def clean_list(movie_list):
    return [remove_movie_rank(remove_years(movie)) for movie in  movie_list]


def format_movie_title(movie_title):
    return remove_years(remove_movie_rank(movie_title)).strip().title()


def intersect(movie_lists):
    intersection = set(movie_lists[0])
    for movie_list in movie_lists:
        intersection = intersection.intersection(movie_list)

    return list(intersection)


def union(movie_lists):
    union = set(movie_lists[0])
    for movie_list in movie_lists:
        union = union.union(movie_list)

    return list(union)


def save_movie_list(movie_list, fname=None):
    with open("movie_lists/{}".format(fname), "w") as file:
        for rank, movie in enumerate(movie_list):
            file.write("{}. {}\n".format(rank + 1, movie))


def read_movie_list_from_file(filename):
    movie_list = []
    with open(filename, "r") as file:
        for line in file:
            movie_list.append(format_movie_title(line))

    return movie_list