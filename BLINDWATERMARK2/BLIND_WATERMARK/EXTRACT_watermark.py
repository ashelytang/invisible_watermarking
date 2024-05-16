# import os
# import cv2
# from blind_watermark import WaterMark

# def extract_watermarks(input_folder, output_folder, watermark_shape):
#     # Ensure the output folder exists
#     os.makedirs(output_folder, exist_ok=True)

#     # Initialize the WaterMark object for extraction
#     bwm = WaterMark(password_wm=1, password_img=1)

#     # Iterate over all images in the input folder
#     for filename in os.listdir(input_folder):
#         if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
#             file_path = os.path.join(input_folder, filename)
#             output_filename = f'sameSize_extract_{filename}'
#             output_path = os.path.join(output_folder, output_filename)

#             # Extract the watermark
#             extracted_wm = bwm.extract(filename=file_path, wm_shape=watermark_shape, out_wm_name=output_path, mode='img')

#             print(f'Extracted watermark saved to {output_path}')

# # Define your folders and watermark shape
# input_folder = 'examples/pic/test_embedded_og128x128'
# output_folder = 'examples/pic/extracted_128x128'
# watermark_shape = (128, 128)  # Example shape, adjust to your watermark's dimensions

# # Run the watermark extraction process
# extract_watermarks(input_folder, output_folder, watermark_shape)


fall 2023
import os
import cv2
from blind_watermark import WaterMark

def extract_watermarks(input_folder, output_folder, watermark_shape):
    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Initialize the WaterMark object for extraction
    bwm = WaterMark(password_wm=1, password_img=1)

    # Iterate over all images in the input folder
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            file_path = os.path.join(input_folder, filename)
            output_filename = f'sameSize_extract_{filename}'
            output_path = os.path.join(output_folder, output_filename)

            try:
                # Attempt to extract the watermark
                extracted_wm = bwm.extract(filename=file_path, wm_shape=watermark_shape, out_wm_name=output_path, mode='img')
                print(f'Extracted watermark saved to {output_path}')
            except Exception as e:
                # If an error occurs, skip this image and continue
                print(f'Could not extract watermark from {filename}: {e}')

# Define your folders and watermark shape
input_folder = 'examples/pic/test_embedded_og256x256'
output_folder = 'examples/pic/extracted_256x256'
watermark_shape = (256, 256)  # Example shape, adjust to your watermark's dimensions

# Run the watermark extraction process
extract_watermarks(input_folder, output_folder, watermark_shape)




