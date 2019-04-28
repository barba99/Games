#!usr/bin/env python3
# -*- coding: utf-8 -*-
 
import os
import random
 
palabraAdivinar     = random.choice('atun chope pasas disputa lavadora consumir senado espacio semaforo volver relampaguear levadizo espia tocar aduana barba convidar hembra mexico jet conde mochiila hermanastra america flauta hipopotamo empacar medico popular balcon combate hormiga babuino tejon murcielago oso castor camello gato almeja cobra pantera coyote cuervo ciervo perro burro pato aguila huron zorro rana cabra ganso halcon leon paloma piton conejo carnero rata cuervo rinoceronte salmon foca tiburon oveja mofeta perezoso serpiente araña cigüeña cisne tigre Sapo trucha pavo tortuga comadreja ballena lobo wombat cebra'.split(' '))
listaPalabraAdiv    = []
listaPalabraMost    = []
intentos            = 7
vidas               = 0
letra               = ''
run                 = True
 
banner = ['''
 
   +---+
   |   |
       |
       |
       |
       |
=========''','''
 
   +---+
   |   |
   O   |
       |
       |
       |
=========''','''
 
   +---+
   |   |
   O   |
   |   |
       |
       |
=========''','''
 
   +---+
   |   |
   O   |
  /|   |
       |
       |
=========''','''
 
   +---+
   |   |
   O   |
  /|\  |
       |
       |
=========''','''
 
   +---+
   |   |
   O   |
  /|\  |
  /    |
       |
=========''','''
 
   +---+
   |   |
   O   |
  /|\  |
  / \  |
       |
=========''']
 
 
listaPalabraAdiv = list(palabraAdivinar)
 
for item in listaPalabraAdiv:
    listaPalabraMost.append('_')
 
while run:
 
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
    print('AHORCADO\n')
    print('Te quedan {intentos} intentos'.format(intentos=intentos))
    print(banner[vidas])
    print("\n"+' '.join(listaPalabraMost))
 
    letra = input('\nletra: ')
 
 
    fallo = False
 
    if letra[0] not in listaPalabraAdiv:
 
        fallo = True
        intentos -= 1
        vidas += 1
    else:
 
        for key, value in enumerate(listaPalabraAdiv):
            if value == letra:
                listaPalabraMost[key] = value
 
    if intentos <= 0:
        run = False
        print('Has perdido, la palabra '
              'era "{palabra}"'.format(palabra=''.join(listaPalabraAdiv)))
    elif listaPalabraAdiv == listaPalabraMost:
        run = False
        print('Has ganado, la palabra '
              'era "{palabra}"'.format(palabra=''.join(listaPalabraAdiv)))
    
