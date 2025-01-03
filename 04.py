import numpy as np

def aplicacao_elem_estruturante(image, elementro_estruturante, center, operacao):
    padded = np.pad(image,                   
        ((center[0], elementro_estruturante.shape[0] - center[0] - 1),
        (center[1], elementro_estruturante.shape[1] - center[1] - 1)), 
    mode='constant', constant_values=0)
    result = np.zeros_like(image)
    
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            #Recorte da região correspondente ao elemento estruturante
            region = padded[i:i+elementro_estruturante.shape[0], j:j+elementro_estruturante.shape[1]]
            if operacao == "dilatacao":
                result[i, j] = np.max(region * elementro_estruturante)
            elif operacao == "erosao":
                result[i, j] = np.min(region * elementro_estruturante)
    
    return result

def dilatacao(image, elementro_estruturante, center):
    dilatacao = aplicacao_elem_estruturante(image, elementro_estruturante, center, operacao="dilatacao")
    return dilatacao

def erosao(image, elementro_estruturante, center):
    erosao = aplicacao_elem_estruturante(image, elementro_estruturante, center, operacao="erosao")
    return erosao

def abertura(image, elementro_estruturante, center):
    ero = erosao(image, elementro_estruturante, center)
    return dilatacao(ero, elementro_estruturante, center)

def fechamento(image, elementro_estruturante, center):
    dil = dilatacao(image, elementro_estruturante, center)
    return erosao(dil, elementro_estruturante, center)

