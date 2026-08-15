
# Contact Book CLI App

A command-line contact book built in Python — add, view, search, and delete contacts, with persistent storage using JSON. Built as the Stage 2 capstone project.

## Features

- **Add Contact** — store name, phone, and email
- **View Contacts** — list all saved contacts
- **Search Contact** — look up a contact by name
- **Delete Contact** — remove a contact by name
- **Save/Load** — contacts persist across sessions via `contacts.json`

## Concepts Applied

- Dictionaries for structured contact records
- Lists for managing the contact collection
- File I/O with the `json` module for persistence
- `try`/`except` for handling missing save files on first run
- Loop-based menu-driven CLI flow

## How to Run

```bash
python ContactBookCLIApp.py
```

Contacts are automatically loaded from `contacts.json` on start (if it exists) and saved back to it when you choose **Save Contacts** or exit.

## Files

| File | Description |
|---|---|
| `ContactBookCLIApp.py` | Main application source code |
| `contacts.json` | Saved contact data (auto-generated) |
