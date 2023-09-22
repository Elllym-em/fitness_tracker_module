# Модуль фитнес-трекера
Модуль фитнес-трекера, который обрабатывает данные для трёх видов тренировок: бега, спортивной ходьбы и плавания.

Выполняет следующие функции:
- принимает от блока датчиков информацию о прошедшей тренировке;
- определяет вид тренировки;
- рассчитывает результаты тренировки;
- выводит информационное сообщение о результатах тренировки.
  
Информационное сообщение включает следующие данные:
- тип тренировки (бег, ходьба или плавание);
- длительность тренировки;
- дистанция, которую преодолел пользователь, в километрах;
- среднюю скорость на дистанции, в км/ч;
- расход энергии, в килокалориях.

## Стек технологий:
- Python 3.9
- ООП

### Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:
```
git clone git@github.com:Elllym-em/fitness_tracker_module.git
```
```
cd fitness_tracker_module
```
Cоздать и активировать виртуальное окружение:
```
python3 -m venv env
```
* Если у вас Linux/macOS
    ```
    source env/bin/activate
    ```
* Если у вас windows
    ```
    source env/scripts/activate
    ```
Установить зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```
Запустить файл:
```
python3 homework.py
```

**Автор:**
[Elina Mustafaeva](https://github.com/Elllym-em)

