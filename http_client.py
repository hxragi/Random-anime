import time

from main import logger
from requests import get


def request(
    url,
    retries=3,
    delay=2,
):
    for i in range(retries):
        response = get(url)
        if response.status_code == 200:
            return response
        if response.status_code == 429:
            logger.warning("Too many requests, ждем...")
            time.sleep(delay * (2**i))
            continue
        if response.status_code in (500, 503):
            logger.error(f"Серверная ошибка: {response.status_code}")
            continue
        else:
            logger.error(f"Ошибка HTTP: {response.status_code}")
            return None
    logger.error(f"Не удалось выполнить запрос после {retries} попыток.")
    return None
