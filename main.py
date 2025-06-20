from re import search

from bs4 import BeautifulSoup
from colorama import Fore, Style, init

from clients import request
from parsers import parse_anime_eps, parse_anime_genres, parse_anime_name

init(autoreset=True)

URL = "https://animego.org/anime/random"


class ParseError(Exception):
    pass


def parse(response) -> bool:
    if not response:
        print("Пустой ответ, парсить нечего...")
        return False

    soup = BeautifulSoup(response.content, "html.parser")

    try:
        anime_name = parse_anime_name(soup)
        anime_eps = parse_anime_eps(soup)
        anime_genres = parse_anime_genres(soup)
    except ParseError as e:
        print(f"Ошибка парсинга: {e}")
        return False

    number_ep_match = search(r"\d+", anime_eps)
    number_ep = number_ep_match.group() if number_ep_match else "0"

    genres_csv = ", ".join(anime_genres)

    print(f"{Fore.CYAN}\n🎬 Информация об аниме 🎬{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}Название:{Style.RESET_ALL} {anime_name}")
    print(f"{Fore.GREEN}Серий:{Style.RESET_ALL} {number_ep}")
    print(f"{Fore.MAGENTA}Жанры:{Style.RESET_ALL} {genres_csv}")
    print(f"{Fore.CYAN}{'=' * 30}{Style.RESET_ALL}\n")

    return True


def main():
    while True:
        response = request(URL)
        if parse(response):
            break


if __name__ == "__main__":
    main()
