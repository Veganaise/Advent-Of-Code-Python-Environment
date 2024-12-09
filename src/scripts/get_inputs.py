import os

import requests

from config import ROOT_DIR, AOC_DIR


def get_input(year: int, day: int):
    session = _read_session()
    if session:
        data = _download_input(year, day, session)
        _save_input(data, year, day)
    else:
        print('Session is not configured. Check your .session file')
        raise Exception('Session is not configured. Check your .env file')


def _download_input(year: int, day: int, session: str) -> bytes:
    """
    Downloads the input as text from the advent of code site
    """
    cookies = {'session': session}
    url = f'https://adventofcode.com/{year}/day/{day}/input'
    headers = {'User-Agent': 'github.com/AntoineGanne/adventofcode by antoine.ganne+aoc@hotmail.fr'}
    resp = requests.get(url, cookies=cookies, headers=headers)
    resp.raise_for_status()
    return resp.content  # type: ignore


def _save_input(data: bytes, year: int, day: int) -> None:
    inputs_path = os.path.join(AOC_DIR, 'inputs')

    if not os.path.exists((year_path := os.path.join(inputs_path, str(year)))):
        os.mkdir(year_path)

    with open(os.path.join(year_path, f'day_{day:02}.txt'), 'wb') as file:
        file.write(data)


def _read_session():
    target = os.path.join(ROOT_DIR, '../.session')
    path = os.path.abspath(target)

    with open(path) as f:
        return f.read()
