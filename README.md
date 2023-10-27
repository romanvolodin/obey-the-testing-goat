# Python TDD

Учебный проект по книге ["Test-Driven Development with Python"](https://www.obeythetestinggoat.com/).

## Требования

Для запуска вам понадобится:

- Python 3.8 или выше
- Веб-драйвер для вашего браузера. Скачать можно [на этой странице](https://pypi.org/project/selenium/) в разделе Drivers.

Скачанный веб-драйвер (в моём случает это **geckodriver** для **Firefox**) скопируйте в корень проекта. Либо в `~/.local/bin`.

## Переменные окружения

Настройки берутся из переменных окружения. Чтобы их определить, создайте файл `.env` в корне проекта и запишите туда данные в таком формате: `ПЕРЕМЕННАЯ=значение`.

Доступные переменные:

- `SECRET_KEY` — обязательный секретный ключ Django. Это соль для генерации хэшей. Значение может быть любым, важно лишь, чтобы оно не было известно посторонним. [Документация Django](https://docs.djangoproject.com/en/4.2/ref/settings/#secret-key).
- `DEBUG` — настройка Django для включения отладочного режима. Принимает значения `true` или `false`, по-умолчанию `false`. [Документация Django](https://docs.djangoproject.com/en/4.2/ref/settings/#std:setting-DEBUG).
- `ALLOWED_HOSTS` — настройка Django со списком разрешённых адресов. Если запрос прилетит на другой адрес, то сайт ответит ошибкой 400. Можно перечислить несколько адресов через запятую, например `127.0.0.1,192.168.0.1,site.test`. [Документация Django](https://docs.djangoproject.com/en/4.2/ref/settings/#allowed-hosts).

Пример:

```env
SECRET_KEY="mkl.so84hf;woj3r-0iqe4wt"
DEBUG=true
ALLOWED_HOSTS="localhost,127.0.0.1"
```
