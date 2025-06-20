from typing import List, Optional


class ParseError(Exception):
    pass


class NameParseError(ParseError):
    pass


class EpisodesParseError(ParseError):
    pass


class GenresParseError(ParseError):
    pass


def parse_anime_name(soup) -> Optional[str]:
    el = soup.select_one(".anime-title > div:nth-child(1) > h1:nth-child(1)")
    if not el:
        raise NameParseError("Failed to parse anime name")
    return el.get_text(strip=True) if el else None


def parse_anime_eps(soup) -> Optional[str]:
    el = soup.select_one("dd.col-6:nth-child(4)")
    if not el:
        raise EpisodesParseError("Failed to parse anime episodes")
    return el.get_text(strip=True) if el else None


def parse_anime_genres(soup) -> List[str]:
    els = soup.select("dd.col-6:nth-child(8) a")
    if not els:
        raise GenresParseError("Failed to parse anime genres")
    return [el.get_text(strip=True) for el in els]
