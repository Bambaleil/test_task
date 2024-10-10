# Text Replacement Utility

## Описание
Это утилита для замены текста в файлах на основе конфигурационного файла. Программа заменяет значения в текстовом файле, используя пары `ключ=значение` из конфигурационного файла. Результаты сортируются по количеству произведенных замен.

## Установка

1. Клонируйте репозиторий:
    ```sh
    git clone https://github.com/Bambaleil/test_task.git
    ```
   
2. Перейдите в папку проекта:
    ```sh
    cd test_task
    ```

3. Создайте виртуальное окружение и активируйте его:
    ```sh
    python -m venv venv
    source venv/bin/activate   # для Windows используйте venv\Scripts\activate
    ```

4. Установите необходимые зависимости:
    ```sh
    pip install -r requirements.txt
    ```

## Использование

Запуск программы:
```sh
python test.py <config_file> <text_file>
