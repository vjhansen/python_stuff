# -*- coding:utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

def median_blur(img, kernel):
    Width, Height = img.shape
    N = kernel

    # Padding image
    pad_xy = (N - 1) // 2
    padding = ((pad_xy, pad_xy,), (pad_xy, pad_xy), (0, 0))
    img_pad = np.pad(img, padding, mode='constant', constant_values=0)

    # Find median
    result = np.zeros_like(img, dtype=img.dtype)
    for i in range(Width):
        for j in range(Height):
            result[i, j] = np.median(img_pad[i:i+N, j:j+N], axis=(0, 1))
    return result

if __name__ == "__main__":
    test_img = plt.imread('head.jpg')

    kernel_size = 7 # change this, e.g. 3, 5, 7, 9, 13, etc..
    median_blur_img = median_blur(test_img, kernel_size)

    _, (ax1, ax2) = plt.subplots(1, 2)
    ax1.set_title('Original image')
    ax1.imshow(test_img)
    ax2.set_title('7x7 Median Blur image')
    ax2.imshow(median_blur_img)
    plt.show()
