x="s"
i=0

while x == "s":

    name = chr(i+65) #da o nome de uma letra (nesse caso = A)
    dx = input(f'Crie o nó {name}, defina seu local no eixo X: ') #salva a distancia de x 
    dy = input("Defina o local no eixo Y: ") #salva a distancia de y

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


    more = input("Deseja criar mais um nó? s/n:")
    if more == "s":
        x = "s"
    else:
        x = "n"

    i = i +1


# no que vai ser conectado : 
# no que vai conectar : 
# os dois nois na lista.