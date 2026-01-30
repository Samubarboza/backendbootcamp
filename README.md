# Rick and Morty Characters App

This is a Flask web application that connects an external API, a backend server, and a local database to display and store Rick and Morty characters.

The application acts as a middle layer between the browser and the Rick and Morty public API.

---

## What does the app do?

* Retrieves characters from the Rick and Morty API
* Displays characters with pagination
* Allows searching characters by name
* Saves favorite characters in a local database
* Shows and deletes saved favorites

---

## How the app works (intuitive flow)

### 1. User opens the app

The browser sends a request to the Flask server.

```
Browser → Flask
```

---

### 2. Flask requests data from the external API

Flask asks the Rick and Morty API for character data.

```
Flask → Rick and Morty API
```

---

### 3. The API responds with data

The API returns JSON data.

```
Rick and Morty API → Flask (JSON)
```

---

### 4. Flask processes the data

Flask:

* Reads the JSON
* Applies pagination or search
* Prepares the data for the frontend

---

### 5. Data is rendered in HTML

Flask sends HTML pages to the browser.

```
Flask → Browser (HTML)
```

---

### 6. Saving favorites

When the user saves a character:

```
Browser → Flask → SQLite Database
Browser ← Flask
```

---

## High-level flow diagram

```
Browser
   ↓
Flask Backend
   ↓
Rick and Morty API
   ↑
SQLite Database
```

---

## Project architecture

* **Flask** → routes and backend logic
* **Requests** → API consumption
* **SQLAlchemy** → database access
* **SQLite** → local data storage
* **Jinja templates** → HTML rendering

---

## How to run the project

### 1. Clone the repository

```bash
git clone <repository-url>
cd <repository-folder>
```

---

### 2. Create and activate virtual environment

```bash
python -m venv .venv
```

Activate it:

**Windows**

```bash
.venv\Scripts\activate
```

**macOS / Linux**

```bash
source .venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Run the application

```bash
python app.py
```

---

### 5. Open in browser

```text
http://127.0.0.1:5000
```

---

## Notes

* The database is created automatically on first run
* Favorites are stored locally using SQLite
* `.venv`, `__pycache__`, and `app.db` are ignored by Git

---
