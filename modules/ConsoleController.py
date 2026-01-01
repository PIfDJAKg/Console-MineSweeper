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
				self.frameBuffer[y].append(".")
		
	# Отрисовка кадра в консоли
	def fillFrame(self) -> None:
		self.clear()  # Очищаем консоль
		output_frame = ""
		for y in range(self.height):
			output_frame += "\n"
			for x in range(self.width):
				output_frame += " " + self.frameBuffer[y][x]
		print(output_frame)
	
	# Добавление горизонтальной линии в буфер
	def drawHLine(self, pos:Vector2, lenght:int, symbol:str):
		# Проверяем символ, что бы он не являлся строкой
		if len(symbol) != 1:
			print("Получена строка а ожидался один символ!")
		elif lenght == 0:
			print("Длинна не может равняться нулю!")
		else:
			# Вычисляем шаг
			step = 1 if lenght >= 0 else -1
			# Получаем модуль длинны
			abs_lenght = abs(lenght)
			for _ in range(abs_lenght):
				self.drawPixel(pos.copy(), symbol)  # Рисуем пиксель
				pos.x += step  # Добавляем шаг к позиции


	# Добавление горизонтальной линии в буфер
	def drawVLine(self, pos:Vector2, lenght:int, symbol:str) -> None:
		# Проверяем символ, что бы он не являлся строкой
		if len(symbol) != 1:
			print("Получена строка а ожидался один символ!")
		elif lenght == 0:
			print("Длинна не может равняться нулю!")
		else:
			# Вычисляем шаг
			step = 1 if lenght >= 0 else -1
			# Получаем модуль длинны
			abs_lenght = abs(lenght)
			for _ in range(abs_lenght):
				self.drawPixel(pos.copy(), symbol)
				pos.y += step
			
	# Добавление полого квадрата в буфер
	def drawRect(self, pos:Vector2, size:Vector2, symbol:str) -> None:
		if len(symbol) == 1:
			self.drawHLine(pos.copy(), size.x, symbol)  # Отрисовка верхней границы,
			self.drawVLine(pos.copy(), size.y, symbol)  # Отрисовка левой границы,
			pos.x += size.x - 1
			pos.y += size.y - 1
			self.drawHLine(pos.copy(), -size.x, symbol)  # Отрисовка нижней границы,
			self.drawVLine(pos.copy(), -size.y, symbol)  # Отрисовка правой границы,
		else:
			print("Получена строка а ожидался один символ!")
	
	# Добавление заполненного квадрата в буфер
	def drawFRect(self, pos:Vector2, size:Vector2, symbol:str) -> None:
		if len(symbol) != 1:
			print("Получена строка а ожидался один символ!")
		else:
			for _ in range(size.y):
				self.drawHLine(pos.copy(), size.x, symbol)  # Отрисовка линии
				pos.y += 1  # Смещение курсора на пиксель вниз

	# Добавление пикселя в буфер
	def drawPixel(self, position:Vector2, symbol:str) -> None:
		if len(symbol) == 1:  # Проверка является ли строка символом
			try:
				# Присваиваем пикселю в буфере значение символа 
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
