import pytesseract
from PIL import Image
import cv2
import numpy as np
# Đường dẫn đến tesseract.exe (chỉ cần cho Windows)
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Admin\Documents\tool\tool_craw_data_game_through_bluestack\tesseract.exe'
class
image = cv2.imread('t1_kills_points81.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, binary = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

blurred = cv2.GaussianBlur(binary, (5, 5), 0)
processed_image_1 = Image.fromarray(blurred)

width, height = processed_image_1.size
scale_percent = 150  # Phóng to 150%

# Calculate new dimensions
new_width = int(width * scale_percent / 100)
new_height = int(height * scale_percent / 100)

# Resize the image using OpenCV
resized_image = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_LINEAR)
processed_image = Image.fromarray(resized_image)

custom_config = r'--oem 3 --psm 6 -c tessedit_char_whitelist=0123456789'
processed_image.save('processed_image.png')

text = pytesseract.image_to_string(processed_image, config=custom_config)

    # In ra text đã lấy được
print(text)
