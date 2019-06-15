import afi
import imdb
import rotten_tomatoes as rt
import metacritic as mc
import hollywood as hw
import utils
import os


def get_movie_lists():
    file_path = lambda fname: "movie_lists/{}".format(fname)
    if imdb_list_exists():
        imdb_list = utils.read_movie_list_from_file(file_path(imdb.list_fname))
    else:
        print("...scraping IMDb")
        imdb_list = imdb.scrape_imdb_top_250()

    if afi_list_exists():
        afi_list = utils.read_movie_list_from_file(file_path(afi.list_fname))
    else:
        print("...scraping AFI")
        afi_list = afi.scrape_afi_top_100()

    if rt_list_exists():
        rt_list = utils.read_movie_list_from_file(file_path(rt.list_fname))
    else:
        print("...scraping Rotten Tomatoes")
        rt_list = rt.scrape_rt_top_100()

    if mc_list_exists():
        mc_list = utils.read_movie_list_from_file(file_path(mc.list_fname))
    else:
        print("...scraping Metacritic")
        mc_list = mc.scrape_metacritic_top_400()
    
    if hw_list_exists():
        hw_list = utils.read_movie_list_from_file(file_path(hw.list_fname))
    else:
        print("...scraping Hollywood Reporter")
        hw_list = hw.scrape_hollywood_top_100()

    print("Done scraping!\n")

    return imdb_list, afi_list, rt_list, mc_list, hw_list


def imdb_list_exists():
    return os.path.isfile("movie_lists/IMDb_Top_250.txt")


def afi_list_exists():
    return os.path.isfile("movie_lists/AFI_Top_100.txt")


def rt_list_exists():
    return os.path.isfile("movie_lists/Rotten_Tomatoes_Top_100.txt")


def mc_list_exists():
    return os.path.isfile("movie_lists/Metacritic_Top_400.txt")


def hw_list_exists():
    return os.path.isfile("movie_lists/Hollywood_Reporter_Top_100.txt")