from re import search
from typing import List, Optional, Tuple

from bs4 import BeautifulSoup
from colorama import Fore, Style

from config import BASE_URL
from errors import NameParseError, EpisodesParseError, GenresParseError
from http_client import request
from parsers import parse_anime_eps, parse_anime_genres, parse_anime_name

from utils import logger


def parse(response) -> Optional[Tuple[Optional[str], int, List[str]]]:
    if response is None:
        logger.error("Ответ пустой или отсутствует контент")
        return None

    soup = BeautifulSoup(response.content, "lxml")

    try:
        anime_name = parse_anime_name(soup)
        anime_eps = parse_anime_eps(soup)
        anime_genres = parse_anime_genres(soup)
    except NameParseError as e:
        logger.error("Ошибка парсинга названия, селектор: %s", e.selector)
        return None
    except EpisodesParseError as e:
        logger.error("Ошибка парсинга эпизодов, селектор: %s", e.selector)
        return None
    except GenresParseError as e:
        logger.error("Ошибка парсинга жанров, селектор: %s", e.selector)
        return None

    number_ep = 0
    if anime_eps:
        match = search(r"\d+", anime_eps)
        number_ep = int(match.group()) if match else 0

    return anime_name, number_ep, anime_genres


def print_anime_info(name: str, eps: int, genres: List[str]) -> None:
    genres_joined = ", ".join(genres)
    print(
        f"{Fore.CYAN}\n🎬 Информация об аниме 🎬{Style.RESET_ALL}\n"
        f"{Fore.YELLOW}Название:{Style.RESET_ALL} {name}\n"
        f"{Fore.GREEN}Серий:{Style.RESET_ALL} {eps}\n"
        f"{Fore.MAGENTA}Жанры:{Style.RESET_ALL} {genres_joined}\n"
        f"{Fore.CYAN}{'=' * 30}{Style.RESET_ALL}\n"
    )


def main(max_attempts=5):
    for _ in range(max_attempts):
        response = request(BASE_URL)
        result = parse(response)
        if result:
            name, eps, genres = result
            print_anime_info(name, eps, genres)
            return
    logger.error("Не удалось получить данные после %s попыток.", max_attempts)
    return None


if __name__ == "__main__":
    main()