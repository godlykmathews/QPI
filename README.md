# Daily Quotes API

A lightweight, database-free FastAPI application that serves a daily inspirational quote.

## Features

- **Deterministic**: Returns the same quote for everyone on the same day.
- **Database-free**: Quotes are stored in a static file (`data.py`).
- **Lightweight**: Built with FastAPI.
- **Keep-alive**: Includes a script to prevent free-tier hosting from sleeping.

## Setup & Run Locally

1.  **Install Dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

2.  **Run the Server**:

    ```bash
    uvicorn main:app --reload
    ```

3.  **Access the API**:
    Open `http://127.0.0.1:8000` in your browser.
