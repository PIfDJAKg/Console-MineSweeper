# Новые типы пиджака для его библиотек и игр

# Вектор с двумя осями
class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def copy(self): 
        return Vector2(self.x, self.y)
    
    def add(self, vec2):
        return Vector2(self.x + vec2.x, self.y + vec2.y)
    
    def subtract(self, vec2):
        return Vector2(self.x - vec2.x, self.y - vec2.y)
