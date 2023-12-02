#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cv2

from blind_watermark import WaterMark
import os

from PIL import Image

# os.chdir(os.path.dirname(__file__))
# bwm = WaterMark(password_wm=1, password_img=1)
# # 读取原图
# bwm.read_img(filename='pic/ori_img.jpeg')
# # 读取水印
# bwm.read_wm('pic/watermark.png')
# # 打上盲水印
# bwm.embed('output/embedded.png')
# wm_shape = cv2.imread('pic/watermark.png', flags=cv2.IMREAD_GRAYSCALE).shape

# # %% 解水印


# bwm1 = WaterMark(password_wm=1, password_img=1)
# # 注意需要设定水印的长宽wm_shape
# bwm1.extract('output/embedded.png', wm_shape=wm_shape, out_wm_name='output/wm_extracted.png', mode='img')



os.chdir(os.path.dirname(__file__))
bwm = WaterMark(password_wm=1, password_img=1)
bwm.read_img(filename='pic/baby_photo.png')
bwm.read_wm('pic/watermark.png')
bwm.embed('output/baby_photo_embedded.png')
wm_shape = cv2.imread('pic/watermark.png', flags=cv2.IMREAD_GRAYSCALE).shape


bwm1 = WaterMark(password_wm=1, password_img=1)
bwm1.extract('output/baby_photo_embedded.png', wm_shape=wm_shape, out_wm_name='output/watermark_extracted2.png', mode='img')


# def resize_image(image_path, output_size=(32, 32)):
#     """Resize the image to the specified size."""
#     with Image.open(image_path) as img:
#         resized_img = img.resize(output_size, Image.Resampling.LANCZOS)  # Updated resampling method
#         resized_img.save(image_path)

# # Change directory to the script's directory
# os.chdir(os.path.dirname(__file__))

# # Resize the watermark image
# watermark_path = 'pic/rune.jpg'
# resize_image(watermark_path)

# # Embed watermark
# bwm = WaterMark(password_wm=1, password_img=1)
# bwm.read_img(filename='pic/baby_photo.png')
# bwm.read_wm(watermark_path)
# bwm.embed('output/baby_photo_embedded.png')

# # Read the shape of the watermark for extraction
# wm_shape = cv2.imread(watermark_path, flags=cv2.IMREAD_GRAYSCALE).shape

# # Extract watermark
# bwm1 = WaterMark(password_wm=1, password_img=1)
# bwm1.extract('output/baby_photo_embedded.png', wm_shape=wm_shape, out_wm_name='output/rune_extracted.png', mode='img')