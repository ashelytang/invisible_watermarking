import subprocess
from PIL import Image
import os

def resize_watermark(watermark_path, desired_size=(64, 64)):
    """Resize the watermark image to the desired size."""
    with Image.open(watermark_path) as img:
        if img.size != desired_size:
            img = img.resize(desired_size, Image.ANTIALIAS)
            img.save(watermark_path)  # Overwrite the original watermark image

# Your watermark image path
watermark_path = 'pic/wm.png'

# Resize the watermark to 64x64 if necessary
resize_watermark(watermark_path)

# Set the directory containing your images
image_directory = 'path/to/your/image/folder'

# Path to the watermark image
watermark_path = 'pic/wm.png'

# Set the directories for saving the watermarked and extracted watermark images
watermarked_images_directory = 'path/to/watermarked/image/folder'
extracted_watermarks_directory = 'path/to/extracted/watermark/folder'

# Ensure that the output directories exist
os.makedirs(watermarked_images_directory, exist_ok=True)
os.makedirs(extracted_watermarks_directory, exist_ok=True)

# Iterate over the files in the directory
for filename in os.listdir(image_directory):
    if filename.endswith('.png'):  # assuming you're only processing PNG images
        # Construct the full file path
        file_path = os.path.join(image_directory, filename)

        # Create unique names for the watermarked and extracted watermark images
        watermarked_image_path = os.path.join(watermarked_images_directory, f"watermarked_{filename}")
        extracted_watermark_path = os.path.join(extracted_watermarks_directory, f"extracted_wm_{filename}")

        # Embed watermark
        embed_command = [
            'python', 'bwm.py', '-k', '4399', '2333', '32', '-em', '-r', file_path, 
            '-wm', watermark_path, '-o', watermarked_image_path, '-s'
        ]
        subprocess.run(embed_command)

        # Extract watermark
        extract_command = [
            'python', 'bwm.py', '-k', '4399', '2333', '32', '-ex', '-r', watermarked_image_path, 
            '-wm', watermark_path, '-ws', '64', '64', '-o', extracted_watermark_path, '-s'
        ]
        subprocess.run(extract_command)

print("Processing completed.")
