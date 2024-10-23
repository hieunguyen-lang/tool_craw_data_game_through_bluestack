import pytesseract
from PIL import Image

# Đường dẫn đến tesseract.exe (chỉ cần cho Windows)
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Admin\Documents\tool\tool_craw_data_game_through_bluestack\tesseract.exe'

# Mở ảnh chụp màn hình
img = Image.open('screenshot.png')

# Sử dụng pytesseract để lấy text
text = pytesseract.image_to_string(img)

# In ra text đã lấy được
print(text)
