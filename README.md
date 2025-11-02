## Test API Framework

### Особенности асинхронных тестов

Все тесты в фреймворке **асинхронные** (`async def`). Настройка `asyncio_mode = auto` в `pytest.ini` позволяет автоматически запускать асинхронные тесты без необходимости вручную добавлять декоратор `@pytest.mark.asyncio` к каждой функции.

Декоратор `@pytest.mark.asyncio` в коде остается для обратной совместимости, но при включенном `auto` режиме он не обязателен.

### Установка зависимостей

1. Создайте виртуальное окружение (рекомендуется):
```sh
python -m venv venv
source venv/bin/activate  # для Linux/Mac
# или
venv\Scripts\activate  # для Windows
```

2. Установите зависимости:
```sh
pip install -r requirement.txt
```

3. Создайте файл `.env` в корне проекта (используйте `.env.example` как шаблон):
```sh
cp .env.example .env
```

Заполните `.env` своими данными:
- `HOST` - URL вашего API
- `REFRESH_TOKEN` - токен для обновления сессии
- `ACCESS_TOKEN` - токен доступа (будет автоматически обновляться)

### Запуск автотестов

#### Основные команды

**Все тесты Accounts:**
```sh
pytest tests/accounts/
```

**Все тесты Admin Entities:**
```sh
pytest tests/admin_entities/
```

**Все тесты в проекте:**
```sh
pytest tests/
```

#### Примеры запуска (Accounts)

**Smoke Tests (быстрая проверка API):**
```sh
pytest tests/accounts/test_accounts_api.py
```

**Flow Tests (проверка последовательности операций):**
```sh
pytest tests/accounts/test_accounts_flow.py
```

**Negative Tests (проверка обработки ошибок):**
```sh
pytest tests/accounts/test_accounts_negative.py
```

**Все тесты Accounts:**
```sh
pytest tests/accounts/
```

#### Фильтрация тестов по маркерам

**Только Admin Entities тесты:**
```sh
pytest -m adminentities
```

**Только regression тесты:**
```sh
pytest -m regression
```

**Пропустить skipped тесты:**
```sh
pytest tests/ -v
```

#### Запуск с Allure отчетом

**Генерация отчета:**
```sh
pytest tests/ --alluredir=reports/allure
```

**Просмотр отчета:**
```sh
allure serve reports/allure
```

**Генерация статического HTML отчета:**
```sh
allure generate reports/allure -o reports/html --clean
```

#### Дополнительные опции

**Подробный вывод:**
```sh
pytest tests/ -v
```

**Очень подробный вывод:**
```sh
pytest tests/ -vv
```

**Запуск конкретного теста:**
```sh
pytest tests/accounts/test_accounts_api.py::TestAccounts::test_total_amount
```

**Параллельный запуск (требует pytest-xdist):**
```sh
pytest tests/ -n auto
```

**Остановка на первой ошибке:**
```sh
pytest tests/ -x
```

**Повтор провальных тестов (требует pytest-rerunfailures):**
```sh
pytest tests/ --reruns 3
```

### Структура тестов

- `tests/accounts/` - тесты для Accounts API
  - `test_accounts_api.py` - основные API тесты
  - `test_accounts_flow.py` - тесты последовательностей
  - `test_accounts_negative.py` - негативные тесты

- `tests/admin_entities/` - тесты для Admin Entities API
  - `test_admin_entities_api.py` - основные API тесты
  - `test_admin_entities_negative.py` - негативные тесты

### Логи

Логи тестов сохраняются в `reports/test_framework.log`

### Troubleshooting

**Проблема:** тесты не запускаются с ошибкой о pytest-asyncio
**Решение:** убедитесь что установлен pytest-asyncio:
```sh
pip install pytest-asyncio
```

**Проблема:** не находит .env файл
**Решение:** убедитесь что файл `.env` находится в корне проекта

**Проблема:** токены не обновляются
**Решение:** проверьте формат REFRESH_TOKEN в `.env` и доступность API
