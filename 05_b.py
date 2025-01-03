from skimage import io
import numpy as np
import matplotlib.pyplot as plt

imagem = io.imread("quadro.png") 

red = imagem[..., 0]
green = imagem[..., 1]
blue = imagem[..., 2]

black_objects = (red == 0) & (green == 0) & (blue == 0)

red_removed = np.where(black_objects, 255, red)
green_removed = np.where(black_objects, 255, green)  
blue_removed = np.where(black_objects, 255, blue)  

imagem_final = np.stack([red_removed, green_removed, blue_removed], axis=-1)
fig, axes = plt.subplots(1, 2, figsize=(10, 5))

axes[0].imshow(imagem)
axes[0].set_title("Imagem original")
axes[0].axis("off")

axes[1].imshow(imagem_final)
axes[1].set_title("Imagem sem objetos pretos")
axes[1].axis("off")

plt.tight_layout()
plt.show()
