#Калькулятор версии 4.0.2

import os
import config
from colorama import Fore, Style, init
init(autoreset = True) #Ресет цвета текста

#Переменные цветов текста
M = Fore.LIGHTMAGENTA_EX + Style.BRIGHT
C = Fore.LIGHTCYAN_EX + Style.BRIGHT
G = Fore.LIGHTGREEN_EX + Style.BRIGHT
Y = Fore.LIGHTYELLOW_EX + Style.BRIGHT

#Отображение тега и версии из config
print(config.teg, config.line)
color = config.ColorLine

#Работа данных через цикл while
while True:
		
		inp = input(C+"\nВведите значение >> "+G)
		
		if inp == "exit": #Заканчивает работу
			break
			
		if inp in ("+", "-", "*", "/", "**"):
			a = int(input(C + "Введи первые цифры >> "+G))
			b = int(input(C + "Введи вторые цифры >> "+G))
			os.system("clear || cls")
			
			#Вычесления данных из выше написанного
			
			if inp == "+":
				print(config.teg + G + "\n" + color + f"\n{C}Итого: {a} + {b} = {Y} {a + b}")
				print(G + color)
			
			elif inp == "-":
				print(config.teg + G + "\n" + color + f"\n{C}Итого: {a} - {b} = {Y} {a - b}")
				print(G + color)
				
			elif inp == "*":
				print(config.teg + G + "\n" + color + f"\n{C}Итого: {a} * {b} = {Y} { a * b}")
				print(G + color)
			
			elif inp == "/":
				#На ноль делить нельзя!
				if b != 0:
					print(config.teg + G + "\n" + color + f"\n{C}Итого: {a} / {b} = {Y} {a / b}")
					print(G + color)
				
				else:
					print(config.teg + Y + color + f"\nНельзя делить на ноль!\n{color}")

			elif inp == "**":
				print(config.teg +  G + "\n" + color + f"\n{C}Итого: {a} √ {b} = {Y} {a ** b}")
				print(G + color)

		else:
			print(Y + color)
			print(Y + f"Неверное значение!\n{color}")