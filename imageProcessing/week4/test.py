import cv2
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = [20, 20]
plt.rcParams['figure.dpi'] = 461

plt.figure(figsize=(6.4 * 5, 4.8 * 5), constrained_layout=False)

img_c1 = cv2.imread("period_input.jpg", 0)
H = np.ones(img_c1.shape[:2])
H[49:59, 39:49] = 0
H[34:47, 102:112] = 0
H[86:96, 17:27] = 0
H[75:85, 82:92] = 0
H[150:160, 17:27] = 0

img_c2 = np.fft.fft2(img_c1)
img_c3 = np.fft.fftshift(img_c2)

# Apply the designed filter H to the centered spectrum
img_c6 = H * img_c3

# Inverse Fourier transform to obtain the filtered image
img_c4 = np.fft.ifftshift(img_c6)
img_c5 = np.fft.ifft2(img_c4)

# Properly scale the Fourier spectrum and filtered image for visualization
spectrum = np.log(1 + np.abs(img_c3))
filtered_image = np.abs(img_c5)

plt.subplot(141), plt.imshow(img_c1, "gray"), plt.title("Original Image")
plt.subplot(142), plt.imshow(spectrum, "gray"), plt.title("Spectrum")
plt.subplot(143), plt.imshow(np.log(1 + np.abs(img_c6)), "gray"), plt.title("Filtered Spectrum")
plt.subplot(144), plt.imshow(H, "gray"), plt.title("Designed Filter")
plt.show()
