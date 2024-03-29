# Задание 1. Приложение заметки (Python)
## Информация о проекте
Необходимо написать проект, содержащий функционал работы с заметками.
Программа должна уметь создавать заметку, сохранять её, читать список
заметок, редактировать заметку, удалять заметку.

## Создание сущности **Note**
```
class Note:
    def __init__(self, id, title, body, date_time):
        self.id = id
        self.title = title
        self.body = body
        self.date_time = date_time
```

## Создание модуля Controller
Данный модуль отвечает за логику приложения. В нем реализованы методы создания, сохранения, чтения, вывода в консоль, поиска и удаления заметок

**Методы создания и сохранения заметок**
```
import csv
from datetime import datetime
from note import Note

class Controller:
    def __init__(self):
        self.notes = []
        
    def write_note(self, title, body):
        id = len(self.notes) + 1
        date_time = datetime.now().strftime('%d.%m.%y %H:%M:%S')
        new_note = Note(id, title, body, date_time)
        self.notes.append(new_note)
        self.save_notes()
        
    def save_notes(self):
        with open('notes.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            for note in self.notes:
                writer.writerow([note.id, note.title, note.body, note.date_time])
            
```
**Методы чтения и вывода в консоль заметок**
```
    def read_all_notes(self):
        return self.notes

    def print_all_notes(self):
        for note in self.notes:
            print(f'ID: {note.id}, Заголовок: {note.title}, Текст: {note.body}, Дата/время: {note.date_time}\n')
```
**Метод поиска заметки по номеру, заголовку и дате создания/изменения**
```
    def search_note(self):
        while True:
            print(
                'Возможные варианты поиска:\n'
                '1. По номеру\n'
                '2. По заголовку\n'
                '3. По дате\n'
                '0. Выход в меню\n'
            )

            index_var = input('\nВыберите вариант поиска: ')
            
            if index_var == '1':
                search = int(input('\nВведите номер ID: '))
                for note in self.notes:
                    if note.id == search:
                        print(f'ID: {note.id}; Заголовок: {note.title}; Текст: {note.body}; Дата/время: {note.date_time}\n')
                        break
                    else:
                        print('\nТакого номера нет\n')
            elif index_var == '2':
                search = input('\nВведите данные для поиска: ').capitalize()
                for note in self.notes:
                    if search in note.title:
                        print(f'ID: {note.id}; Заголовок: {note.title}; Текст: {note.body}; Дата/время: {note.date_time}\n')    
            elif index_var == '3':
                search = input('\nВведите данные для поиска в формате ДД.ММ.ГГ: ')
                for note in self.notes:
                    only_date = note.date_time.split(' ')
                    date_for_search = only_date[0]
                    if search in date_for_search:
                        print(f'ID: {note.id}; Заголовок: {note.title}; Текст: {note.body}; Дата/время: {note.date_time}\n')
            elif index_var == '0': 
                break
            else:
                print('\nТакого номера нет. Попробуйте еще раз.\n')
```
**Методы редактирования и удаления заметки с определенным номером**
```    
    def edit_note(self, id, title=None, body=None):
        for note in self.notes:
            if note.id == id:
                if title:
                    note.title = title
                if body:
                    note.body = body
                note.date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.save_notes()
                print('\nЗаметка изменена.\n')
                break
            else:
                print('\nТакого номера нет.\n')  
                
    def del_note(self, id):
        for note in self.notes:
            if note.id != id:
                self.notes.remove(note)
                self.save_notes()
                print('\nЗаметка удалена.\n')
            else:
                print('\nТакого номера нет.\n')
```
## Создание модуля View
Данный модуль создан для взаимодействия с пользователем и предлагает ему меню для выбора команд с приложением заметки: новая заметка, вывод всех заметок, поиск заметки, редактирование заметки, удаление заметки и завершение работы 
```
from controller import Controller
from note import Note

class View:
    def __init__(self):
        self.controller = Controller()
        
    def run(self):
        with open('notes.csv', 'a'):
            pass
        while True:
            print('Возможные варианты действия:\n'
                '1. Новая заметка\n'
                '2. Вывод всех заметок\n'
                '3. Поиск заметки\n'
                '4. Редактирование заметки\n'
                '5. Удаление заметки\n'
                '0. Завершение работы\n'
            )

            user_input = input('\nВыберите вариант действия: ')
            
            if user_input == '1':
                title = input('\nВведите заголовок заметки: ').capitalize()
                body = input('Введите описание заметки: ').capitalize()
                self.controller.write_note(title, body)
            elif user_input == '2':
                notes = self.controller.read_all_notes()
                if notes:
                    self.controller.print_all_notes()
                else:
                    print('Заметки не найдены.')
            elif user_input == '3':
                self.controller.search_note()
            elif user_input == '4':
                id = int(input('\nВведите номер заметки для редактирования: '))
                title = input('\nВведите новый заголовок: ').capitalize()
                body = input('\nВведите новое описание заметки: ').capitalize()
                self.controller.edit_note(id, title, body)
            elif user_input == '5':
                id = int(input('\nВведите номер заметки, которую нужно удалить: '))
                self.controller.del_note(id)
            elif user_input == '0':
                break
            else:
                print('\nТакого номера нет. Попробуйте еще раз.\n')
```
## Модуль Main для инициации запуска приложения 
```
from view import View

if __name__ == '__main__':
    view = View()
    view.run()
```