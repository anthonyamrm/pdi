from skimage import io, morphology
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
verde_preenchido = preencher_buracos(objetos_verdes)

azul_fecho = morphology.convex_hull_image(azul_preenchido)
amarelo_fecho = morphology.convex_hull_image(amarelo_preenchido)
verde_fecho = morphology.convex_hull_image(verde_preenchido)

fig, axes = plt.subplots(1, 4, figsize=(20, 5))

axes[0].imshow(imagem)
axes[0].set_title("Imagem original")
axes[0].axis("off")

axes[1].imshow(azul_fecho, cmap="gray")
axes[1].set_title("Fecho convexo azul")
axes[1].axis("off")

axes[2].imshow(amarelo_fecho, cmap="gray")
axes[2].set_title("Fecho convexo amarelo")
axes[2].axis("off")

axes[3].imshow(verde_fecho, cmap="gray")
axes[3].set_title("Fecho convexo verde")
axes[3].axis("off")

plt.tight_layout()
plt.show()
