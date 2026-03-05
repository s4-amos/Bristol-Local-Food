# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Bristol Local Food Network – a Django 4.2 web platform connecting local food producers with customers in Bristol. Sprint 1 establishes core user authentication, customer registration, and producer registration/dashboard.

## Commands

### Running with Docker (recommended)
```bash
docker-compose up --build          # Start DB + web server
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
```

### Running locally (requires PostgreSQL running separately)
```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

The DB container exposes PostgreSQL on port `5433` (host) → `5432` (container). The web app runs on port `8000`.

### Database credentials (dev)
- DB: `bristol_food`, User: `bristol_user`, Password: `bristol_pass`, Host: `db` (Docker) or `localhost`

### Django management
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py shell
```

## Architecture

### App Structure
- **`core`** – Custom `User` model (email as username field), login/logout views, base templates, home page. All other apps import `User` from here or use `settings.AUTH_USER_MODEL`.
- **`customers`** – `CustomerProfile` (OneToOne → User), customer registration (raw POST handling, no forms), product browsing templates.
- **`producers`** – `ProducerProfile` (OneToOne → User), producer registration via `ProducerRegistrationForm` (ModelForm), dashboard view.
- **`orders`** – Placeholder for Sprint 2+; model file is empty.

### Custom User Model
`core.models.User` extends `AbstractUser` with:
- `email` as the `USERNAME_FIELD` (login identifier)
- `role` field: `'customer'`, `'producer'`, or `'admin'`
- `username` is auto-generated from email if not provided (slug + UUID suffix)

Always reference the user model via `settings.AUTH_USER_MODEL` or `get_user_model()` in other apps — never import `User` directly from `core` in apps other than `customers` (which currently does import directly).

### URL Routing
```
/                → core (home, login, logout)
/customers/      → customers app
/producers/      → producers app (namespace: producers)
/admin/          → Django admin
```

### Registration Flows
- **Customer**: Raw POST processing in `customers/views.py` — creates `User` then `CustomerProfile` atomically.
- **Producer**: Django `ModelForm` (`ProducerRegistrationForm`) that creates `User` + `ProducerProfile` in `form.save()`, then logs the user in.

### Templates
Each app has its own `templates/<app_name>/` directory. The shared base template is `core/templates/core/base.html`. Static CSS/JS is split per-app under `static/css/` and `static/js/` with a shared `global.css`/`global.js`.

### Settings
- `AUTH_USER_MODEL = 'core.User'`
- `LOGIN_URL = 'login'`, `LOGIN_REDIRECT_URL = 'home'`, `LOGOUT_REDIRECT_URL = 'login'`
- DB config reads from env vars: `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT`
