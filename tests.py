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
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    def test_add_new_book_added_book_has_empty_genre_true(self):
        collector = BooksCollector()
        collector.add_new_book('Тошнота')
        assert collector.books_genre['Тошнота'] == ''

    @pytest.mark.parametrize('name', [
        '',
        '12345678901234567890123456789012345678901',
        '123456789012345678901234567890123456789012345678901234567890'])
    def test_add_new_book_invalid_length_name_not_added(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert collector.books_genre == {}

    def test_set_book_genre_true(self):
        collector = BooksCollector()
        collector.books_genre = \
            {
                'Ходячий замок':
                    'Мультфильмы',
                'Достать ножи':
                    'Детективы',
                'Оно':
                    'Ужасы',
                'Ведьмак':
                    ''
            }
        collector.set_book_genre('Ведьмак', 'Фантастика')
        assert collector.books_genre['Ведьмак'] == 'Фантастика'

    @pytest.mark.parametrize('name', [
        'Ходячий замок',
        'Достать ножи',
        'Оно',
        'Ведьмак',
        ])
    def test_get_book_genre_true(self, name):
        collector = BooksCollector()
        collector.books_genre = \
            {
                'Ходячий замок':
                    'Мультфильмы',
                'Достать ножи':
                    'Детективы',
                'Оно':
                    'Ужасы',
                'Ведьмак':
                    'Фантастика'
            }
        assert collector.get_book_genre(name) == collector.books_genre[name]

    def test_get_books_with_specific_genre_valid_genre_true(self):
        collector = BooksCollector()
        collector.books_genre = \
            {
                'Ходячий замок':
                    'Мультфильмы',
                'Достать ножи':
                    'Детективы',
                'Оно':
                    'Ужасы',
                'Ведьмак':
                    'Фантастика'
            }
        assert collector.get_books_with_specific_genre('Детективы') == ['Достать ножи']

    def test_get_books_for_children_book_without_age_rating_true(self):
        collector = BooksCollector()
        collector.books_genre = {
            'Ходячий замок':
                'Мультфильмы'}
        assert collector.get_books_for_children() == [
            'Ходячий замок']

    def test_get_books_for_children_books_with_age_rating_not_added(self):
        collector = BooksCollector()
        collector.books_genre = {
            'Ходячий замок':
                'Мультфильмы',
            'Достать ножи':
                'Детективы',
            'Оно':
                'Ужасы'}
        assert collector.get_books_for_children() == [
            'Ходячий замок']

    def test_add_book_in_favorites_recurring_book_is_added_once(self):
        collector = BooksCollector()
        collector.books_genre = {'Достать ножи': ''}
        collector.favorites = ['Достать ножи']
        collector.add_book_in_favorites('Достать ножи')
        assert collector.favorites == ['Достать ножи'] and len(collector.favorites) == 1

    def test_delete_book_from_favorites_valid_name_true(self):
        collector = BooksCollector()
        collector.favorites = ['Достать ножи', 'Ведьмак', 'Тошнота', 'Процесс']
        collector.delete_book_from_favorites('Процесс')
        assert collector.favorites == ['Достать ножи', 'Ведьмак', 'Тошнота']

    def test_get_list_of_favorites_books_true(self):
        collector = BooksCollector()
        collector.favorites = ['Достать ножи', 'Ведьмак', 'Тошнота', 'Процесс']
        assert collector.get_list_of_favorites_books() == collector.favorites