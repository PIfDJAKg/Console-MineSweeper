"""Прошу прощения за мой говнокод, если вы знаете как код можно улучшить
Пожалуйста сделайте отдельную ветку репозитория и улучшите его, или напишите мне
email: antonovskijila6@gmail.com
Большое спасибо"""

# Импорт библиотек и зависимостфей
import modules.ConsoleController as CCtrl
from modules.Ptypes import Vector2
from string import ascii_uppercase
from random import randint

class Game:
    def __init__(self):
        # Создание контроллера
        self.controller: CCtrl.Controller = CCtrl.Controller()  
        # Размер экрана
        self.display_size: Vector2 = Vector2(14, 14)
        # Размер игрового поля, отнимаем 4 потому-что столько занимает рамка
        self.game_size: Vector2 = self.display_size.subtract(Vector2(4, 4))
        self.mines_count = 12

        self.errors_codes = {
            0 : "Invalid",
            1 : "Invalid input",
            2 : "Input out of range",
            3 : "Empty entered data",
            4 : "Invalid data type"
        }

        self.controller.setResolution(self.display_size)
        self.controller.updateBuffer()

        self.mines_list: list = []  # Положения мин
        self.numbers_list: list = []  # Чисела на поле
        self.flags_list: list = []  # Флажки на поле

    # Создание внутренностей списков
    def create_lists(self) -> None:
        for y in range(self.game_size.y):
            self.mines_list.append([])
            self.numbers_list.append([])
            self.flags_list.append([])
            for x in range(self.game_size.x):
                self.mines_list[y].append("")
                self.numbers_list[y].append(None)
                self.flags_list[y].append(None)

    # Случайный вектор
    def random_vector2(self, min:Vector2, max:Vector2) -> Vector2:
        x = randint(min.x, max.x)
        y = randint(min.y, max.y)
        return Vector2(x, y)

    # Генерация мин
    def generate_mines(self, count:int) -> None:
        for i in range(count):
            # Уменьшаем на 1 потому-что в списке рассчет начинается не с 1 а с 0
            max_vector = self.game_size.subtract(Vector2(1, 1))
            mine_position = self.random_vector2(Vector2(0, 0), max_vector)
            while self.mines_list[mine_position.x][mine_position.y] == True:
                mine_position = self.random_vector2(Vector2(0, 0), max_vector)
            
            self.mines_list[mine_position.x][mine_position.y] = True

    # Генерация чисел
    def generate_numbers(self) -> None:
        for y in range(self.game_size.y):
            for x in range(self.game_size.x):
                if self.mines_list[y][x]:
                    continue
                
                count = 0
                
                # Проверяем клетки по кругу
                for dy in (-1, 0, 1):
                    for dx in (-1, 0, 1):
                        nx = x + dx
                        ny = y + dy
                        
                        # Пропускаем клетку если это базавая клетка
                        if nx == x and ny == y:
                            continue
                        
                        if 0 <= nx < self.game_size.x and 0 <= ny < self.game_size.y:
                            if self.mines_list[ny][nx]:
                                count += 1
                if count > 0:
                    self.numbers_list[y][x] = count
                
    # Отрисовка рамки игры
    def draw_frame(self) -> None:
        """
        Docstring for draw_frame

        Функция draw_frame отрисовывает
        красивую рамку по караям экрана
        """

        # Отрисовываем точки
        self.controller.drawPixel(Vector2(0, 0), "+")
        self.controller.drawPixel(Vector2(self.display_size.x - 1, 0), "+")
        self.controller.drawPixel(Vector2(0, self.display_size.x - 1), "+")
        self.controller.drawPixel(Vector2(self.display_size.y - 1, self.display_size.y - 1), "+")

        # Пробелы между точками и нумерацией
        self.controller.drawHLine(Vector2(0, 1), self.display_size.x, " ")
        self.controller.drawVLine(Vector2(1, 0), self.display_size.y, " ")

        self.controller.drawHLine(Vector2(0, self.display_size.x - 2), self.display_size.x, " ")
        self.controller.drawVLine(Vector2(self.display_size.y - 2, 0), self.display_size.y, " ")

        # Отрисовка чисел
        numeration = "".join(str(i) for i in range(self.game_size.x))
        self.controller.drawHText(Vector2(2, 0), numeration)
        self.controller.drawHText(Vector2(2, self.display_size.y - 1), numeration)

        # Отрисовка букв
        text_numeration = "".join(ascii_uppercase[i] for i in range(self.game_size.y))
        self.controller.drawVText(Vector2(0, 2), text_numeration)
        self.controller.drawVText(Vector2(self.display_size.x -1, 2), text_numeration)

        
        self.controller.drawFRect(Vector2(2, 2), self.game_size.copy(), ".")

    # Рендер поля
    def grid_render(self) -> None:
        """
        Docstring for grid_render
        
        Функция отрисовывает поле на экране игрока
        """

        grid_offset = Vector2(2, 2)
        for y in range(self.game_size.y):
            for x in range(self.game_size.x):
                position_on_grid = Vector2(x, y).add(grid_offset)
                if self.mines_list[y][x]:
                    self.controller.drawPixel(position_on_grid, "@")
                elif self.numbers_list[y][x] != None:
                    self.controller.drawPixel(position_on_grid, str(self.numbers_list[y][x]))

    # Получение ввода клетки
    def get_cell(self, invalid:bool = False, error_code:int = 0) -> Vector2:
        """
        Docstring for get_cell
        
        :param invalid: Говорит нужно ли показать игроку ошибку
        :type invalid: bool

        :param error_code: Код ошибки
        :type error_code: int

        :return: Возвращает позицию клетки как Vector2(x, y)
        :rtype: str
        """

        # Вывод ошибки
        if invalid:
            self.controller.fillFrame()
            print("")
            print(f"{self.errors_codes[error_code]}! Enter again, exemple: A1")
        else:
            print("")
        
        cell = input("Ender cell >> ").lower()


        
        # Получаем букву и число
        try:
            letter = cell[0]
            number = cell[1::1]
        except:
            return self.get_cell(invalid=True, error_code=3)
        
        # Получаем позицию буквы в алфавите
        if letter:
            letter_in_alphabet = ord(letter) - ord("a")

        # Проверяем правильно ли игрок ввел данные
        if not letter.isalpha() or not number.isdigit():
            return self.get_cell(invalid=True, error_code=1)
        elif int(number) >= self.game_size.x or letter_in_alphabet >= self.game_size.y:
            return self.get_cell(invalid=True, error_code=2)
        elif cell == "":
            return self.get_cell(invalid=True, error_code=3)

        return Vector2(number, letter_in_alphabet)
    
    def get_step(self, invalid:bool = False, error_code:int = 0) -> int:
        """
        Docstring for get_step
        
        :param invalid: Говорит нужно ли показать игроку ошибку
        :type invalid: bool

        :param error_code: Код ошибки
        :type error_code: int

        :return: Возвращает индекс хода (1, 2 или 3)
        :rtype: int
        """

        if invalid:
            self.controller.fillFrame()
            print("")
            print(f"{self.errors_codes[error_code]}! Write again, examble: 2")
        else:
            print("")

        print("1 - open; 2 - put/remote flag, 3 - cancel")
        step = input("Enter step >> ")
        
        if step == "":
            return self.get_step(invalid=True, error_code=3)
        elif not step.isdigit():
            return self.get_step(invalid=True, error_code=4)
        elif len(step) != 1:
            return self.get_step(invalid=True, error_code=2)
        elif step not in ("1", "2", "3"):
            return self.get_step(invalid=True, error_code=1)
        else:
            return int(step)

    # Открыть клетку
    def open_cell(self, pos: Vector2):
        pass
    
    # Поставить флаг на клетку
    def use_flag(self, pos: Vector2) -> None:
        if self.flags_list[pos.y][pos.x]:
            self.flags_list[pos.y][pos.x] = None
        else:
            self.flags_list[pos.y][pos.x] = True

    # Получаем ход игрока
    def get_move(self) -> None:
        cell = self.get_cell()
        self.controller.fillFrame()
        step = self.get_step()

        match step:
            case 1:
                pass
            case 2:
                self.use_flag(cell)

    def main(self):
        self.draw_frame()  # отрисовываем рамку
        self.create_lists()  # Создаем списки
        self.generate_mines(self.mines_count)  # Генерируем мины
        self.generate_numbers()  # Генерируем числа
        self.grid_render()  # Рендерим поле
        self.controller.fillFrame() # Отрисовываем кадр
        self.get_move()
        


if __name__ == "__main__":
    game = Game()
    game.main()