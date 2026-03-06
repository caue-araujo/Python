tempo = int(input())

horas = tempo // 3600
tempo = tempo % 3600
minutos = tempo // 60
segundos = tempo  % 60

print('{}:{}:{}'.format(horas,minutos,segundos))