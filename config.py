from typing import Final

BASE_URL: Final[str] = "https://animego.org/anime/random"
ANIME_NAME_SELECTOR: Final[str] = ".anime-title > div:nth-child(1) > h1:nth-child(1)"
ANIME_EPISODES_SELECTOR: Final[str] = "dd.col-6:nth-child(4)"
ANIME_GENRES_SELECTOR: Final[str] = "dd.col-6:nth-child(8) a"
