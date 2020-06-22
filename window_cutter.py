"""
This file has the purpose of taking a photo, cutting it into windows,
then saving those photos
Author: Alex Sutay
"""


from PIL import Image
DEFAULT_HEIGHT = 100  # Height and width when main() is called
DEFAULT_WIDTH = 50


def main():
    filename = input("Where is the photo?")
    directory = input("Where should I save them?")
    print("Breaking it apart..")
    im = Image.open(filename)
    images = split(im, DEFAULT_HEIGHT, DEFAULT_WIDTH)
    for i in range(0, len(images)):
        images[i].save(directory + "\\" + str(i) + ".png", "PNG")
    im.close()
    print("done.")


def split(im, h, w):
    """
    Split a given Image object into smaller image objects
    :param im: the image object being split
    :param h: the height of each split
    :param w: the width of each split
    :return: a list of the new image objects
    """
    width, height = im.size
    width = width - width % w
    height = height - height % h
    rtn_list = []
    h = h//2  # The steps are half the size of the windows, so I reuse the size variables and simply half them
    w = w//2
    for x in range(w, width - w, w):
        for y in range(h, height - h, h):
            im_crop = im.crop((y - h, x - w, y + h, x + h))
            rtn_list.append(im_crop)
    return rtn_list


if __name__ == "__main__":
    main()
