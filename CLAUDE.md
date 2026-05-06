# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Architecture Overview
The application uses a standard Django setup organized under `calories_app`.

**Core Components:**
*   `calories_app/core/`: Contains global configuration settings (`settings.py`), root URL routing (`urls.py`), and WSGI entry points. This directory manages the overall behavior of the web application.
*   `calories_app/tracker/`: This is the primary functional app responsible for tracking calorie data. It contains models (`models.py`), forms, views, and templates specific to the tracking feature (e.g., `templates/tracker/index.html`).

**Data Flow:**
The system utilizes a Django ORM structure defined in `calories_app/tracker/models.py`. Data interaction flows from views (in `views.py`) which utilize forms (`forms.py`) to interact with the models, and is managed via migrations located in `calories_app/tracker/migrations`.

## Development Workflow
When developing or debugging this application, these commands are frequently used:

**1. Running the Application:**
To start the local development server:
`python manage.py runserver`

**2. Database & Migrations:**
*   Generate new migration files for changes in `tracker/models.py`:
    `python manage.py makemigrations tracker`
*   Apply migrations to update the database schema:
    `python manage.py migrate`

**3. Testing:**
To run tests specifically for the `tracker` app, which is the core feature set:
`python manage.py test tracker`

## Key Directories and Files
*   **Configuration:** All environment-specific settings are located in `calories_app/core/settings.py`.
*   **Tracking Logic:** The primary business logic resides within the `tracker` app.
*   **Templates:** HTML templates used for rendering pages are kept in `calories_app/tracker/templates/tracker/`.