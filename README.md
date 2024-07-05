## Перевод числовой записи суммы в рублях в словесную.
 Данный сервис создан для перевода числа в словестную запись
 Пример:
 С клавиатуры вводится сумма. Вывести словесную запись суммы 106,77  = сто шесть рублей 77 копеек

## Настройка

#### Настройка происходит в файле .env его нет в репозитории, т.к. он конфиденциален, но я предоставил файл .env.dist создайте на его основе файл .env и проведите все необходимые настройки.

## Установка зависимостей

#### В основе проекта лежит пакетный менеджер poetry.

`poetry install` - Вариант с использованием poetry.

`pip install -r requirements.txt` - Вариант с использованием pip.


## Документация по make командам

`make help` - Команда help отображает список доступных команд и их описание.

`make ref` - Команда ref используется для форматирования кода с помощью ruff и black.

`make dev` - Команда dev запускает приложение в режиме разработки.

`make req` - Команда req обновляет зависимости в [requirements.txt](requirements.txt)

`make migrate` - Команда migrate применяет все ожидающие миграции к базе данных с помощью alembic.

`make generate` - Команда generate используется для генерации новой миграции базы данных с помощью alembic.

## Запуск
```fastapi dev app``` - Для запуска в режиме отладки
```fastapi run app``` - Для запуска в режиме production
```docker-compose up --build``` - Для запуска через Docker контейнер
