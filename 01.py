from skimage import io, filters, img_as_float
from scipy.ndimage import laplace
import matplotlib.pyplot as plt

image_file = "lena_gray.bmp"
image = io.imread(image_file, as_gray=True)
image = img_as_float(image)  

laplaciano = laplace(image) 
unsharp_image = filters.unsharp_mask(image, radius=1, amount=1)  
k = 1.5
blurred = filters.gaussian(image, sigma=1)
highboost = image + k * (image - blurred)  
prewitt = filters.prewitt(image) 
sobel = filters.sobel(image)


fig, axes = plt.subplots(2, 3, figsize=(15, 10))
axes = axes.ravel() 


axes[0].imshow(image, cmap='gray')
axes[0].set_title("Imagem Original")
axes[0].axis('off')

axes[1].imshow(laplaciano, cmap='gray')
axes[1].set_title("Laplaciano")
axes[1].axis('off')

axes[2].imshow(unsharp_image, cmap='gray')
axes[2].set_title("Unsharp Masking")
axes[2].axis('off')

axes[3].imshow(highboost, cmap='gray')
axes[3].set_title("Highboost")
axes[3].axis('off')

axes[4].imshow(prewitt, cmap='gray')
axes[4].set_title("Bordas - Prewitt")
axes[4].axis('off')

axes[5].imshow(sobel, cmap='gray')
axes[5].set_title("Bordas - Sobel")
axes[5].axis('off')


plt.tight_layout()
plt.show()
