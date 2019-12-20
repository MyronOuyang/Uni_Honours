from PIL import Image as img
import os


def main():

    bird = open_image("../pics/bird.png")
    # coins = open_image("../pics/coins.png")
    # film = open_image("../pics/film.png")
    # lena = open_image("../pics/lena.png")
    # star = open_image("../pics/star.png")

    print_img(bird)
    # print_img(coins)
    # print_img(film)
    # print_img(lena)
    # print_img(star)


def print_img(image):

    f = threshold(image, 65)
    f.show()

    eroded = erode_pixels(f)
    eroded.show()

    dilated = dilate_pixels(f)
    dilated.show()

    edge_img = diff(f, eroded)
    edge_img.show()
    edge_img = diff(f, dilated)
    edge_img.show()


def dilate_pixels(f):

    WHITE = 255

    def update(results, coords):
        BOUNDARY = -1

        x0 = (coords[0] - 1, coords[1])
        x1 = (coords[0] + 1, coords[1])
        x2 = (coords[0], coords[1] - 1)
        x3 = (coords[0], coords[1] + 1)

        if (BOUNDARY not in x0) and (f.size[0] not in x0):
            results[x0[0], x0[1]] = WHITE

        if (BOUNDARY not in x1) and (f.size[0] not in x1):
            results[x1[0], x1[1]] = WHITE

        if (BOUNDARY not in x2) and (f.size[1] not in x2):
            results[x2[0], x2[1]] = WHITE

        if (BOUNDARY not in x3) and (f.size[1] not in x3):
            results[x3[0], x3[1]] = WHITE

    image = img.new(f.mode, f.size)
    results = image.load()
    M, N = image.size[0], image.size[1]

    for m in range(M):
        for n in range(N):
            test = image.getpixel((m, n))[0]
            if test == WHITE:
                update(results, (m, n))
    
    return image

def erode_pixels(f):

    WHITE = 255
    BLACK = 0

    def check(coords):
        BOUNDARY = -1

        x0 = (coords[0] - 1, coords[1])
        x1 = (coords[0] + 1, coords[1])
        x2 = (coords[0], coords[1] - 1)
        x3 = (coords[0], coords[1] + 1)

        passed = True
        
        if not((BOUNDARY not in x0) and (f.size[0] not in x0) and (f.getpixel(x0)[0] == WHITE)):
            passed = False

        if not((BOUNDARY not in x1) and (f.size[0] not in x1) and (f.getpixel(x1)[0] == WHITE)):
            passed = False

        if not((BOUNDARY not in x2) and (f.size[1] not in x2) and (f.getpixel(x2)[0] == WHITE)):
            passed = False

        if not((BOUNDARY not in x3) and (f.size[1] not in x3) and (f.getpixel(x3)[0] == WHITE)):
            passed = False

        return passed

    image = img.new(f.mode, f.size)
    results = image.load()
    M, N = image.size[0], image.size[1]

    for m in range(M):
        for n in range(N):
            coords = (m, n)
            if check(coords):
                results[m, n] = WHITE
            else:
                results[m, n] = BLACK

    return image

def threshold(f, mininum_threshold):

    WHITE = 255
    BLACK = 0

    f_Map = f.load()
    image = img.new(f.mode, f.size)
    M, N = image.size[0], image.size[1]

    results = image.load()

    for m in range(M):
        for n in range(N):
            test = f_Map[m, n][0]
            if test > mininum_threshold:
                results[m, n] = WHITE 
            else:
                results[m, n] = BLACK

    return image

def diff(f, f2):

    WHITE = 255
    BLACK = 0

    image = img.new(f.mode, f.size)
    results = image.load()
    M, N = image.size[0], image.size[1]

    for m in range(M):
        for n in range(N):
            pixel1 = f.getpixel((m, n))
            pixel2 = f2.getpixel((m, n))
            if pixel1 != pixel2:
                results[m, n] = BLACK
            else:
                results[m, n] = WHITE

    return image

def open_image(path):
    
    current_path = os.path.abspath(os.path.dirname(__file__))
    image_path = os.path.normpath(current_path + "/" + path)

    if not(os.path.exists(image_path)):
        raise FileNotFoundError(f"File at path: '{image_path}' does not exist")

    image = img.open(image_path)
    image = image.convert("LA")
    image.show()

    return image

if __name__ == "__main__":
    main()