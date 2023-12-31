# import os
# import cv2
# from blind_watermark import WaterMark

# def watermark_images(input_folder, output_folder, watermark_image):
#     # Ensure the output folder exists
#     os.makedirs(output_folder, exist_ok=True)

#     # Initialize the WaterMark object
#     bwm = WaterMark(password_wm=1, password_img=1)

#     # Read the watermark
#     bwm.read_wm(watermark_image, mode='img')

#     # Iterate over all images in the input folder
#     for filename in os.listdir(input_folder):
#         if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
#             file_path = os.path.join(input_folder, filename)
#             base_name = os.path.splitext(filename)[0]  # Extracts the base name without extension
#             output_filename = f'watermarked_p_{base_name}.png'  # Ensures the output is a PNG file
#             output_path = os.path.join(output_folder, output_filename)

#             # Embed the watermark
#             bwm.read_img(file_path)
#             bwm.embed(output_path)

#             print(f'Watermarked image saved to {output_path}')

# # Define your folders and watermark image
# input_folder = 'examples/pic/test_wm'
# output_folder = 'examples/pic/test_embedded_og128x128'
# watermark_image = 'examples/pic/qr_resized128x128.png'

# # Run the watermarking process
# watermark_images(input_folder, output_folder, watermark_image)

import os
import cv2
from blind_watermark import WaterMark

def watermark_images(input_folder, output_folder, watermark_image):
    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Initialize the WaterMark object
    bwm = WaterMark(password_wm=1, password_img=1)

    # Read the watermark
    bwm.read_wm(watermark_image, mode='img')

    # Iterate over all images in the input folder
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            file_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, f'watermarked_{filename}')

            try:
                # Attempt to embed the watermark
                bwm.read_img(file_path)
                bwm.embed(output_path)
                print(f'Watermarked image saved to {output_path}')
            except Exception as e:
                # If an error occurs, skip this image and continue
                print(f'Could not embed watermark in {filename}: {e}')

# Define your folders and watermark image
input_folder = 'examples/pic/test_wm'
output_folder = 'examples/pic/test_embedded_og256x256'
watermark_image = 'examples/pic/qr_resized256x256.png'

# Run the watermarking process
watermark_images(input_folder, output_folder, watermark_image)

