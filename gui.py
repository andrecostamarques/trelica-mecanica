import numpy as np
import pandas as pd

x="s" #valor inicial para saber se ele vai executar a primeira entrada de input
i=0 #contador para inputs
contador_apoio = 0 #contador pra salvar a quantidade de apoios
Joint = []
X = []
Y = []
RX = []   ####### listas para adicionar ao banco de dados com os valores
RY = []
FX = []
FY = []
start = []
end = []

while x == "s":  #enquanto o valor de contar os inputs está um

    name = chr(i+65) #da o nome de uma letra (nesse caso = A)
    dx = float(input(f'Crie o nó {name}, defina seu local no eixo X: ')) #salva a distancia de x 
    dy = float(input("Defina o local no eixo Y: ")) #salva a distancia de y

    #fala se o ponto tem reação
    if(contador_apoio <= 1):
        r = input("Esse nó vai ter apoio? Retorne x para reação no x, y para reação no y e xy para em ambos, pule se nada: ")
        if r == "x":
            rx = 1
            contador_apoio += 1
        elif r == "y":
            ry = 1  
            contador_apoio += 1
        elif r == "xy":
            rx = 1
            ry = 1
            contador_apoio += 1
        else:
            rx = 0
            ry = 0

    #salva os valores em uma matriz/lista

    if (input("Esse nó vai ter força em diagonal? s/n:") == "s"):
        ang = float(input("Defina o angulo em relação ao eixo x: "))
        forca = float(input("Defina o modulo da força: "))
        fx = np.sin(np.deg2rad(ang)) * forca
        fy = np.cos(np.deg2rad(ang)) * forca                ##ta derivando os valores das forças a partir de seus angulos
    else:
        fx=float(input("Defina a força em X: "))
        fy=float(input("Defina a força em Y: "))

    Joint.insert(i,name)
    X.insert(i,dx)
    Y.insert(i,dy)
    RX.insert(i,rx)
    RY.insert(i,ry)
    FX.insert(i,fx)
    FY.insert(i,fy)

    more = input("Deseja criar mais um nó? s/n:")
    if more == "s":
        x = "s"
    else:
        x = "n"

    i = i +1

print(Joint)
print(X)
print(Y)
print(RX)
print(RY)
print(FX)
print(FY)

#### -------- pegando os inputs de conexões
x = 0 #zerando o valor de x para voltar a ter o while

while x < (len(Joint)-1):
    
    coneco = int(input(f'O nó {Joint[x]} tem quantas conexões?: ')) #quantidade de vezes que vai ter q rodar o for pra anotar

    i = 0

    for i in range(coneco): #o valor inicial

        start.insert(i,Joint[x]) #adicionando o inicial todas as vezes que ele rodar
        final = input(f'Defina uma das conexões do nó {Joint[x]}: ')
        end.insert(i,final.upper())  #adicionando o valor escrito que se conecta
        coneco += 1
    
    x += 1 #adiciona 1 no x pra ele ir pro próximo nó inicial

start.reverse() ##inverte o 
end.reverse()

print(start)
print(end)

Jointdata = pd.DataFrame(

    {

        "Joint": Joint,

        "X": X,

        "Y": Y,

        "RX": RX,

        "RY": RY,

        "FX": FX,

        "FY": FY,

    }

)
print(Jointdata)

Elementdata = pd.DataFrame(
    {
        "Start": start,

        "End": end,
    }
)

print(Elementdata)
# no que vai ser conectado : 
# no que vai conectar : 
# os dois nois na lista


