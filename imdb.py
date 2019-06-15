from bs4 import BeautifulSoup
from simple_scraping import *
import utils

main_page = "https://www.imdb.com/search/title?groups=top_250&sort=user_rating"
pages = [
    main_page,
    main_page + ",desc&start=51&ref_=adv_nxt",
    main_page + ",desc&start=101&ref_=adv_nxt",
    main_page + ",desc&start=151&ref_=adv_nxt",
    main_page + ",desc&start=201&ref_=adv_nxt",
]

save_as = {
    pages[0]: "top_50.html",
    pages[1]: "top_100.html",
    pages[2]: "top_150.html",
    pages[3]: "top_200.html",
    pages[4]: "top_250.html",
}

list_fname = "IMDb_Top_250.txt"

def get_titles(pages, save_pages=False):
    imdb_top_250 = []

    def scrape_page(page):
        raw_html = simple_get(page)
        html = BeautifulSoup(raw_html, 'html.parser')

        if save_pages:
            save_html_page(raw_html, save_as[page])

        for img in html.select('img'):
            alt = img.get("alt", "")
            if alt != "IMDbPro Menu" and alt != "Go to IMDbPro" and alt != "":
                imdb_top_250.append(utils.format_movie_title(alt))

    for page in pages:
        scrape_page(page)

    return imdb_top_250

def scrape_imdb_top_250():
    imdb_top_250 = get_titles(pages)
    utils.save_movie_list(imdb_top_250, fname=list_fname)

    return imdb_top_250