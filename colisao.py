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

for ligacao in ligacoes:
            if verificaVetoresCruzam(nos[ligacao[0]], nos[ligacao[1]], nos[no1-1], nos[no2-1]):
                  if not any((no[0], no[1]) == localizaCruzamentoVetores(nos[ligacao[0]], nos[ligacao[1]], nos[no1-1], nos[no2-1]) for no in nos):
                        raise ValueError("Você inseriu ligações que se cruzam!")