from bs4 import BeautifulSoup
from simple_scraping import *
import utils

main_page = '''https://www.metacritic.com/browse/movies/score/metascore/\
               all/filtered'''
extension = "?page="
pages = [main_page] + [main_page + extension + str(i) for i in range(1, 4)]
save_as = {page: "metacritic_top_{}.html".format((i + 1)*100) for i, page in enumerate(pages)}
list_fname = "Metacritic_Top_400.txt"

def get_titles(pages, save_pages=False):
    metacritic_top_400 = []

    def scrape_page(page):
        raw_html = simple_get(page)
        html = BeautifulSoup(raw_html, 'html.parser')

        if save_pages:
            save_html_page(raw_html, save_as[page])

        for header in html.select('h3'):
            for content in header.contents:
                metacritic_top_400.append(utils.format_movie_title(content))

    for page in pages:
        scrape_page(page)

    return metacritic_top_400


def scrape_metacritic_top_400():
    metacritic_top_400 = get_titles(pages)
    utils.save_movie_list(metacritic_top_400, fname=list_fname)

    return metacritic_top_400