# mythos-tests

Репозиторий автотестов на Python: REST API Mythos Sandbox и UI (авторизация Mythos, форма Form Fields на practice-automation.com). Собственного сервера или веб-приложения в проекте нет.

## Описание проекта

Набор pytest-сценариев против внешних стендов. Тесты проверяют API и страницы в браузере, используя HTTP-клиент и Selenium.

Задачи, которые закрывает репозиторий:

- CRUD сущности mythology в Mythos API;
- регистрация пользователя через `POST /api/register`;
- UI-авторизация тестового пользователя Tuco;
- заполнение учебной формы Form Fields и проверка alert об успехе.

### Mythos Sandbox API

Базовый хост: `https://api.qasandbox.ru` (`storage/urls.py`, класс `MythosUrls`).

| Метод | Путь | Клиентская функция | Тесты |
| --- | --- | --- | --- |
| `POST` | `/api/register` | `register_user` | `tests/rest/mythos/auth/post_api_register_test.py` |
| `POST` | `/api/login` | `get_entities_auth_headers` | вызывается из фикстуры `auth_user_tuco` и части тестов напрямую |
| `POST` | `/api/mythology` | `create_mythology` | `post_mythology_test.py` |
| `GET` | `/api/mythology` | `get_all_mythology` | `get_mythology_test.py` (список, фильтр `category`, сортировка `sort`) |
| `GET` | `/api/mythology/{id}` | `get_mythology_by_id` | `get_mythology_id_test.py` |
| `PUT` | `/api/mythology/{id}` | `fully_update_mythology_by_id` | `put_mythology_id.py` |
| `PATCH` | `/api/mythology/{id}` | `partial_update_mythology_by_id` | `patch_mythology_id.py` |
| `DELETE` | `/api/mythology/{id}` | `delete_mythology_by_id` | `delete_mythology_by_id_test.py` |

В фильтрах списка используются категории `gods`, `heroes`, `creatures`. Сортировка: `sort=asc` или `sort=desc`, проверка порядка по полю `name`.

Поля сущности по умолчанию в `create_mythology` и `fully_update_mythology_by_id`: `name="Посейдон"`, `category="gods"`, `desc="Бог морей"`, `img="https://images.com/"`.

### UI

- Mythos: Page Object `Auth` (`clients/web/mythos_sandbox/auth.py`), тест `tests/web/mythos/auth_test.py`.
- Form Fields: `https://practice-automation.com/form-fields`, Page Object `FormFields`, тесты `tests/web/automate_now/form_field_test.py`. Успешная отправка формы проверяется текстом alert: `Message received!`.

Ссылки на кейсы Qase из декораторов `@allure.testcase`: [MSA-22](https://app.qase.io/case/MSA-22), [AN-12](https://app.qase.io/case/AN-12), [AN-15](https://app.qase.io/case/AN-15), [AN-16](https://app.qase.io/case/AN-16), [AN-17](https://app.qase.io/case/AN-17).

## Технологический стек

Зависимости зафиксированы в `requirements.txt`.

| Назначение | Пакеты / инструменты |
| --- | --- |
| Язык | Python |
| Запуск тестов | pytest `9.0.3` |
| HTTP | requests `2.34.2`, curlify `3.0.0` |
| UI | selenium `4.45.0`, webdriver-manager `4.1.2` (ChromeDriver) |
| Отчётность | allure-pytest `2.16.0`, allure-python-commons `2.16.0` |
| Переменные окружения | python-dotenv `1.2.2` (`load_dotenv` в `storage/credentials.py`) |

База данных не используется. В репозитории нет `Dockerfile`, `docker-compose`, `pyproject.toml`, `package.json` и файлов CI.

## Структура проекта

```text
mythos-tests/
├── clients/
│   ├── data_generator.py              # get_random_string (letters / digits / lowercase)
│   ├── rest/
│   │   ├── base_http.py               # send_request: requests + вложения Allure
│   │   ├── base_auth.py               # POST /api/login → заголовок Bearer
│   │   ├── base_validation.py         # check_response_code, check_value_in_dicts, check_dicts_are_sorted_by_key
│   │   └── mythos_sandbox/
│   │       └── entities.py            # методы register и mythology
│   └── web/
│       ├── base_page.py               # общие действия Selenium
│       ├── mythos_sandbox/auth.py     # локаторы и шаги авторизации
│       └── automate_now/form_fields.py
├── storage/
│   ├── urls.py                        # MythosUrls, AutomateNow
│   └── credentials.py                 # UserTuco из TUCO_* env
├── tests/
│   ├── rest/mythos/auth/post_api_register_test.py
│   ├── rest/mythos/entities/
│   │   ├── post_mythology_test.py
│   │   ├── get_mythology_test.py
│   │   ├── get_mythology_id_test.py
│   │   ├── put_mythology_id.py
│   │   ├── patch_mythology_id.py
│   │   └── delete_mythology_by_id_test.py
│   └── web/
│       ├── mythos/auth_test.py
│       └── automate_now/form_field_test.py
├── conftest.py                        # фикстуры browser, auth_user_tuco, mythology_id_by_user_tuco
├── pytest.ini                         # маркеры pytest
├── requirements.txt
├── .gitignore
└── README.md
```

В `.gitignore`: `allure-results/`, `__pycache__/`, `.pytest_cache/`, `.env`, `/venv/`, `.idea/`.

## Требования

Версия Python и системные требования в проекте **не указаны**. Из кода и зависимостей следует:

- Python и pip;
- пакеты из `requirements.txt`;
- Google Chrome для UI: фикстура `browser` создаёт `webdriver.Chrome` через `ChromeDriverManager().install()`;
- сеть до `https://api.qasandbox.ru` и `https://practice-automation.com`;
- для сценариев с логином Tuco — переменные `TUCO_USER_NAME` и `TUCO_PASSWORD`.

## Установка и настройка

### Клонирование

Remote `origin`: `https://github.com/sasha99996/mythos-tests.git`.

```bash
git clone https://github.com/sasha99996/mythos-tests.git
cd mythos-tests
```

### Зависимости

В `.gitignore` указан каталог `venv/`:

```bash
python -m venv venv
```

Активация:

```bash
venv\Scripts\activate
```

```powershell
venv\Scripts\Activate.ps1
```

```bash
source venv/bin/activate
```

```bash
pip install -r requirements.txt
```

### Переменные окружения

Файла `.env.example` нет. `storage/credentials.py` вызывает `load_dotenv()` и читает `TUCO_USER_NAME`, `TUCO_PASSWORD`. В комментарии к файлу указано, что данные лежат в переменных CI-сборки или в локальном env-файле.

Создайте `.env` в корне (файл не коммитится):

```env
TUCO_USER_NAME=your_username
TUCO_PASSWORD=your_password
```

Подставьте свои значения. Реальные пароли и логины в README не публикуются.

## Запуск проекта

Отдельных сервисов поднимать не нужно. Точка входа — pytest из корня репозитория.

```bash
pytest
```

```bash
pytest tests/rest
pytest tests/web
```

Маркеры из `pytest.ini`:

```bash
pytest -m post_register
pytest -m post_mythology
pytest -m get_all_mythology
pytest -m get_mythology_id
pytest -m put_mythology
pytest -m patch_mythology
pytest -m delete_mythology_id
pytest -m UI_auth
pytest -m automate_now_form_fields
```

В `pytest.ini` нет `addopts` и настроек Allure. Плагин `allure-pytest` подключается как зависимость; каталог `allure-results/` игнорируется git. Команда Allure CLI для HTML-отчёта в репозитории не задана.

## Использование

### Фикстуры (`conftest.py`)

| Фикстура | Назначение |
| --- | --- |
| `browser` | Chrome, сразу открывает `AutomateNow.FORM_FIELDS_URL`, после теста `quit()` |
| `auth_user_tuco` | заголовки `Authorization: Bearer …` после логина Tuco |
| `mythology_id_by_user_tuco` | создаёт mythology, отдаёт `id`, в teardown удаляет сущность |

### Регистрация

`register_user(username, password)` → `POST /api/register`. В тесте логин и пароль строятся через `get_random_string(size=6, string_type="letters")`. Ожидаемый код: `201`.

### Mythology API

Авторизованные вызовы передают результат `get_entities_auth_headers()` / фикстуру `auth_user_tuco`. Ожидаемые коды из тестов:

| Сценарий | Код |
| --- | --- |
| создание | `201` |
| список, GET по ID, PUT/PATCH успех | `200` |
| удаление | `204` |
| GET после удаления | `404` |
| PATCH или DELETE без авторизации (`auth=None`) | `401` |
| GET с буквенным ID | `400` |

`test_get_mythology_with_long_id` пропущен (`@pytest.mark.skip`): в причине указано, что при ID из 50 цифр API отвечает `500`.

### Form Fields

Методы `FormFields`: `fill_in_name_field`, `fill_in_password_field`, `choose_favorite_drink`, `choose_favorite_color`, `choose_automation_answer`, `fill_in_email`, `fill_in_message`, `click_btn_submit`, `get_success_message`.

Параметры в тестах:

- automation: `Yes`, `No`, `Undecided`;
- напиток: `Milk`, `Water`, `Coffee`;
- цвет: `Red`, `Blue`, `Yellow`, `Green`, `#FFC0CB`.

Значения по умолчанию в Page Object: имя `Ivan`, пароль `test123`, email `ivan@gmail.com`, сообщение `ыыы ааа`.

### UI Mythos

Шаги теста `test_auth_by_user`: кнопка «Войти» в шапке → логин/пароль Tuco → кнопка входа на виджете → видимость кнопки выхода (`LOG_OUT_BTN`).

## Тестирование

Проект состоит из автотестов. Команды запуска — в разделе «Запуск проекта».

Дополнительно (стандартные флаги pytest, в конфиге проекта не прописаны):

```bash
pytest -v
pytest -k "test_create_mythology"
pytest tests/rest/mythos/entities/get_mythology_test.py
```

Линтеры, форматтеры, tox и Makefile в репозитории не настроены. Пакет `black` в `requirements.txt` отсутствует.

## Конфигурация

### URL (`storage/urls.py`)

| Константа | Значение |
| --- | --- |
| `MythosUrls.BASE_URL` | `https://api.qasandbox.ru` |
| `MythosUrls.MYTHOLOGE_URL` | `https://api.qasandbox.ru/api/mythology` |
| `MythosUrls.LOGIN_URL` | `https://api.qasandbox.ru/api/login` |
| `MythosUrls.REGISTER_URL` | `https://api.qasandbox.ru/api/register` |
| `AutomateNow.BASE_URL` | `https://practice-automation.com` |
| `AutomateNow.FORM_FIELDS_URL` | `https://practice-automation.com/form-fields` |

Имя константы `MYTHOLOGE_URL` в коде записано именно так.

### HTTP (`clients/rest/base_http.py`)

`requests.request(..., verify=False, timeout=120)`. В Allure: curl запроса (если тело не `bytes`), код ответа, тело ответа как JSON.

Логин: `POST` на `LOGIN_URL` с `Content-Type: application/json` и телом `UserTuco.CREDS`; из JSON берётся поле `token`.

### Переменные окружения

| Имя | Назначение | Пример формата |
| --- | --- | --- |
| `TUCO_USER_NAME` | логин Tuco | строка логина |
| `TUCO_PASSWORD` | пароль Tuco | строка пароля |

Других `os.getenv` / `os.environ` в исходниках нет.

### Маркеры (`pytest.ini`)

| Маркер | Описание в pytest.ini |
| --- | --- |
| `put_mythology` | полное обновление mythology |
| `patch_mythology` | частичное обновление mythology |
| `get_mythology_id` | получение mythology по ID |
| `get_all_mythology` | список mythology |
| `delete_mythology_id` | удаление mythology по ID |
| `post_mythology` | создание mythology |
| `post_register` | регистрация |
| `UI_auth` | UI-авторизация Mythos |
| `automate_now_form_fields` | автотесты Form Fields |

Маркер `patch_mythology` в коде стоит только на `test_patch_mythology_with_auth`. Функция `test_patch_mythology_without_auth` этого маркера не имеет.

## Дополнительная информация

- Учётные данные не зашиты в код: класс `UserTuco` читает окружение.
- TLS при HTTP-запросах не проверяется (`verify=False`).
- В `requirements.txt` есть и `dotenv==0.9.9`, и `python-dotenv==1.2.2`; импорт в коде: `from dotenv import load_dotenv`.
- Фикстура `browser` всегда открывает Form Fields. UI-тест авторизации Mythos (`tests/web/mythos/auth_test.py`) эту фикстуру использует — отдельного URL Mythos UI в `storage/urls.py` нет.
- Документации по версии Python, CI и сборке Allure-отчёта в репозитории нет.
