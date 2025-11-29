# Daily Quotes API

A lightweight, database-free FastAPI application that serves a daily inspirational quote.

## Features

- **Deterministic**: Returns the same quote for everyone on the same day.
- **Database-free**: Quotes are stored in a static file (`data.py`).
- **Lightweight**: Built with FastAPI.
- **Keep-alive**: Includes a script to prevent free-tier hosting from sleeping.

## Setup & Run Locally

1. **Setup Environment**:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

2.  **Install Dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the Server**:

    ```bash
    uvicorn main:app --reload
    ```

4.  **Access the API**:
    Open `http://127.0.0.1:8000` in your browser.

    ## Documentation
- [Collaboration Guide](COLLABORATION.md)
