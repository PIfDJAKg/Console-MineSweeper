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
        self.CControl: CCtrl.Controller = CCtrl.Controller()  
        # Размер экрана
        self.display_size: Vector2 = Vector2(10, 10)
        # Размер игрового поля, отнимаем 2 потому-что столько занимает рамка
        self.game_size: Vector2 = Vector2(self.display_size.x - 2, self.display_size.y - 2)
        self.mines_count = 12

        self.CControl.setResolution(self.display_size)
        self.CControl.updateBuffer()

        self.mines_list: list = [] # Положения мин    

    def create_lists(self) -> None:
        for y in range(self.game_size.y):
            self.mines_list.append([])
            for x in range(self.game_size.x):
                self.mines_list[y].append("")

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

            # Увеличиваем на 1 потому-что 1 пиксель с обеих сторон занимает рамка
            position_on_field = mine_position.add(Vector2(1, 1))
            
            self.mines_list[mine_position.x][mine_position.y] = True
            self.CControl.drawPixel(position_on_field, "@")

    # Отрисовка рамки игры
    def draw_frame(self) -> None:
        """
        Docstring for draw_frame
        
        Отрисовка границ поля
        """

        # Отрисовываем точки
        self.CControl.drawPixel(Vector2(0, 0), "+")
        self.CControl.drawPixel(Vector2(self.display_size.x - 1, 0), "+")
        self.CControl.drawPixel(Vector2(0, self.display_size.x - 1), "+")
        self.CControl.drawPixel(Vector2(self.display_size.y - 1, self.display_size.y - 1), "+")

        # Отрисовка чисел
        numeration = "".join(str(i) for i in range(self.game_size.x))
        self.CControl.drawHText(Vector2(1, 0), numeration)
        self.CControl.drawHText(Vector2(1, self.display_size.y - 1), numeration)

        # Отрисовка букв
        text_numeration = "".join(ascii_uppercase[i] for i in range(self.game_size.y))
        self.CControl.drawVText(Vector2(0, 1), text_numeration)
        self.CControl.drawVText(Vector2(self.display_size.x -1, 1), text_numeration)

        self.CControl.drawFRect(Vector2(1, 1), self.game_size.copy(), " ")

    def main(self):
        self.draw_frame() # отрисовываем рамку
        self.create_lists()
        self.generate_mines(self.mines_count)
        self.CControl.fillFrame()


if __name__ == "__main__":
    game = Game()
    game.main()