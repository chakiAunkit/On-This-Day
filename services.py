from asyncio import events
from typing import Dict
import datetime as _dt
import json 

def get_all_events() -> Dict:
    with open("events.json") as f:
        data = json.load(f) 
    return data

def get_month_events(month: str) -> Dict:
    events = get_all_events()
    month = month.lower()
    try:
        month_event = events[month]
        return month_event
    except KeyError:
        return "This is not a valid month"

def get_events_of_day(month: str, day: int) -> Dict:
    events = get_all_events()
    month = month.lower()
    try:
        event = events[month][str(day)]
        return event
    except KeyError:
        return "This is not a valid month or day"

def get_today():
    today = _dt.date.today()
    month = today.strftime("%B")
    return get_events_of_day(month, today.day)