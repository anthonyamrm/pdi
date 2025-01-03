from skimage import io
import numpy as np
import matplotlib.pyplot as plt

imagem = io.imread("quadro.png")  

red = imagem[..., 0]
green = imagem[..., 1]
blue = imagem[..., 2]

def preencher_buracos(imagem_binaria):
    imagem_invertida = np.logical_not(imagem_binaria)
    buracos_preenchidos = np.zeros_like(imagem_binaria, dtype=bool)
    stack = []

    for i in range(imagem_invertida.shape[0]):
        for j in range(imagem_invertida.shape[1]):
            if imagem_invertida[i, j] and (i == 0 or j == 0 or i == imagem_invertida.shape[0] - 1 or j == imagem_invertida.shape[1] - 1):
                stack.append((i, j))

    while stack:
        x, y = stack.pop()
        if imagem_invertida[x, y] and not buracos_preenchidos[x, y]:
            buracos_preenchidos[x, y] = True
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < imagem_invertida.shape[0] and 0 <= ny < imagem_invertida.shape[1]:
                    stack.append((nx, ny))

    return np.logical_or(imagem_binaria, np.logical_not(buracos_preenchidos))

objetos_azuis = (red < 50) & (green < 50) & (blue > 150)

objetos_amarelos = (red > 150) & (green > 150) & (blue < 100)

objetos_verdes = (red < 100) & (green > 150) & (blue < 100)

azul_preenchido = preencher_buracos(objetos_azuis)
amarelo_preenchido = preencher_buracos(objetos_amarelos)
verde_Preenchido = preencher_buracos(objetos_verdes)

verm = np.copy(red)
verd = np.copy(green)
azu = np.copy(blue)

verm[azul_preenchido] = 0
verd[azul_preenchido] = 0
azu[azul_preenchido] = 255  

verm[amarelo_preenchido] = 255 
verd[amarelo_preenchido] = 255
azu[amarelo_preenchido] = 0

verm[verde_Preenchido] = 0
verd[verde_Preenchido] = 255  
azu[verde_Preenchido] = 0

imagem_final = np.stack([verm, verd, azu], axis=-1)

fig, axes = plt.subplots(1, 2, figsize=(10, 5))

axes[0].imshow(imagem)
axes[0].set_title("Imagem original")
axes[0].axis("off")

axes[1].imshow(imagem_final)
axes[1].set_title("Imagem com buracos preenchidos")
axes[1].axis("off")

plt.tight_layout()
plt.show()
