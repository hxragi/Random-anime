import requests
from bs4 import BeautifulSoup


bs = BeautifulSoup
r = requests


def parse(url: str):
    response = r.get(url)
    
    if response.status_code == 200:
        print("All is ok")
        # TODO: make a parse anime name. To make this use bs4 and do search for class name "anime-title"
    else:
        print(f"Unknown error. Code: {response.status_code}")


if __name__ == '__main__':
    parse('https://animego.org/anime/random')