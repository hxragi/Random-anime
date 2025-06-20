import time

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
            print("Too many requests, ждем...")
            time.sleep(delay)
        else:
            print(f"Ошибка HTTP: {response.status_code}")
            return None
    return None
