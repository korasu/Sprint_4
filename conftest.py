from main import BooksCollector
import pytest


@pytest.fixture()
def books_collection():
    collector = BooksCollector()
    books_with_genre = [("First Book", 'Фантастика'),
                        ("Second Book", 'Ужасы'),
                        ("3", 'Детективы'),
                        ("Long story short in one book w good men", 'Мультфильмы'),
                        ("Simple idea", 'Комедии')
                        ]
    for books in books_with_genre:
        collector.add_new_book(books[0])

    for genre in books_with_genre:
        collector.set_book_genre(genre[0], genre[1])

    return collector
