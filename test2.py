import pytest
from main2 import count_vowels

def test_only_vowels():
    """Проверка строки, содержащей только гласные."""
    assert count_vowels("aeiouAEIOU") == 10

def test_no_vowels():
    """Проверка строки, не содержащей гласных."""
    assert count_vowels("bcdfghjklmnpqrstvwxyz") == 0

def test_mixed_string():
    """Проверка строки, содержащей как гласные, так и согласные."""
    assert count_vowels("Hello World") == 3
    assert count_vowels("Python Programming") == 4

def test_empty_string():
    """Проверка пустой строки."""
    assert count_vowels("") == 0

def test_vowels_with_special_characters():
    """Проверка строки с гласными и специальными символами."""
    assert count_vowels("!@# $% aeiou 123") == 5

# Запуск тестов
if __name__ == "__main__":
    pytest.main()
