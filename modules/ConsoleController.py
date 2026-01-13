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
		"""
		setResolution() -> Выставляет разрешение консольного экрана
		
		:param resolution: Разрешение консольного экрана Ширина/Высота
		:type resolution: Vector2
		"""

		self.width = resolution.x  # Устанавливаем ширину
		self.height = resolution.y  # Устанавливаем высоту
		
	# Обновление размера буфера
	def updateBuffer(self) -> None:
		"""
		updateBuffer() -> Обновляеть разрешение буфера
		"""

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
		"""
		Отрисовывает кадр из буфера в консоли
		"""

		self.clear()  # Очищаем консоль
		output_frame = ""
		for y in range(self.height):
			output_frame += "\n"
			for x in range(self.width):
				output_frame += " " + self.frameBuffer[y][x]
		print(output_frame)

	# Добавление горизонтального текста в буфер
	def drawHText(self, pos:Vector2, text:str):
		"""
		Добавляет горизонтальный текст в буфер
		
		:param pos: Стартавая позиция в буфере по x, y
		:type pos: Vector2
		:param text: Текст
		:type text: str
		"""
		for symbol in text:
			self.drawPixel(pos.copy(), symbol)
			pos.x += 1
	
	# Добавление вертикального текста в буфер
	def drawVText(self, pos:Vector2, text:str):
		"""
		Добавляет вертикальный текст в буфер
		
		:param pos: Стартавая позиция в буфере по x, y
		:type pos: Vector2
		:param text: Текст
		:type text: str
		"""
		for symbol in text:
			self.drawPixel(pos.copy(), symbol)
			pos.y += 1

	# Добавление горизонтальной линии в буфер
	def drawHLine(self, pos:Vector2, lenght:int, symbol:str):
		"""
		Добавляет горизонтальную линию в буфер
		
		:param pos: Стартовая позиция в буфере по x, y
		:type pos: Vector2
		:param lenght: Длинна линии в пикселях
		:type lenght: int
		:param symbol: Символ отрисовки
		:type symbol: str
		"""

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
		"""
		Добавляет вертикальную линию в буфер
		
		:param pos: Стартовая позиция в буфере по x, y
		:type pos: Vector2
		:param lenght: Длинна линии в пикселях
		:type lenght: int
		:param symbol: Символ отрисовки
		:type symbol: str
		"""

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
		"""
		Добавляет полый квадрат в буфер
		
		:param pos: Начальная позиция по x, y
		:type pos: Vector2
		:param size: Размер width, height
		:type size: Vector2
		:param symbol: Символ отрисовки
		:type symbol: str
		"""

		if len(symbol) == 1:
			self.drawHLine(pos.copy(), size.x, symbol)  # Отрисовка верхней границы,
			self.drawVLine(pos.copy(), size.y, symbol)  # Отрисовка левой границы,
			pos = pos.add(size.subtract(Vector2(1, 1)))  # Переносим курсор в конец квадрата
			self.drawHLine(pos.copy(), -size.x, symbol)  # Отрисовка нижней границы,
			self.drawVLine(pos.copy(), -size.y, symbol)  # Отрисовка правой границы,
		else:
			print("Получена строка а ожидался один символ!")
	
	# Добавление заполненного квадрата в буфер
	def drawFRect(self, pos:Vector2, size:Vector2, symbol:str) -> None:
		"""
		Добавляет заполненный квадрат в буфер
		
		:param pos: Начальная позиция по x, y
		:type pos: Vector2
		:param size: Размер width, height
		:type size: Vector2
		:param symbol: Символ отрисовки
		:type symbol: str
		"""

		if len(symbol) != 1:
			print("Получена строка а ожидался один символ!")
		else:
			for _ in range(size.y):
				self.drawHLine(pos.copy(), size.x, symbol)  # Отрисовка линии
				pos.y += 1  # Смещение курсора на пиксель вниз

	# Добавление пикселя в буфер
	def drawPixel(self, position:Vector2, symbol:str) -> None:
		"""
		Добавляет пиксель в буфер
		
		:param position: Позиция пикселя по x, y
		:type position: Vector2
		:param symbol: Символ отрисовки
		:type symbol: str
		"""

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
		"""
		Очищает консоль
		"""

		# Получение имени системы
		os_name = system()
		if os_name.lower() == "Windows".lower(): #Если это Windows
			os.system("cls")
		else: # Иначе это Linux/MacOS
			os.system("clear")
