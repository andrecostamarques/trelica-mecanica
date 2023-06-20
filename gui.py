import numpy as np
import pandas as pd

def verificaVetoresCruzam(A, B, C, D):
    # Verifica se os vetores AB e AC têm direções opostas
    cross1 = (D[0]-C[0]) * (A[1]-C[1]) - (D[1]-C[1]) * (A[0]-C[0])
    
    # Verifica se os vetores CD e CA têm direções opostas
    cross2 = (B[0]-A[0]) * (C[1]-A[1]) - (B[1]-A[1]) * (C[0]-A[0])
    
    # Verifica se os vetores cruzam
    if cross1 * cross2 < 0:
        return True
    else:
        return False
    
def localizaCruzamentoVetores(A, B, C, D):      #for i in rang()
    # Coordenadas dos pontos dos vetores        if 
    x1, y1 = A
    x2, y2 = B
    x3, y3 = C
    x4, y4 = D
    
    # Determinante da matriz
    det1 = (x1 - x2) * (y3 - y4)
    det2 = (y1 - y2) * (x3 - x4)
    det_total = det1 - det2
    
    # Verifica se os vetores são paralelos
    if det_total == 0:
        return None  # Vetores paralelos, não há ponto de interseção
    
    # Coordenadas do ponto de interseção
    x = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / det_total
    y = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / det_total
    
    return x, y

class Point:
	def __init__(self,x,y):
		self.x = x
		self.y = y

def ccw(A,B,C):
	return (C.y-A.y)*(B.x-A.x) > (B.y-A.y)*(C.x-A.x)

def intersect(A,B,C,D):
	return ccw(A,C,D) != ccw(B,C,D) and ccw(A,B,C) != ccw(A,B,D)

x="s" #valor inicial para saber se ele vai executar a primeira entrada de input
i=0 #contador para inputs
Joint = []
X = []
Y = []
RX = []   ####### listas para adicionar ao banco de dados com os valores
RY = []
FX = []
FY = []
start = []
end = []
nos1 = [] 

while x == "s":  #enquanto o valor de contar os inputs está um

    name = chr(i+65) #da o nome de uma letra (nesse caso = A)
    dx = float(input(f'Crie o nó {name}, defina seu local no eixo X: ')) #salva a distancia de x 
    dy = float(input("Defina o local no eixo Y: ")) #salva a distancia de y

    #fala se o ponto tem reação
    r = input("Esse nó vai ter apoio? Retorne x para reação no x, y para reação no y e xy para em ambos, pule se nada: ")
    if r == "x":
        rx = 1
        ry = 0
    elif r == "y":
        ry = 1
        rx = 0  
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

for i in range(len(Joint)):
    nos1.append((X[i],Y[i]))  
    
for i in range(len(start)): #indice de cada um que tem no start
    for j in range(len(start)):
        noA = nos1[int(ord(start[i])-65)]
        noB = nos1[int(ord(end[i])-65)]
        noC = nos1[int(ord(start[j])-65)]
        noD = nos1[int(ord(end[j])-65)]
        if verificaVetoresCruzam(noA, noB, noC, noD):
            intersecao = localizaCruzamentoVetores(noA, noB, noC, noD)
            if not any((no[0], no[1]) == intersecao for no in nos1):
                raise ValueError("Houve cruzamento de membros não desejado!")


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


