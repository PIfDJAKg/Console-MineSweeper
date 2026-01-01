# Импорт библиотек и зависимостей
import os
from platform import system


# Класс вектора с двумя осями
class Vector2:
	def __init__(self, x, y) -> None:
		self.x = x  # Координата x
		self.y = y  # Координата y


# Класс контроллера консоли
class Controller:
	def __init__(self) -> None:
		self.width = 12  # Ширина поля
		self.height = 12  # Высота поля
		self.frameBuffer = []  # Буффер кадра
	
	# Установка размера поля
	def setResolution(self, resolution:Vector2) -> None:
		self.width = resolution.x  # Устанавливаем ширину
		self.height = resolution.y  # Устанавливаем высоту
	
	# Обновление размера поля
	def updateResolution(self) -> None:
		# Очищаем буфер
		self.frameBuffer.clear()
		# Создание списков по y
		for y in range(self.height):
			self.frameBuffer.append([])
			# Создание значений по x
			for _ in range(self.width):
				self.frameBuffer[y].append("")
		print(self.frameBuffer)
		
		
	
	# Добавление пикселя в буфер
	def drawPixel(self, position:Vector2, symbol:str) -> None:
		if len(symbol) == 1:  # Проверка является ли строка символом
			try:
				self.frameBuffer[position.y][position.x] = symbol
			except:
				print("Неудалось добавить символ в буфер кадра!")
		else:
			print("Получена строка а ожидался один символ!")
			
	
	# Очистка терминала
	def clear(self) -> None:
		# Получение имени
		os_name = system()
		if os_name == lower("Windows"): #Если это Windows
			os.system("cls")
		else: # Иначе это Linux/MacOS
			os.system("clear") 
