#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-05-15 15:10
# @Author  : Gin (gin.lance.inside@hotmail.com)
# @Link    : 
# @Disc    : about Pillow Apis

from PIL import Image
import urllib.request,io
from base64 import b64encode
from os import urandom

#generates a sequence of bytes that will be converted to alphanumeric characters
byte_soup = urandom(64)
#converts the byte sequence to alphanumeric characters
alpha_soup = b64encode(byte_soup).decode("utf-8")
#generates a random, 7-digit alphanumeric string for the image name
image_name = alpha_soup[0:8]

def get_image(image_path):
    # if the image_path is a remote url, read the image at first
    if image_path.startswith("http://") or image_path.startswith("https://"):
        image_path = io.BytesIO(urllib.request.urlopen(image_path).read())

    image = Image.open(image_path)
    return image

def get_thumbnail(image):
    image.thumbnail((256, 256))
    return image

def get_colors(image_path):
    """ image instance
    """
    image = get_image(image_path)

    """ image thumbnail
        size: 256 * 256
        reduce the calculate time 
    """
    thumbnail = get_thumbnail(image)


    """ calculate the max colors the image cound have
        if the color is different in every pixel, the color counts may be the max.
        so : 
        max_colors = image.height * image.width
    """
    image_height = thumbnail.height
    image_width = thumbnail.width
    max_colors = image_height * image_width

    image_colors = image.getcolors(max_colors)
    return image_colors

def new_image(mode, size, color):
    """ generate a new color block
        to generate the palette
    """
    new_image = Image.new(mode, size, color)
    return new_image

def joint_image(images):
    """ generate the palette
        size: 50 x 400
        color_block_size: 50 x 50
    """
    palette = Image.new('RGB', (400, 20))

    # init the box position
    init_ul = 0

    for image in images:
        palette.paste(image, (init_ul, 0))
        init_ul += image.width

    #Saves the generated image as a jpeg file so that it may be uploaded to imgur
    palette.save(image_name, format="JPEG")
    #Closes the image after it has been opened by the palette.save() method
    palette.close()
