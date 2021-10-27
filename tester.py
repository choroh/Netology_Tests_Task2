"""
Netology. Тестирование. Задание 2.
Задача №2 Автотест API Яндекса

Проверим правильность работы Яндекс.Диск REST API. Написать тесты, проверяющий создание папки на Диске.
Используя библиотеку requests напишите unit-test на верный ответ и возможные отрицательные тесты на ответы с ошибкой

Пример положительных тестов:

    Код ответа соответствует 200.
    Результат создания папки - папка появилась в списке файлов.
"""

import unittest

import create_folder
from create_folder import YaUploader

token = create_folder.outh()
uploader = YaUploader(token, 'MyFolder')


class TestAPI(unittest.TestCase):
    def test_create_folder(self):
        self.assertEqual(uploader.create_folder(), "Папка MyFolder успешно создана")

    def test_create_folder_exist(self):
        self.assertEqual(uploader.create_folder(), "Папка с таким именем уже существует")


if __name__ == '__main__':
    unittest.main()
