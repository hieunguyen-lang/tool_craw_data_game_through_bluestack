import pytesseract
from PIL import Image
# Đường dẫn đến tesseract.exe (chỉ cần cho Windows)
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Admin\Documents\tool\tool_craw_data_game_through_bluestack\tesseract.exe'

img = Image.open('test2.png')

text = pytesseract.image_to_string(img)

    # In ra text đã lấy được
print(text)
