import requests
import os.path

urlback = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/"
urlfront = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/"

for i in range(1, 152):

    if not os.path.exists('../Sprites/back/' + str(i) + '.png'):
        rback = requests.get(urlback + str(i) + ".png")
        with open('../Sprites/back/' + str(i) + '.png', 'wb') as back:
            back.write(rback.content)   
    
    if not os.path.exists('../Sprites/front/' + str(i) + '.png'):
        with open('../Sprites/front/' + str(i) + '.png', 'wb') as front:
            rfront = requests.get(urlfront + str(i) + ".png")
            front.write(rfront.content)
