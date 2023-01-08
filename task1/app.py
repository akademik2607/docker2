while True:
    val = input('Введите пример: ')
    if val.lower() == 'stop':
        break
    print(eval(val))
print("Вы завершили программу")
