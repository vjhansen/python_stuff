# -*- coding:utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

def median_blur(img, kernel):
    Width, Height, Ch = img.shape
    N = kernel

    # Padding image
    padding = (N - 1) // 2
    if Ch == 1: # GRAY = 1 channel, trengs ikke...
        padding = ((padding, padding,), (padding, padding))
    else: # RGB = 3 channels
        padding = ((padding, padding,), (padding, padding), (0, 0))

    img_pad = np.pad(img, padding, mode='constant', constant_values=0)

    # Find median
    result = np.zeros_like(img, dtype=img.dtype)
    for i in range(Width):
        for j in range(Height):
            result[i, j] = np.median(img_pad[i:i+N, j:j+N], axis=(0, 1))
    return result

if __name__ == "__main__":
    test_img = plt.imread('head.jpg')

    kernel_size = 7
    median_blur_img = median_blur(test_img, kernel_size)

    _, (ax1, ax2) = plt.subplots(1, 2)
    ax1.set_title('Original image')
    ax1.imshow(test_img)
    ax2.set_title('7x7 Median Blur image')
    ax2.imshow(median_blur_img)
    plt.show()