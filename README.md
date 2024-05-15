# Data Collection and Database Creation with SQLAlchemy

## Project Overview
This project involves collecting data from an API, parsing the JSON file to CSV, and then using SQLAlchemy to create a SQLite database. The repository is structured into several directories, each with specific files that contribute to the overall functionality of the project.

## Directory Structure
- `collecting_data/`
  - `api_call.py`: Contains the code to call the API and collect data.
- `json_files/`
  - `json_extraction.py`: Parses the JSON data and converts it to CSV format.
- `database_creation/`
  - `__init__.py`: Initializes the Python package.
  - `models.py`: Defines the SQLAlchemy ORM models for the database.
  - `NPSparks.csv`: CSV file containing data about parks.
  - `NPSCamps.csv`: CSV file containing data about camps.
  - `app.py`: The main script that creates the database and populates it with data.

## app.py Functionality
The `app.py` script performs the following actions:
1. Initializes a session with the database using SQLAlchemy.
2. Reads the `NPSparks.csv` and `NPSCamps.csv` files into pandas dataframes.
3. Iterates over the rows of the dataframes and adds entries to the database.
4. Commits the changes to the database.

## How to Run
1. Ensure you have Python and the necessary packages (`sqlalchemy`, `pandas`) installed.
2. Navigate to the `database_creation/` directory.
3. Run the `app.py` script to create and populate the database:


