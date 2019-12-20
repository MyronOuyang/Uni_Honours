from PIL import Image, ImageDraw
from math import sqrt, pi, cos, sin
from collections import defaultdict
import cv2
import numpy as np


def hough_circle(img, threshold):
    # Load image:
    input_image = Image.open("../pics/coins.png")

    # Output image:
    output_image = Image.new("RGB", input_image.size)
    output_image.paste(input_image)
    draw_result = ImageDraw.Draw(output_image)
    # Find circles
    rmin = 18
    rmax = 50

    accumulator = defaultdict(int)
    # accumulator = np.zeros((500, 500, 360))
    points = []
    theta_arr = np.deg2rad(np.arange(0.0, 180.0))

    for r in range(rmin, rmax + 1):
        for theta in theta_arr:
            points.append((r, int(r * np.cos(theta)), int(r * np.sin(theta))))

    y_edges, x_edges = np.nonzero(img)  # (row, col) indexes to edges
    for i in range(len(x_edges)):
        x = x_edges[i]
        y = y_edges[i]
        for r, dx, dy in points:
            a = x - dx
            b = y - dy
            accumulator[(a, b, r)] += 1

    circles = []
    for k, v in sorted(accumulator.items(), key=lambda i: -i[1]):
        x, y, r = k
        if v >= threshold:
            circles.append((x, y, r))

    for x, y, r in circles:
        draw_result.ellipse((x - r, y - r, x + r, y + r), outline=(255, 0, 0, 0))

    output_image.show()


ma_image = cv2.imread('../pics/coins.png', cv2.COLOR_BGR2GRAY)
edged_img = cv2.Canny(ma_image, 50, 200)

hough_circle(edged_img, 120)
