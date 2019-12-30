import time
from time import sleep
import random

sus = "-" * 35
depo =["piedra", "papel", "tijera"]


while True:
    x = raw_input("que elijes?, piedra, papel, tijera: ")
    print(sus)
    if x not in depo:
        print('No hagas trampa!!!')
        print(sus)
        continue
    
    pc = random.choice(depo)
    sleep(0.5)
    print(('Pc elige {}.'). format(pc))
    if x == pc:
        print('Emapte')
        print(sus)
    elif x == "piedra" and pc == 'tijera':
        print('Ganaste')
        print(sus)
    elif x == 'papel' and pc == 'piedra':
        print('Ganaste')
        print(sus)
    elif x == 'tijera' and pc == 'papel':
        print('Ganaste')
        print(sus)
    else: 
        print('Perdimos. {} gana {} '.format(pc,x))
        print(sus)