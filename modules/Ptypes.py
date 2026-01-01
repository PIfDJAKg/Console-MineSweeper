# Новые типы пиджака для его библиотек и игр

# Вектор с двумя осями
class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def copy(self): 
        return Vector2(self.x, self.y)