from typing import List
import requests
from bs4 import BeautifulSoup

def _get_url(month: str, day: int) -> str:
    url = f"https://www.onthisday.com/day/{month}/{day}"
    return url

def _get_page(url: str) -> BeautifulSoup:
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup

def events_of_the_day(month: str, day: int) -> List[str]:
    url = _get_url(month, day)
    page = _get_page(url)
    raw_events = page.find_all(class_='event')
    events = [event.text for event in raw_events]
    return events