# aipo-document-recognition

Analysis and Image Processing project, which aim is to create a desktop app, that will recognize documents and insert the data found on them into the database

## Requirements

## To run the project

Before running the project, ensure you have PostgreSQL installed and its binaries added to PATH.

For example, for PostgreSQL 16, you should add following entry to PATH:

```
C:\Program Files\PostgreSQL\16\bin
```

1. Create a python environment (version 3.12 is recommended)
2. Install requirements

```py
pip install -r requirements.txt
```

4. In the .env file, set environment variables:

- `DB_USERNAME` - username and the database name
- `DB_PASSWORD` - password to database
- `DB_HOSTNAME` - database hostname
- `PYTESSERACT_PATH` - path to `tesseract` executable (required, if running app on Windows)

3. Run the program

```py
python main.py
```
