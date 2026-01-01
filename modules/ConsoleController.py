# Импорт библиотек и зависимостей
import os
from platform import system
from modules.Ptypes import Vector2


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
	def updateBuffer(self) -> None:
		# Очищаем буфер
		self.frameBuffer.clear()
		# Создание списков по y
		for y in range(self.height):
			self.frameBuffer.append([])
			# Создание значений по x
			for _ in range(self.width):
				self.frameBuffer[y].append("")
		
	# Отрисовка кадра в консоли
	def fillFrame(self) -> None:
		self.clear()  # Очищаем консоль
		output_frame = ""
		for y in range(self.height):
			output_frame += "\n"
			for x in range(self.width):
				output_frame += self.frameBuffer[y][x]
		print(output_frame)
	
	# Добавление горизонтальной линии в буфер
	def drawHLine(self, pos:Vector2, lenght:int, symbol:str):
		if len(symbol) == 1:  # Проверка является ли строка символом
			for i in range(lenght):
				self.drawPixel(pos, symbol)
				pos.x += 1
			return self.frameBuffer
		else:
			print("Получена строка а ожидался один символ!")
			
	# Добавление полого квадрата в буфер
	def drawRect(pos:Vector2, size:Vector2, symbol:str):
		pass
	
	# Добавление пикселя в буфер
	def drawPixel(self, position:Vector2, symbol:str) -> None:
		if len(symbol) == 1:  # Проверка является ли строка символом
			try:
				self.frameBuffer[position.y][position.x] = symbol
			except:
				None
		else:
			print("Получена строка а ожидался один символ!")
			
	
	# Очистка терминала
	def clear(self) -> None:
		# Получение имени
		os_name = system()
		if os_name.lower() == "Windows".lower(): #Если это Windows
			os.system("cls")
		else: # Иначе это Linux/MacOS
			os.system("clear") 
