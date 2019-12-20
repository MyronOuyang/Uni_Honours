import cv2
from matplotlib import pyplot as plt
import numpy as np
import os
import scipy as sp
from scipy import fftpack as fp


def dft(img):

    width, height = img.shape
    results = np.zeros((width, height), dtype=complex)

    for width_index in range(width):
        for height_index in range(height):
            result = 0
            for i in range(width):
                for n in range(height):
                    f_val = img[i][n]
                    e = np.exp(-1j * 2 * sp.pi * (float(width_index * i) / width + float(height_index * n) / height))
                    result += f_val * e
            results[width_index][height_index] = result / (width * height)

    return results


def inverse_dft(img):

    width, height = img.shape
    results = np.zeros((width, height), dtype=float)

    for i in range(width):
        for n in range(height):
            result = 0
            for width_index in range(width):
                for height_index in range(height):
                    f_val = img[height_index][width_index] 
                    e = np.exp(1j * 2 * sp.pi * (float(width_index * i) / width + float(height_index * n) / height))
                    result += f_val * e
            results[i][n] = int(np.real(result) + 0.5)

    return results


def shift(img):
    img = np.asarray(img)
    axes = tuple(range(img.ndim))
    shift = [dim // 2 for dim in img.shape]

    return np.roll(img, shift, axes)


image = cv2.imread("pics/small_lena.png", 0)
fourier_transform = dft(image)
fourier_inverse = inverse_dft(fourier_transform)

shifted = shift(fourier_transform)
magnitude_spectrum = 20 * np.log(np.abs(shifted))
plt.subplot()
plt.imshow(magnitude_spectrum, cmap='gray')
plt.show()

inverse_magnitude_spectrum = 20 * np.log(np.abs(fourier_inverse))
inverse_magnitude_spectrum = np.transpose(inverse_magnitude_spectrum)
plt.subplot()
plt.imshow(inverse_magnitude_spectrum, cmap='gray')
plt.show()
