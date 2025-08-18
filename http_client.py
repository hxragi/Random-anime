import time

from utils import logger
from types_request import get


def request(
    url,
    retries=3,
    delay=2,
):
    for i in range(retries):
        response = get(url, timeout=delay)
        if response.status_code == 200:
            return response
        if response.status_code == 429:
            logger.warning("Too many requests, ждем...")
            time.sleep(delay * (2**i))
            continue
        if response.status_code in (500, 503):
            logger.error("Серверная ошибка: %s", response.status_code)
            continue
        else:
            logger.error("Ошибка HTTP: %s", response.status_code)
            return None
    logger.error("Не удалось выполнить запрос после %s попыток.", retries)
    return None
