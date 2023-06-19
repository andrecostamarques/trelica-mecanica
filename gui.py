import numpy as np

x="s"
i=0

while x == "s":

    name = chr(i+65) #da o nome de uma letra (nesse caso = A)
    dx = float(input(f'Crie o nó {name}, defina seu local no eixo X: ')) #salva a distancia de x 
    dy = float(input("Defina o local no eixo Y: ")) #salva a distancia de y

    #fala se o ponto tem reação
    r = input("Esse nó vai ter apoio? Retorne x para reação no x, y para reação no y e xy para em ambos, pule se nada: ")
    if r == "x":
        rx = 1
    elif r == "y":
        ry = 1  
    elif r == "xy":
        rx = 1
        ry = 1
    else:
        rx = 0
        ry = 0

    #salva os valores em uma matriz/lista

    if (input("Esse nó vai ter força em diagonal? s/n:") == "s"):
        ang = float(input("Defina o angulo em relação ao eixo x: "))
        forca = float(input("Defina o modulo da força: "))
        fx = np.sin(np.deg2rad(ang)) * forca
        fy = np.cos(np.deg2rad(ang)) * forca
    else:
        fx=input("Defina a força em X: ")
        fy=input("Defina a força em Y: ")

    more = input("Deseja criar mais um nó? s/n:")
    if more == "s":
        x = "s"
    else:
        x = "n"

    i = i +1


# no que vai ser conectado : 
# no que vai conectar : 
# os dois nois na lista.