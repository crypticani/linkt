import requests
import bs4
import lxml


def fetch_title(res):
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    title = soup.select('title')
    print(title)


if __name__ == "__main__":
    print("Enter the link: ")
    link = input('linkt> ')
    res = requests.get(link)
    fetch_title(res)
