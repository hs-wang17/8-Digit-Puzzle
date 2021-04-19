from PIL import Image
import os


def cut_image(image_, M, N):
    width, height = image_.size
    item_width = int(width / N)
    item_height = int(height / M)
    box_list = []
    for i in range(0, M):
        for j in range(0, N):
            box = (j * item_width, i * item_height, (j + 1) * item_width, (i + 1) * item_height)
            box_list.append(box)
    image_list_ = [image_.crop(box) for box in box_list]
    return image_list_


def save_images(image_list_, rank):
    index = 0
    for image_ in image_list_:
        image_.save("temp/" + str(rank[index]) + '.jpg')
        index += 1




