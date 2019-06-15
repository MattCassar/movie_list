import scrape_movies
import utils
import numpy as np 
from graph import Graph

def get_rank(movie, movie_list):
    try:
        rank = movie_list.index(movie) + 1

    except ValueError:
        rank = 0

    return rank


def average_rank(movie, movie_lists):
    rank = 0
    count = 0

    for movie_list in movie_lists:
        temp_rank = get_rank(movie, movie_list)
        count = count + 1 if temp_rank > 0 else count    
        rank += temp_rank

    if count > 1:
        avg_rank = (rank / count ** 2)

    else:
        avg_rank = rank * len(movie_lists)**2

    return avg_rank, count


def create_word_graph(union):
    graph = Graph()
    for movie in union:
        words = movie.split()
        v1, v2 = words[0:-1], words[1:]
        for vertex_from, vertex_to in zip(v1, v2):
            try:
                graph.add_edge((vertex_from, vertex_to, 1))

            except Exception:
                w = graph.edges[vertex_from][vertex_to] + 1
                graph.update_edge(vertex_from, vertex_to, w)

    graph.create_adjacency_matrix()

    return graph


def create_distance_matrix(movie_ranks, names):
    graph = Graph()
    for i, rank1 in enumerate(movie_ranks):
        for j, rank2 in enumerate(movie_ranks[i:]):
            dist = np.linalg.norm(rank1 - rank2)
            j += i
            try:
                graph.add_edge((names[i], names[j], dist))

            except ValueError:
                graph.update_edge(names[i], names[j], dist)

            print(names[i], names[j])
    graph.create_adjacency_matrix()

    return graph

imdb, afi, rt, mc, hw = scrape_movies.get_movie_lists()
movie_lists = [imdb, afi, rt, mc, hw]

union = utils.union(movie_lists)
intersection = utils.intersect(movie_lists)

ranks = {}
counts = {}
for movie in union:
    rank, count = average_rank(movie, movie_lists)
    ranks[movie], counts[movie] = rank, count

top_movies = sorted(ranks, key=ranks.get)
with open("movie_lists/aggregate_top_100.txt", "w") as file:
    for rank, movie in enumerate(top_movies[:100]):
        file.write(str(rank + 1) + ". " + movie + "\n")


union = sorted(union)
imdb_ranks = np.zeros((len(union), 1))
afi_ranks = np.zeros((len(union), 1))
rt_ranks = np.zeros((len(union), 1))
mc_ranks = np.zeros((len(union), 1))
hw_ranks = np.zeros((len(union), 1))

aggregate_ranks = np.zeros((len(union), 1))

for i, movie in enumerate(union):
    imdb_ranks[i] = 100 - get_rank(movie, imdb[:100])
    afi_ranks[i] = 100 - get_rank(movie, afi[:100])
    rt_ranks[i] = 100 - get_rank(movie, rt[:100])
    mc_ranks[i] = 100 - get_rank(movie, mc[:100])
    hw_ranks[i] = 100 - get_rank(movie, hw[:100])
    aggregate_ranks[i] = 100 - get_rank(movie, top_movies[:100])

movie_ranks = [aggregate_ranks, imdb_ranks, afi_ranks, rt_ranks, mc_ranks, hw_ranks]
names = [
    "Aggregate", 
    "IMDb", 
    "AFI", 
    "Rotten Tomatoes", 
    "Metacritic", 
    "Hollywood Reporter"
]
word_graph = create_word_graph(union)
distance_graph = create_distance_matrix(movie_ranks, names)

for i, v1 in enumerate(names):
    for v2 in names[i+1:]:
        print("Distance from {} to {} = {}".format(v1, v2, distance_graph.edges[v1][v2]))