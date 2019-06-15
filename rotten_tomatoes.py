from bs4 import BeautifulSoup
from simple_scraping import *
import utils

rt_url = "https://www.rottentomatoes.com/top/bestofrt/"
list_fname = "Rotten_Tomatoes_Top_100.txt"
html_file = "rt_top_100.html"

def scrape_rt_top_100():
    rt_top_100 = get_top_100(rt_url)
    rt_top_100 = [movie.strip() for movie in rt_top_100]
    
    utils.save_movie_list(rt_top_100, fname=list_fname)

    return rt_top_100

def get_top_100(rt_url, save_page=False):
    rt_top_100 = []
    raw_html = simple_get(rt_url)
    html = BeautifulSoup(raw_html, 'html.parser')

    if save_page:
        save_html_page(raw_html, html_file)

    for a in html.select("a"):
        if a is not None and a.has_attr("class") and a.get("class") == "unstyled articleLink".split():
            for content in a.contents:
                if content != "View All" and content is not None:
                    rt_top_100.append(utils.format_movie_title(str(content)))
    
    return rt_top_100[-100:]