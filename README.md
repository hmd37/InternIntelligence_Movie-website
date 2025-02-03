# Movie API

This is a Django-based API that provides movie-related functionalities, including listing movies, retrieving movie details, and searching for movies using TMDB.

## Features

- List all movies
- Retrieve details of a specific movie
- Search for movies using TMDB

## Requirements

- Python 3.x
- Django
- Django REST Framework
- requests (for TMDB API integration)

## Setup

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   cd movie_project
   ```

2. **Install pipenv if not already installed:**

   ```bash
   pip install pipenv
   ```

3. **Install the dependencies:**

   ```bash
   pipenv install
   ```

4. **Activate the virtual environment:**

   ```bash
   pipenv shell
   ```

5. **Apply migrations:**

   ```bash
   python manage.py migrate
   ```

6. **Run the server:**

   ```bash
   python manage.py runserver
   ```
## Endpoints

- **List all movies**  
  `GET /movies/`  
  Retrieves a list of all movies.

- **Create a new movie**  
  `POST /movies/`  
  Adds a new movie to the database.

- **Retrieve movie details**  
  `GET /movies/<movie_id>/`  
  Retrieves details of a specific movie.

- **Update a movie**  
  `PUT /movies/<movie_id>/`  
  Updates the details of an existing movie.

- **Delete a movie**  
  `DELETE /movies/<movie_id>/`  
  Deletes a specific movie from the database.

- **Search for movies using TMDB**  
  `GET /tmdb/?query=`  
  Searches for movies using TMDB API.
