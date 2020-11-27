import numpy as np
import matplotlib.pyplot as plt

# add: Pad the image with zeros on all sides to perform filtering on the border pixels.

def median_filter(image, filter_size):
    temp = [] # temp = empty array
    width = len(image)
    length = len(image[0])
    
    median_index = filter_size//2 # '//' is integer division
    # The index that is obtained by dividing the total number of elements in a window by 2 gives us the median position.
    # e.g. if we have a 5x5 window (filter_size = 5), the median is 2, [0 1 2 3 4].
    #           for a 3x3 window the median will be 1, [0 1 2].
    
    data_final = [] # data_final = empty array
    data_final = np.zeros((width,length)) # data_final = 2D array filled with zeros
    for i in range(width):
        for j in range(length):
            for z in range(filter_size):
                if ((i+z-median_index < 0) or (i+z-median_index > width-1)): # out of bounds
                    for c in range(filter_size):
                        temp.append(0)
                else:
                    if ((j+z-median_index < 0) or (j+median_index > length-1)): # out of bounds
                        temp.append(0)
                    else:
                        for k in range(filter_size):
                            temp.append(image[i+z-median_index][j+k-median_index])
            temp.sort()
            data_final[i][j] = temp[len(temp) // 2]
            temp = [] # overwrite 'temp' with an empty array
    return data_final



if __name__ == '__main__':
    # Load image and convert it to gray scale
    img = plt.imread('head.jpg')
    gray_img = np.dot(img[...,:3], [0.299, 0.587, 0.114])

    # Apply Median Filter
    # Define the window size NxN, e.g.: 3x3, 7x7, 13x13
    removed_noise = median_filter(gray_img, 7) # NxN=7x7

    # Display results
    fig = plt.figure(figsize = (12, 10))
    display = [gray_img, removed_noise]
    title = ['Original Image', '7x7 Median Filter']
    for i in range(len(display)):
        fig.add_subplot(2, 2, i+1)
        plt.imshow(display[i], cmap = 'gray')
        plt.title(title[i])
    
    plt.show()