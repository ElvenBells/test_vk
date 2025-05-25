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

    def create_collection(self, name: str) -> None:
        """Создает новую коллекцию фильмов."""
        if name in self._collections:
            raise ValueError(f"Коллекция '{name}' уже существует")
        self._collections[name] = []
    
    def add_to_collection(self, collection_name: str, movie_title: str) -> None:
        """Добавляет фильм в коллекцию."""
        if collection_name not in self._collections:
            raise ValueError(f"Коллекция '{collection_name}' не найдена")
        if movie_title not in self._movies:
            raise ValueError(f"Фильм '{movie_title}' не найден")
        if movie_title in self._collections[collection_name]:
            raise ValueError(f"Фильм '{movie_title}' уже есть в коллекции '{collection_name}'")    
        self._collections[collection_name].append(movie_title)
    
    def remove_from_collection(self, collection_name: str, movie_title: str) -> None:
        """Удаляет фильм из коллекции."""
        if collection_name not in self._collections:
            raise ValueError(f"Коллекция '{collection_name}' не найдена")
        if movie_title not in self._collections[collection_name]:
            raise ValueError(f"Фильм '{movie_title}' не найден в коллекции '{collection_name}'")
        self._collections[collection_name].remove(movie_title)

    def __iter__(self) -> Iterator[Movie]:
        """Возвращает итератор для перебора всех фильмов."""
        return iter(self._movies.values())  


if __name__ == "__main__":
    collection = MovieCollection()
    
    collection.add_movie(Movie("Shrek", 2001, "Andrew Ralph Adamson", "Animation", 7.9))
    collection.add_movie(Movie("Shrek 2", 2004, "Andrew Ralph Adamson", "Animation", 7.4))
    collection.add_movie(Movie("The Shawshank Redemption", 1994, "Frank Darabont", "Drama", 9.3))
 
    collection.create_collection("Classics")
    collection.create_collection("Animations")
    
    collection.add_to_collection("Animations", "Shrek")
    collection.add_to_collection("Animations", "Shrek 2")
    collection.add_to_collection("Classics", "The Shawshank Redemption")

    print("\nВсе фильмы в коллекции:")
    for movie in collection:
        print(f"- {movie.title} ({movie.year}), режиссер: {movie.director}")