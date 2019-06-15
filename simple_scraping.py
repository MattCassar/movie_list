from bs4 import BeautifulSoup
from contextlib import closing
from requests import get
from requests.exceptions import RequestException
import logging
from datetime import datetime
import os

date = str(datetime.now().time().isoformat(timespec="seconds"))
directory = str(datetime.today().date())

if not os.path.exists("logging/{}".format(directory)):
    os.mkdir("logging/{}".format(directory))

logging_file = "logging/{}/{}.log".format(directory, date)
logging.basicConfig(filename=logging_file)

USER_AGENT = '''Mozilla/5.0 (Macintosh; Intel Mac \
    OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 \
    Safari/537.36'''

def simple_get(url, timeout=20):
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None.
    """
    user_agent = {'User-Agent': USER_AGENT}

    try:
        with closing(get(url, stream=False, timeout=timeout, headers=user_agent)) as resp:
            logging.info("Request to {}: received Status Code {}".format(url, resp.status_code))
            if is_good_response(resp):
                return resp.content
            else:
                logging.error("Bad response when accessing {}: {}".format(url, resp.text))
                return None

    except RequestException as e:
        logging.error("Error during requests to {} : {}".format(url, str(e)))
        return None


def is_good_response(resp):
    """
    Returns True if the response seems to be HTML, False otherwise. 
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200 
            and content_type is not None 
            and content_type.find('html') > -1)


def save_html_page(raw_html, fname):
    '''
    Save the raw HTML file
    '''
    file = open("html/{}".format(fname), "w")
    file.write(str(raw_html))
    file.close()