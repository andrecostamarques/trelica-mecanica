### Import libraries ### ----------------------------------------------------------------------
import pandas as pd
import numpy as np
from collections import Counter
import operator
import math
import matplotlib.pyplot as plt
from statistics import mean

x="s" #valor inicial para saber se ele vai executar a primeira entrada de input
i=0 #contador para inputs
contador_apoio = 0 #contador pra salvar a quantidade de apoios

##================== valores de teste =========================;

# Joint = ["A","B","C","D","E","F","G","H"]
# X = [0,17,17,34,34,51,51,68]
# Y = [0,8,0,8,0,8,0,0]
# RX = [1,0,0,0,0,0,0,0]   ####### listas para adicionar ao banco de dados com os valores
# RY = [1,0,0,0,0,0,0,1]
# FX = [0,0,0,0,0,0,0,0]
# FY = [0,0,-10,0,-10,0,-10,0]
# start = ["A","A","B","B","B","C","D","D","E","E","F","F","G"]
# end = ["B","C","C","D","E","E","E","F","F","G","G","H","H"]


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
            rx = 1; ry = 0
            contador_apoio += 1
        elif r == "y":
            ry = 1; rx = 0  
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
    RX.insert(i,rx)		## insere todos os valores de x,y,rx,ry,fx,fy para as listas para depois a base de dados
    RY.insert(i,ry)
    FX.insert(i,fx)
    FY.insert(i,fy)

    more = input("Deseja criar mais um nó? s/n:")
    if more == "s":
        x = "s"
    else:
        x = "n"

    i = i +1


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


joints = pd.DataFrame(

    {

        "Joint": Joint,

        "X": X,

        "Y": Y,

        "RX": RX,		##criação das data bases -adicionando as listas

        "RY": RY,

        "FX": FX,

        "FY": FY,

    }

)

elements = pd.DataFrame(
    {
        "Start": start,

        "End": end,
    }
)


X_reactions = joints["RX"].tolist() # lista das reações de x 
Y_reactions = joints["RY"].tolist() # lista das reações de y

print("reacoes: \n")
print(X_reactions) ##debugando as reações
print(Y_reactions)

x_index = [i for i, x in enumerate(X_reactions) if x == 1]	# indice das reações em x
y_index = [i for i, x in enumerate(Y_reactions) if x == 1]	# indice das reações em y

# a função enumarate percorre o array todo, e se x for 1 ele vai adicionar o indice da arrey onde x é 1 e guarda no x_index
# que x_index tbm é uma array, onde ficam salvo os valores dos indices onde a array das reações é 1

print("indexes: \n")
print(x_index)		##debugando os indices
print(y_index)

# Lista das equações
if (len(x_index)) == 1: # 2 Rx e 1 Ry
	x_eq = [1, 0, 0]
	y_eq = [0, 1, 1] 
else:					# 1 Rx e 1 Ry
	x_eq = [1, 1, 0]
	y_eq = [0, 0, 1]

# como sempre tem que ter 3 reacoes (2x e 1y // 1x e 2y) ele ta assumindo que se tem 1 em x vai ter 2 y
# ele ta verificando isso a partir de ver qnts valores tem no index de x e index de y


X_values = [-i for i in joints["FX"].tolist()] # forca de x na igualidade
Y_values = [-i for i in joints["FY"].tolist()] # forca de y na igualidade

# ele ta pegando os valores de força que cada nó tem, negativando eles pra jogar pro outro lado da equação, pois assim
# comparamos nas outras equações. 

print(X_values) ##debugando os valores de F
print(Y_values)

m_eq = [] #lista para calcular os momentos

##vai começar a calcular os momentos, primeiro em x utilizando o indice de x (locais onde tem reacoes em x)

for i in x_index: # força de X * distancia do ponto. 
	# adiciona na eq de momento o - negativo de x reação * 
	m_eq.append(-X_reactions[i]*joints["Y"].tolist()[i])

for j in y_index: # força de X * distancia do ponto incial
	m_eq.append(Y_reactions[j]*joints["X"].tolist()[j])

M_F_X = [a*b for a, b in zip(joints["FX"].tolist(), joints["Y"].tolist())] # Somatória de momentos de Fx 
M_F_Y = [-a*b for a, b in zip(joints["FY"].tolist(), joints["X"].tolist())] # Somatória de momentos de Fy

#ele ta pegando os valores dos nós, listando os, listando as forças e multiplicando, a partir disso ele tem a somatória de momentos
#que vamos usar a somatória de moomentos para substituir os valores e resolver por meio do nunpy solve

a = np.array([x_eq, y_eq, m_eq]) # Parte esquerda da equação, usa a array do numpy
b = np.array([sum(X_values), sum(Y_values), sum(M_F_Y) + sum(M_F_X)]) 

R = np.linalg.solve(a, b).tolist() # Separamos os valores resultantes da somatória de momentos e colocamos no solve do np
print(a, b, R)

# Substituimos os novos valores pelos antigos da reação para a database
for i, val_x in enumerate(X_reactions):
	if val_x == 1: 
		X_reactions[i] = round(R[0], 2)	#checando os valores de x para ubstituir nas reações de x
		R.pop(0)

for j, val_y in enumerate(Y_reactions):
	if val_y == 1: 
		Y_reactions[j] = round(R[0], 2) #checando os valores de y para substituir nas reacoes em y
		R.pop(0)

joints["RX"] = X_reactions
joints["RY"] = Y_reactions		#atualiza a database de Rx e Ry com os novos valores.

joints.set_index("Joint", inplace = True)	#atualiza os indices da nova database

### resolvendo os braços ### ----------------------------------------------------------------------

elements["Name"] = [a + b for a, b in zip(elements["Start"], elements["End"])] #criando a lista com os nomes (juntando inicio com fim)
elements["Value"] = [None]*len(elements) # anotando os valores do valor inicial (primeira letra)

letters = Counter(elements["Start"].tolist() + elements["End"].tolist()) # quantidade de elementos no nó (não passa de 4)

sorted_letters = sorted(letters.items(), key=operator.itemgetter(1)) # filtrando pra que todos os braços fiquem organizados

sorted_letters = [list(ele) for ele in sorted_letters] # transformando a lista numa array

while (None in elements["Value"].tolist()):

	joint = sorted_letters[0][0] # ta verificando qual nó é oq tem mais coisa pra descobrir
								# ta fazendo isso pra gnt ter um norte de onde começar a fazer as contas

	e_forces = [] # criando a lista pra salvar os membros pra gnt fazer o método dos nós

	# marcando os nós que estão conectados a eles, pra desocbrir quais membros vamos calcular.

	for i in range(len(elements)):
		if (joint in elements["Name"][i]) and elements["Value"][i] == None: #vendo os nomes do elemento e comparando com seus valores pra
			e_forces.append(elements["Name"][i])							#pra saber qual ta conectado a qual

	# descobrindo os angulos entre os nós
	if len(e_forces) == 2:

		angles = []	#lista para os angulos

		for point in e_forces:

			y = joints.loc[point.replace(joint,"")]["Y"] - joints.loc[joint]["Y"] # y do vetor
			x = joints.loc[point.replace(joint,"")]["X"] - joints.loc[joint]["X"] # x do vetor

			if x < 0:
				angles.append(math.atan(y/x) + math.pi)

			elif x > 0:
				angles.append(math.atan(y/x))

			else:
				if y > 0:
					angles.append(math.pi/2) #adicionando aos angulos com base no numpy e atangente (pra descobrir qual é o valor de tan)
				else:
					angles.append(-math.pi/2)

			# diminuindo os valores de variaveis para calcular
			for i in range(len(sorted_letters)):
				if point.replace(joint,"") == sorted_letters[i][0]:
					sorted_letters[i][1] -= 1

		
		#depois de todas as variaveis organizadas a partir das letras e dos nomes. os angulos salvos, começamos a calcular os valroes de cada
		#lado da igualdade pra que a gnt descubra os valores das variaveis usando o solve.np


		left_x = [math.cos(angles[0]), math.cos(angles[1])]
		left_y = [math.sin(angles[0]), math.sin(angles[1])]

		right_x = -(joints.loc[joint]["RX"] + joints.loc[joint]["FX"])
		right_y = -(joints.loc[joint]["RY"] + joints.loc[joint]["FY"])
		
		a = np.array([left_x, left_y]) # organizando o lado esquerdo de x e y
		b = np.array([right_x, right_y]) #prganizando o lado direito de x e y

		R = np.linalg.solve(a, b).tolist() # colocando os dois lados da equação para descobrir os valores pedidos
		result = R.copy()

		elements_forces = [tuple(x) for x in list(zip(e_forces, R))] # salvando as forças em cada elemento na array

		for i in e_forces:
			for j, values in enumerate(elements["Name"].tolist()):
				if i == values:											#salvando os novos valores na lista/array/tupla
					elements["Value"][j] = round(result[0], 2)
					result.pop(0)
	
	# refazer tudo com um nó que só tenha 1 variável
	else:

		angles = []
		y = joints.loc[e_forces[0].replace(joint,"")]["Y"] - joints.loc[joint]["Y"] 
		x = joints.loc[e_forces[0].replace(joint,"")]["X"] - joints.loc[joint]["X"]

		if x < 0:
			angles.append(math.atan(y/x) + math.pi)

		elif x > 0:
			angles.append(math.atan(y/x))

		else:
			if y > 0:
				angles.append(math.pi/2)
			else:
				angles.append(-math.pi/2)

		for i in range(len(sorted_letters)):
			if e_forces[0].replace(joint,"") == sorted_letters[i][0]:
				sorted_letters[i][1] -= 1

		if angles[0] == 0:

			a = np.array([[math.cos(angles[0])]]) # esquerda da igualdade
			b = np.array([-(joints.loc[joint]["RX"] + joints.loc[joint]["FX"])]) # direita da igualdade

			result = np.linalg.solve(a, b)[0] #solução do numpy solve

		else:
			a = np.array([[math.sin(angles[0])]]) # esquerda da igualdade
			b = np.array([-(joints.loc[joint]["RY"] + joints.loc[joint]["FY"])]) # direita da igualdade

			R = np.linalg.solve(a, b)[0] # solução caso haja a necessidade de usar os novos valores dos angulos
			result = R

			elements_forces = (e_forces[0], R)

		for j, values in enumerate(elements["Name"].tolist()):
				if e_forces[0] == values:
					elements["Value"][j] = round(result, 2)

	# adiciona os valores da database para uma nova lista para que possamos calcular os valores finais
	FX_forces = joints["FX"].tolist()
	FY_forces = joints["FY"].tolist()
	
	# adiciona as forças com os membros para cada ponto na nova lista
	for point in e_forces:
		if len(e_forces) == 2:
			for i, j in enumerate(elements_forces):	
				if point == j[0]:
					for k, ind in  enumerate(list(joints.index.values)):
						if point.replace(joint,"") == ind:
							FX_forces[k]= FX_forces[k]-(R[i]*math.cos(angles[i]))
							FY_forces[k]= FY_forces[k]-(R[i]*math.sin(angles[i]))  #a nova lista recebe a derivada de cada angulo
																					# e agora temos os valores de todos as forças para todos 
																					#os pontos
		else:
			for k, ind in  enumerate(list(joints.index.values)):
				if point.replace(joint,"") == ind:
					FX_forces[k]= FX_forces[k]-(R*math.cos(angles[0]))
					FY_forces[k]= FY_forces[k]-(R*math.sin(angles[0]))
				

	# troca todos os valores de forças na database
	joints["FX"] = FX_forces
	joints["FY"] = FY_forces

	# filra a lista para que possamos calcular
	sorted_letters.pop(0)
	sorted_letters = sorted(sorted_letters, key=operator.itemgetter(1))
	

# joints[["RX", "RY"]].round(decimals = 2)
# elements["Value"].round(decimals = 2)

print(joints[["RX", "RY"]])
print(" ")							#enviando so valores para serem printados
print(elements[["Name", "Value"]])

print("---------------")
print("\n")
for i in range (len(x_index)):
	print(X[x_index[i]])			##printando para debuggar os valores finais, para que possamos plotar os valores nos graficos
	print(Y[x_index[i]])
	print(X_reactions[x_index[i]])

for i in range (len(y_index)):
	print(X[y_index[i]])
	print(Y[y_index[i]])
	print(Y_reactions[y_index[i]])


### Plot Truss + Results ### ----------------------------------------------------------------------


for i, name in enumerate(elements["Name"]):
	x_coord = [joints["X"][name[0]], joints["X"][name[1]]]
	y_coord = [joints["Y"][name[0]], joints["Y"][name[1]]]		#pltando as retas,os nós e os nomes

	plt.plot(x_coord, y_coord, "ro-")
	plt.text(mean(x_coord), mean(y_coord), str(round(elements["Value"][i], 2)), fontsize=12)		#plotando as forças e os pontos
	plt.text(x_coord[0], y_coord[0], name[0] , fontsize=12, color = "b", fontweight="bold")
	plt.text(x_coord[1], y_coord[1], name[1] , fontsize=12, color = "b", fontweight="bold")

	for i in range (len(x_index)):
		plt.text(X[x_index[i]], ((Y[x_index[i]])+.3),str(X_reactions[x_index[i]]),fontsize=12)

	for i in range (len(y_index)):			#plotando as reações em x e y em seus valores originais
		plt.text(X[y_index[i]], ((Y[y_index[i]])+.3),str(Y_reactions[y_index[i]]),fontsize=12)

plt.show()

class Point:						#funcao pra verificar se as linhas se cruzam
	def __init__(self,x,y):
		self.x = x
		self.y = y					#classe de ponto pra facilitar a utilização da função

def ccw(A,B,C):
	return (C.y-A.y)*(B.x-A.x) > (B.y-A.y)*(C.x-A.x)		#função pra calcular se eles são perpendiculares

def intersect(A,B,C,D):
	return ccw(A,C,D) != ccw(B,C,D) and ccw(A,B,C) != ccw(A,B,D)