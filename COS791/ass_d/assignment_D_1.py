import numpy as np
import matplotlib.pyplot as plt
import cv2
import math


def hough_transform(img, threshold):
    theta_arr = np.deg2rad(np.arange(-90.0, 90.0))
    width, height = img.shape
    max_length = int(np.ceil(np.sqrt(width * width + height * height)))  # max_dist
    rhos = np.linspace(-max_length, max_length, max_length * 2.0)

    # Cache some resuable values
    cos_t = np.cos(theta_arr)
    sin_t = np.sin(theta_arr)
    len_theta_arr = len(theta_arr)

    # Hough accumulator array of theta vs rho
    accumulator = np.zeros((2 * max_length, len_theta_arr))
    y_edges, x_edges = np.nonzero(img)  # (row, col) indexes to edges

    # for y_index in range(height):
    #     for x_index in range(width):
    #         if img[y_index, x_index] > 0:
    #             for i in range(len_theta_arr):
    #                 # Calculate rho. max_length is added for a positive index
    #                 rho = int(round(x_index * np.cos(np.pi * i / 180) + y_index * np.sin(np.pi * i / 180) + max_length))
    #                 accumulator[rho, i] += 1

    for i in range(len(x_edges)):
        x = x_edges[i]
        y = y_edges[i]

        for i in range(len_theta_arr):
            # Calculate rho. max_length is added for a positive index
            rho = int(round(x * cos_t[i] + y * sin_t[i]) + max_length)
            accumulator[rho, i] += 1

    distance_arr, angle_arr = np.where(accumulator >= threshold)
    res = {
        'theta_arr': theta_arr,
        'rhos': rhos,
        'angle_arr': angle_arr,
        'distance_arr': distance_arr,
        'accumulator': accumulator,
    }

    # return accumulator, theta_arr, rhos
    return res

def draw_line(img, res):
    # find the end point
    theta_arr = res['theta_arr']
    rhos = res['rhos']
    angle_arr = res['angle_arr']
    distance_arr = res['distance_arr']
    # redraw the lines
    for index, theta in enumerate(angle_arr):
        a = np.cos(theta_arr[theta])
        b = np.sin(theta_arr[theta])
        x0 = a * int(rhos[distance_arr[index]])
        y0 = b * int(rhos[distance_arr[index]])
        x1 = int(x0 + 500 * (-b))
        y1 = int(y0 + 500 * (a))
        x2 = int(x0 - 500 * (-b))
        y2 = int(y0 - 500 * (a))

        point_1 = (x1, y1)
        point_2 = (x2, y2)
        cv2.line(img, point_1, point_2, (0, 0, 255), 2)

    return img


# Read image
img = cv2.imread('pics/film.png', cv2.COLOR_BGR2GRAY)
edged_img = cv2.Canny(img, 50, 200)
res = hough_transform(edged_img, 80)

plt.figure('Hough Space')
plt.imshow(res['accumulator'])
# plt.set_cmap('gray')
plt.show()

result = draw_line(img, res)
cv2.imshow("Result Image", result)
cv2.waitKey(0)
