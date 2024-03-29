from bs4 import BeautifulSoup
import urllib

HEADER = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}


def get_data(url):
    if not url.startswith("http://"):
        url = "http://" + url
    req = urllib.request.Request(url, headers=HEADER)

    page = urllib.request.urlopen(req)
    html = page.read().decode()
    soup = BeautifulSoup(html, "html.parser")
    title = soup.title.string
    print("Title: ", title)
    return(soup.get_text())