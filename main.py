import requests
from bs4 import BeautifulSoup
import re

def error_handler(error: int):
    error_messages = {
        1: "Error to parse name of anime",
        2: "Error to parse eps. of anime",
        3: "Error to parse genres of anime"
    }
    
    print(error_messages.get(error, "Unknown error"))

def parse(url: str):
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")

        anime_name = soup.find('h1').get_text() if soup.find('h1') else error_handler(1)
        anime_eps = soup.find(class_='col-3 col-sm-2 col-md text-truncate').get_text() if soup.find(class_='col-3 col-sm-2 col-md text-truncate') else error_handler(2)
        anime_genres = soup.find(class_='col-6 col-sm-8 mb-1 overflow-h').find_all('a') if soup.find(class_='col-6 col-sm-8 mb-1 overflow-h') else error_handler(3)

        genres = [link.text.strip() for link in anime_genres]
        number_ep = re.search(r"\d+", anime_eps).group()
        genres_csv = ', '.join(genres)

        if anime_name and anime_eps and genres_csv:
            print(f"Anime name: {anime_name}. Number of episodes: {number_ep} серий. Genres: {genres_csv}.")
        else:
            print("Error: Unable to print info about anime.")
            
    else:
        print(f"Unknown error. Error code: {response.status_code}")


if __name__ == '__main__':
    parse('https://animego.org/anime/random')
