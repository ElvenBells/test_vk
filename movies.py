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

    def remove_movie(self, title: str) -> None:
        """Удаляет фильм из коллекции."""
        if title not in self._movies:
            raise ValueError(f"Фильм '{title}' не найден в коллекции")
        for collection in self._collections.values():
            if title in collection:
                collection.remove(title)
        del self._movies[title]



if __name__ == "__main__":
    collection = MovieCollection()
    
    collection.add_movie(Movie("Shrek", 2001, "Andrew Ralph Adamson", "Animation", 7.9))
    collection.add_movie(Movie("Shrek 2", 2004, "Andrew Ralph Adamson", "Animation", 7.4))
    collection.add_movie(Movie("The Shawshank Redemption", 1994, "Frank Darabont", "Drama", 9.3))
