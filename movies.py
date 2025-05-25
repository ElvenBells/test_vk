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
