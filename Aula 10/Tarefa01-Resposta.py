import numpy as np
import cv2

# img = cv2.imread('noise.jpg')

# dft = np.fft.fft2(img)
# dft_shift = np.fft.fftshift(dft)

# magnitude_spectrum = np.log(np.abs(dft_shift))/20

# radius = 150
# mask = np.ones_like(img)
# cy = mask.shape[0] // 2
# cx = mask.shape[1] // 2
# cv2.circle(mask, (cx,cy), radius, (255,255,255), -1)[0]
# mask = cv2.GaussianBlur(mask, (3,3), 0)

# dft_shift_masked = np.multiply(dft_shift,mask) / 255
# back_ishift = np.fft.ifftshift(dft_shift)
# back_ishift_masked = np.fft.ifftshift(dft_shift_masked)

# img_filtered = np.fft.ifft2(back_ishift_masked)
# img_filtered = np.abs(3*img_filtered).clip(0,255).astype(np.uint8)


# cv2.imshow("Imagem", img)
# cv2.imshow("Espectro", magnitude_spectrum)
# cv2.imshow("Mascara", mask)
# cv2.imshow("Resultado", img_filtered)

# cv2.waitKey(0)
# cv2.destroyAllWindows()
