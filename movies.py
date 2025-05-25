from typing import Dict, List, Optional, Iterator
from dataclasses import dataclass

@dataclass
class Movie:
    """Класс для представления фильма."""
    title: str
    year: int
    director: str
    genres: str
    rating: float

class MovieCollection:
    """Класс для управления коллекцией фильмов."""
    def __init__(self) -> None:
        self._movies: Dict[str, Movie] = {}
        self._collections: Dict[str, List[str]] = {}
    
    def add_movie(self, movie: Movie) -> None:
        """Добавляет фильм в коллекцию."""
        if movie.title in self._movies:
            raise ValueError(f"Фильм '{movie.title}' уже существует в коллекции")
        self._movies[movie.title] = movie