from PIL import Image


def threshold(ori_img, threshold_val):
    pixelMap = ori_img.load()
    img = Image.new(im.mode, im.size)
    pixelsNew = img.load()
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            if pixelMap[i, j][0] > threshold_val:
                pixelsNew[i, j] = 255  # white
            else:
                pixelsNew[i, j] = 0  # black
    return img


def erode(img):
    def check(pos):
        left = (pos[0] - 1, pos[1])
        right = (pos[0] + 1, pos[1])
        bottom = (pos[0], pos[1] - 1)
        top = (pos[0], pos[1] + 1)

        left_check = False
        right_check = False
        bottom_check = False
        top_check = False
        if -1 not in left and img.size[0] not in left and img.getpixel(left)[0] == 255:
            left_check = True
        if -1 not in right and img.size[0] not in right and img.getpixel(right)[0] == 255:
            right_check = True
        if -1 not in bottom and img.size[1] not in bottom and img.getpixel(bottom)[0] == 255:
            bottom_check = True
        if -1 not in top and img.size[1] not in top and img.getpixel(top)[0] == 255:
            top_check = True

        return left_check and right_check and bottom_check and top_check

    new_img = Image.new(im.mode, im.size)
    pixelsNew = new_img.load()
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            if check((i, j)):
                pixelsNew[i, j] = 255  # white
            else:
                pixelsNew[i, j] = 0  # black
    return new_img


def dilate(img):
    def update(pixelsNew, pos):
        left = (pos[0] - 1, pos[1])
        right = (pos[0] + 1, pos[1])
        bottom = (pos[0], pos[1] - 1)
        top = (pos[0], pos[1] + 1)

        if -1 not in left and img.size[0] not in left:
            pixelsNew[left[0], left[1]] = 255
        if -1 not in right and img.size[0] not in right:
            pixelsNew[right[0], right[1]] = 255
        if -1 not in bottom and img.size[1] not in bottom:
            pixelsNew[bottom[0], bottom[1]] = 255
        if -1 not in top and img.size[1] not in top:
            pixelsNew[top[0], top[1]] = 255

    new_img = Image.new(im.mode, im.size)
    pixelsNew = new_img.load()
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            if img.getpixel((i, j))[0] == 255:
                update(pixelsNew, (i, j))
    return new_img


def diff(ori_img, altered_img):
    img = Image.new(im.mode, im.size)
    pixelsNew = img.load()
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            if ori_img.getpixel((i, j)) != altered_img.getpixel((i, j)):
                pixelsNew[i, j] = 0  # white
            else:
                pixelsNew[i, j] = 255  # black
    return img


im = Image.open('pics/lena.png')
im = im.convert('LA')
im.show()
binary_img = threshold(im, 80)
binary_img.show()

eroded_img = erode(binary_img)
eroded_img.show()

dilated_img = dilate(binary_img)
dilated_img.show()

edge_img = diff(binary_img, eroded_img)
edge_img.show()
edge_img = diff(binary_img, dilated_img)
edge_img.show()


# img.save("out.tif")
im.close()
