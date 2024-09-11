first = input('Введите первое число: ')
second = input('Введите второе число: ')
third = input('Введите третье число: ')

# Вариант решения 1 (по заданию)
print()
print('Вариант решения 1:')  # Для более удобной визуализации вывода результата

if first == second == third:
    print(3)
elif first == second:
    print(2)
elif second == third:
    print(2)
elif first == third:
    print(2)
else:
    print(0)

# Вариант решения 2 (свой)
print()
print('Вариант решения 2:')  # Для более удобной визуализации вывода результата

if first == second and second == third:
    print(3)
elif first == second or second == third or first == third:
    print(2)
else:
    print(0)