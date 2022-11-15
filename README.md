# Downloading_images_API
Данная программа предназначена для публикации различных снимков в Telegram, как находящихся у пользователя, так и посредством скачивания их на компьютер пользователя. Скачивание изображений организовано несколькими способами:
1. По URL изображения;
2. При помощи API Nasa;
3. С сайта SpaceX.

Пользователь имеет возможность запуска отдельных частей программы, что дает возможность её применения для решения различных задач: 
* скачивание отдельных картинок по URL;
* скачивание фотографий запуска шаттла;
* скачивание набора изображений космоса;
* скачивание набора фотографий Земли.

## Модули:
### dload_spacex_launch_img

Данный модуль производит загрузку изображений посредством использования API SpaceX. У пользователя есть возможность скачать изображения какого-либо конкретного запуска, либо по умолчанию последнего.

### dload_nasa_img

Данный модуль производит загрузку изображений космоса посредством использования NASA API.

### dload_Epic_img_from_nasa

Данный модуль производит загрузку набора изображений Земли с периодичностью в несколько часов. 

## Как установить:

Для полного функционирования скрипта понадобится два ключа. Они хранятся в файле .env в следующем виде:

```python
API_KEY="Ваш ключ"
TG_API_KEY="Ваш ключ"
```
Для получения ключей необходимо:
* в директории с файлами к программе создать файл .env;
* `API_KEY` необходимо получить пройдя регистрацию на сайте [NASA](https://api.nasa.gov/?Generate%20API%20Key);
* `TG_API_KEY` может быть получен при регистрации бота (инструкцию по запуску бота можно найти по [ссылке])(https://way23.ru/%D1%80%D0%B5%D0%B3%D0%B8%D1%81%D1%82%D1%80%D0%B0%D1%86%D0%B8%D1%8F-%D0%B1%D0%BE%D1%82%D0%B0-%D0%B2-telegram.html)
* полученные токены необходимо ввести в файл .env.

При корректном выполнении описанных выше шагов, скрипт считает токен и запустится. Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей:

```
pip install -r requirements.txt
```

## Как запустить

Скрип, обеспечивающий скачивание изображений, запускается через командную строку командой:
```
python "Полное название скрипта"
```

Также при запуске используются аргументы:
* `-f` - id запуска шаттла, для работы со скриптом `dload_spacex_launch_img.py`. По умолчанию скрип будет скачивать фотографии последнего запуска шаттла
* `-d` - название директории, куда будут скачиваться изображения. Папки будут находиться в одной директории с файлами программы. По умолчанию, название директории "Images"

Бот, обеспечивающий публикацию изображений в Telegram-канал запускается через командную строку командой:
```
python telegram_bot.py
```
Данный скрипт также обладает несколькими аргументами:
* -iq - количество изображений, которое необходимо опубликовать;
* -st - периодичность публикации (в часах). По умолчанию стоит раз в 10 часов
* -d - директория, в которой находятся файлы, готовые к публикации. По умолчанию, скрипт будет их искать в папке "Images"

## Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [devman](https://devman.org/)



