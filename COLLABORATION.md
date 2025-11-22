# Collaboration Guide

Thank you for exploring **QPI (Daily Quotes API)**. This guide explains how to contribute and keep the project simple and clean.

## Ways You Can Contribute

- Fix bugs or edge cases  
- Add or refine quotes in `data.py`  
- Improve documentation or examples  
- Enhance error handling or response structure  
- Add tests or lightweight tooling  
- Help with deployment configs  

If unsure about an idea, open an issue first.

## Getting Started

### 1. Fork and clone

```bash
git clone https://github.com/<your-username>/QPI.git
cd QPI
````

### 2. Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate    # Windows: .venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the server

```bash
uvicorn main:app --reload
```

### 5. Test the API

* Root: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
* Docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## Project Structure

* `main.py` — FastAPI routes and quote selection logic
* `data.py` — Quote list
* `keep_alive.py` — Keeps free-tier hosting alive
* `requirements.txt` — Python dependencies
* `Procfile` — Deployment definition

## Adding or Editing Quotes

* Open `data.py`
* Follow the existing structure
* Keep formatting consistent
* Avoid duplicates
* Use real authors when possible

If you change the structure, update `main.py` too.

## Code Style

* Use type hints
* Keep code small and readable
* Avoid heavy dependencies
* Follow PEP 8 where reasonable
* Quote selection must stay deterministic

## Issues

Use GitHub Issues for:

* Bugs
* Feature requests
* Clarifications

Include environment details and logs where relevant.

## Pull Request Workflow

1. Fork the repo
2. Create a branch

```bash
git checkout -b feature/<name>
```

3. Make changes
4. Test locally
5. Commit clearly

```bash
git commit -m "Add <feature>"
```

6. Push and open a PR

PR description should include:

* What changed
* Whether it affects public API
* Related issue numbers

## Backward Compatibility

* Do not remove existing fields
* Do not change response structure silently
* Document any breaking change fully

## Roadmap Ideas

* Tags or categories for quotes
* Health or meta endpoint
* Basic test suite
* Multi language support
* Lightweight rate limiting example

Open an issue before starting large features.

## Code of Conduct

* Be respectful
* No harassment or personal attacks
* Assume good intent but give honest feedback
