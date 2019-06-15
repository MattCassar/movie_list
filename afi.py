from bs4 import BeautifulSoup
from simple_scraping import *
import utils

afi_url = "https://www.afi.com/100years/movies10.aspx"
list_fname = "AFI_Top_100.txt"
html_file = "afi_top_100.html"

def scrape_afi_top_100():
    afi_top_100 = get_top_100(afi_url)
    utils.save_movie_list(afi_top_100, fname=list_fname)

    return afi_top_100


def get_top_100(afi_url, save_page=False):
    afi_top_100 = []
    raw_html = simple_get(afi_url)
    html = BeautifulSoup(raw_html, 'html.parser')

    if save_page:
        save_html_page(raw_html, html_file)

    for label in html.select('label'):
        for item in label.contents:
            afi_top_100.append(utils.format_movie_title(item))

    return afi_top_100