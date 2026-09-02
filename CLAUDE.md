# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Development Commands

- **Run Application**: `python app.py` (Runs on port 5001 with debug mode enabled)
- **Install Dependencies**: `pip install -r requirements.txt`
- **Run Tests**: `pytest`

## Code Architecture

This is a Flask-based web application structured as a starter project for an expense tracker.

- `app.py`: The main entry point. Contains application configuration and all route definitions.
- `database/`: Intended for database utility functions.
    - `db.py`: Placeholder for database connection, initialization, and seeding logic.
- `static/`: Contains static assets.
    - `css/`: Application stylesheets.
    - `js/`: Client-side JavaScript.
- `templates/`: Contains Jinja2 HTML templates for all routes.

## Project Status

The project is currently in a "starter" state with several placeholder routes and files (e.g., `database/db.py` and various routes in `app.py`) that are intended to be implemented as part of a guided exercise.
