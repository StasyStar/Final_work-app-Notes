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
                    
    