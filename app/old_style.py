import os
import sys
from datetime import datetime, timedelta
from math import pi, sqrt


def sum_numbers(a: int) -> int:
	second_number = int(
		input(
			"В это поле необходимо ввести второе число, с которым"
			" в последующем "
			"будет складываться первое число. Введите число:\n"
		)
	)
	result = a + second_number
	print(f"Результат сложения: {result}")
	return result


first_number = int(
	input("В это поле необходимо ввести первое число. Введите число: \n")
)

sum_numbers(first_number)

print("Завершение программы...")
