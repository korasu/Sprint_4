from main import BooksCollector
import pytest


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    books = ["First Book", "Second Book", "3", "Long story short in one book w good men", "Simple idea"]

    @pytest.mark.parametrize('books', books)
    def test_add_new_book_added_few_books(self, books):
        collector = BooksCollector()
        collector.add_new_book(books)

        assert list(collector.get_books_genre().keys()) == [books]

    @pytest.mark.parametrize('book', ['Long story short in one book with good men and dog', ''])
    def test_add_new_book_try_added_incorrect_named_book(self, book):
        collector = BooksCollector()

        collector.add_new_book(book)

        assert len(collector.get_books_genre()) == 0

    books_with_genre = [("First Book", 'Фантастика'),
                        ("Second Book", 'Ужасы'),
                        ("3", 'Детективы'),
                        ("Long story short in one book w good men", 'Мультфильмы'),
                        ("Simple idea", 'Комедии')
                        ]

    @pytest.mark.parametrize('book,genre', books_with_genre)
    def test_set_book_genre_added_all_genre(self, book, genre):
        collector = BooksCollector()

        collector.add_new_book(book)
        collector.set_book_genre(book, genre)

        assert collector.get_book_genre(book) == genre

    def test_get_book_genre_correct_return(self):
        collector = BooksCollector()

        collector.add_new_book("The Whispers")
        collector.set_book_genre("The Whispers", "Ужасы")

        assert collector.get_book_genre("The Whispers") == "Ужасы"

    def test_get_books_with_specific_genre_comedy(self, books_collection):
        assert books_collection.get_books_with_specific_genre('Комедии') == ['Simple idea']

    def test_get_books_genre_return_correct_dictionary(self):
        collector = BooksCollector()

        collector.add_new_book('Test book')

        assert len(collector.get_books_genre()) == 1

    def test_get_books_for_child_correct_return(self, books_collection):
        assert books_collection.get_books_for_children() == ["First Book", "Long story short in one book w good men",
                                                             "Simple idea"]

    def test_add_book_in_favorites_added_book_to_list(self):
        collector = BooksCollector()

        collector.add_new_book('Green mile')
        collector.add_book_in_favorites('Green mile')

        assert collector.get_list_of_favorites_books() == ['Green mile']

    def test_delete_from_favorites_taken_empty_list(self):
        collector = BooksCollector()

        collector.add_new_book('Green mile')
        collector.add_book_in_favorites('Green mile')
        collector.delete_book_from_favorites('Green mile')

        assert collector.get_list_of_favorites_books() == []

    def test_get_list_of_favorites_books_empty_list(self):
        collector = BooksCollector()

        assert collector.get_list_of_favorites_books() == []
