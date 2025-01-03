from skimage import io, img_as_float
import numpy as np
from skimage.filters import median
from scipy.ndimage import convolve
from skimage.morphology import square
import matplotlib.pyplot as plt

imagem = img_as_float(io.imread("lena_ruido.bmp", as_gray=True))

mascara1 = 1/5 * np.array([[0,1,0],
                           [1,1,1],
                           [0,1,0]])

mascara2 = 1/9 * np.array([[1,1,1],
                           [1,1,1],
                           [1,1,1]])

mascara3 = 1/32 * np.array([[1,3,1],
                           [3,16,3],
                           [1,3,1]])

mascara4 = 1/8 * np.array([[0,1,0],
                           [1,4,1],
                           [0,1,0]])

img_m1 = convolve(imagem, mascara1)
img_m2 = convolve(imagem, mascara2)
img_m3 = convolve(imagem, mascara3)
img_m4 = convolve(imagem, mascara4)

img_mediana = median(imagem,square(3))

plt.figure(figsize=(12, 10))

plt.subplot(3, 2, 1)
plt.title("Imagem Original")
plt.imshow(imagem, cmap='gray')
plt.axis('off')

plt.subplot(3, 2, 2)
plt.title("Máscara 1")
plt.imshow(img_m1, cmap='gray')
plt.axis('off')

plt.subplot(3, 2, 3)
plt.title("Máscara 2")
plt.imshow(img_m2, cmap='gray')
plt.axis('off')

plt.subplot(3, 2, 4)
plt.title("Máscara 3")
plt.imshow(img_m3, cmap='gray')
plt.axis('off')

plt.subplot(3, 2, 5)
plt.title("Máscara 4")
plt.imshow(img_m4, cmap='gray')
plt.axis('off')

plt.subplot(3, 2, 6)
plt.title("Filtro da Mediana")
plt.imshow(img_mediana, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()


