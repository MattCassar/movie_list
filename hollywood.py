from bs4 import BeautifulSoup
from simple_scraping import *
import utils

hollywood_url = '''https://www.hollywoodreporter.com/lists/100\
    -best-films-ever-hollywood-favorites-818512/item/godfather-\
    hollywoods-100-favorite-films-810496'''

list_fname = "Hollywood_Reporter_Top_100.txt"
html_file = "hollywood_top_100.html"

def scrape_hollywood_top_100():
    hollywood_top_100 = get_top_100(hollywood_url)
    utils.save_movie_list(hollywood_top_100, fname=list_fname)

    return hollywood_top_100


def get_top_100(hollywood_url, save_page=False):
    hollywood_top_100 = []
    raw_html = simple_get(hollywood_url)
    html = BeautifulSoup(raw_html, 'html.parser')

    if save_page:
        save_html_page(raw_html, html_file)

    for header in html.select("h1"):
        for item in header.contents:
            if item != "Hollywood's 100 Favorite Films":
                hollywood_top_100.append(utils.format_movie_title(item))

    return list(reversed(hollywood_top_100))