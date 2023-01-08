import os

# os.system('pip install redis')

import redis

r = redis.Redis(host='redis')

while True:
    try:
        val = input('Введите пример: ')
    except EOFError:
        val = 'stop'
    if val.lower() == 'stop':
        break
    r.lpush('commands', val)
print("Вы завершили программу")
