# coding=utf-8
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('logo-if.jpg',0)

dft = np.fft.fft2(img)
dft_shift = np.fft.fftshift(dft)
magnitude_spectrum = 20*np.log(np.abs(dft_shift))

(fig, ax) = plt.subplots(1, 2, )
ax[0].imshow(img, cmap="gray")
ax[0].set_title("Imagem")
ax[0].set_xticks([])
ax[0].set_yticks([])

ax[1].imshow(magnitude_spectrum, cmap="gray")
ax[1].set_title("Espectro")
ax[1].set_xticks([])
ax[1].set_yticks([])

plt.show()
