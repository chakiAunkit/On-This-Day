from fastapi import FastAPI
import services

app = FastAPI()

@app.get('/')
async def root():
    return {'Message': 'Welcome to this fastapi app, please redirect to /docs'}

@app.get('/events')
async def all_events():
    return services.get_all_events()

@app.get('/events/today')
async def event_of_today():
    return services.get_today()

@app.get('/events/{month}')
async def get_events_of_month(month: str):
    return services.get_month_events(month)

@app.get('/events/{month}/{day}')
async def get_events_of_day(month: str, day: int):
    return services.get_events_of_day(month, day)