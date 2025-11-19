from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
from data import quotes

app = FastAPI()

# Allow all origins for simplicity in this lightweight app
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def get_daily_quote():
    """
    Returns a deterministic quote based on the current day of the year.
    """
    day_of_year = datetime.now().timetuple().tm_yday
    quote_index = day_of_year % len(quotes)
    return {"quote": quotes[quote_index], "day_of_year": day_of_year}

@app.get("/health")
def health_check():
    return {"status": "ok"}
