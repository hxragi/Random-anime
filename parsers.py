from typing import List, Optional

from config import ANIME_EPISODES_SELECTOR, ANIME_GENRES_SELECTOR, ANIME_NAME_SELECTOR
from errors import EpisodesParseError, GenresParseError, NameParseError


def parse_anime_name(soup) -> Optional[str]:
    el = soup.select_one(ANIME_NAME_SELECTOR)
    if not el:
        raise NameParseError(selector=ANIME_NAME_SELECTOR)
    return el.get_text(strip=True)


def parse_anime_eps(soup) -> Optional[str]:
    el = soup.select_one(ANIME_EPISODES_SELECTOR)
    if not el:
        raise EpisodesParseError(selector=ANIME_EPISODES_SELECTOR)
    return el.get_text(strip=True)


def parse_anime_genres(soup) -> List[str]:
    els = soup.select(ANIME_GENRES_SELECTOR)
    if not els:
        raise GenresParseError(selector=ANIME_GENRES_SELECTOR)
    return [el.get_text(strip=True) for el in els]
