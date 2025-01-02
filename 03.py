import numpy as np

def uniao(image1, image2):
    a = np.maximum(image1, image2)
    return a

def intersecao(image1, image2):
    b = np.minimum(image1, image2)
    return b

def diferenca(image1, image2):
    c = np.clip(image1 - image2, 0, 1)
    return c
