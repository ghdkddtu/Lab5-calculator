num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))

message = '''
Выберите математическую операцию:
+ : Сложение
- : Вычитание
* : Умножение

Ваш выбор: '''

operation = input(message)

if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
else:
    print('Неизвестная операция')
    exit()

print("Ответ:", result)
