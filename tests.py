import pytest
from main import BooksCollector

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
    @pytest.mark.parametrize('name', ['', 'Очень длинное название книги больше сорока символов'])
    def test_add_new_book_invalid_name_not_added(self, name):
        collector = BooksCollector()

        collector.add_new_book(name)

        assert name not in collector.get_books_genre()

    def test_add_new_book_book_has_no_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Гарри Поттер')

        assert collector.get_book_genre('Гарри Поттер') == ''

    def test_set_book_genre_valid_genre_success(self):
        collector = BooksCollector()

        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')

        assert collector.get_book_genre('Гарри Поттер') == 'Фантастика'

    def test_get_book_genre_returns_correct_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')

        assert collector.get_book_genre('Оно') == 'Ужасы'

    def test_get_books_with_specific_genre_returns_correct_books(self):
        collector = BooksCollector()

        collector.add_new_book('Оно')
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Оно', 'Ужасы')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')

        assert collector.get_books_with_specific_genre('Ужасы') == ['Оно']

    def test_get_books_genre_returns_books_genre_dictionary(self):
        collector = BooksCollector()

        collector.add_new_book('Гарри Поттер')

        assert collector.get_books_genre() == {'Гарри Поттер': ''}

    def test_get_books_for_children_excludes_age_rating_genres(self):
        collector = BooksCollector()

        collector.add_new_book('Добрая книга')
        collector.add_new_book('Страшная книга')
        collector.set_book_genre('Добрая книга', 'Мультфильмы')
        collector.set_book_genre('Страшная книга', 'Ужасы')

        assert collector.get_books_for_children() == ['Добрая книга']

    def test_add_book_in_favorites_added_book_success(self):
        collector = BooksCollector()

        collector.add_new_book('Гарри Поттер')
        collector.add_book_in_favorites('Гарри Поттер')

        assert collector.get_list_of_favorites_books() == ['Гарри Поттер']

    def test_delete_book_from_favorites_existing_book_success(self):
        collector = BooksCollector()

        collector.add_new_book('Гарри Поттер')
        collector.add_book_in_favorites('Гарри Поттер')
        collector.delete_book_from_favorites('Гарри Поттер')

        assert collector.get_list_of_favorites_books() == []    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()