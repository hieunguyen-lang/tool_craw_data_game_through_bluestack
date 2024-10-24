
import time
from ppadb.client import Client as AdbClient
import pytesseract
from PIL import Image,ImageDraw
import pandas as pd
import pyperclip
from datetime import datetime
import re
import json
import os
start_time =datetime.now()
# Đường dẫn đến tesseract.exe (chỉ cần cho Windows)
with open('input.json', 'r') as f:
    config = json.load(f)
tesseract_path = config['tesseract_path']
pytesseract.pytesseract.tesseract_cmd = tesseract_path
def export_excel(list_rank, list_id, list_name, list_power, list_kill_points,list_t4_kills, list_t4_kills_points, list_t5_kills, list_t5_kills_points,list_dead):
    data = {
    'Rank': [],
    'ID': [],
    'Name': [],
    'Power': [],
    'Kill Points': [],
    'T4 Kills': [],
    'T4 Kills Points': [],
    'T5 Kills': [],
    'T5 Kills Points': [],
    'Dead': []
    }
    df = pd.DataFrame(data)
    new_data = pd.DataFrame({'Rank': list_rank, 'ID': list_id, 'Name': list_name, 'Power': list_power, 'Power': list_power, 'Kill Points': list_kill_points, 'T4 Kills': list_t4_kills, 'T4 Kills Points': list_t4_kills_points, 'T5 Kills': list_t5_kills, 'T5 Kills Points': list_t5_kills_points, 'Dead': list_dead})
    df = pd.concat([df, new_data], ignore_index=True)
    df.to_excel('./result.xlsx', index=False)

# Kết nối đến BlueStacks
try:
    adb = AdbClient(host='127.0.0.1', port=5037)  # Đảm bảo sử dụng port 5037 cho ADB
    devices = adb.devices()  # Lấy danh sách thiết bị
    if devices:
        print("Thiết bị đã kết nối:", devices)
    else:
        print("Không tìm thấy thiết bị.")
except Exception as e:
    print(f"Có lỗi xảy ra: {e}")
device = devices[0]
 # Thay đổi ID thiết bị nếu cần
# Thời gian chờ để ứng dụng tải

# Đặt tọa độ mà bạn muốn nhấp
 # Thay đổi tọa độ Y

def go_to_rank(device):
    try:
        x_coordinate = 37  # Thay đổi tọa độ X
        y_coordinate = 37 
        device.shell(f'input tap {x_coordinate} {y_coordinate}')
        
        time.sleep(1)
        x_rank = 300  # Thay đổi tọa độ X
        y_rank = 450
        device.shell(f'input tap {x_rank} {y_rank}')
        
        time.sleep(1)
        x_power_person = 160  # Thay đổi tọa độ X
        y_power_person = 300
        device.shell(f'input tap {x_power_person} {y_power_person}')
        time.sleep(1)
    except Exception as e:
        print(f"Có lỗi xảy ra khi nhấp: {e}")




def get_data_craw(device):

    screenshot_id = device.screencap()  # Chụp ảnh màn hình 
    #(442, 116, 442 + 59, 116 + 18)
    id = convert_img_to_string(screenshot_id, 442, 116, 442+58, 116+18)
    power = convert_img_to_string(screenshot_id, 520, 197, 520+130, 197+25)
    kill_points = convert_img_to_string(screenshot_id, 670, 195, 670+140, 195+25)

    x_pro1_info1 = 670  # Thay đổi tọa độ X
    y_pro1_info1 = 190 
    device.shell(f'input tap {x_pro1_info1} {y_pro1_info1}')
    time.sleep(1)
    screenshot_ask_button = device.screencap()
    t4_kills = convert_img_to_string(screenshot_ask_button, 518, 337, 518+150, 337+15)
    t4_kills_points = convert_img_to_string(screenshot_ask_button, 755, 337, 750+104, 337+17)
    t5_kills = convert_img_to_string(screenshot_ask_button, 518, 365, 518+100, 365+15)
    t5_kills_points = convert_img_to_string(screenshot_ask_button, 755, 365, 750+100, 365+15)
    x_pro1_info2 = 210  # Thay đổi tọa độ X
    y_pro1_info2 = 450
    device.shell(f'input tap {x_pro1_info2} {y_pro1_info2}')
   
    x_copy_name = 225  # Thay đổi tọa độ X
    y_copy_name = 93 
    time.sleep(1)
    device.shell(f'input tap {x_copy_name} {y_copy_name}')
    time.sleep(1)
    name = pyperclip.paste()
    print(name)
    pyperclip.copy('')
    screenshot_detail = device.screencap()
    dead = convert_img_to_string(screenshot_detail, 675, 265, 675+110, 265+21)
    x_exit_pro_1 = 836  # Thay đổi tọa độ X
    y_exit_pro_1 = 32 
    device.shell(f'input tap {x_exit_pro_1} {y_exit_pro_1}')
    
    time.sleep(1)
    x_exit_pro_2 = 819  # Thay đổi tọa độ X
    y_exit_pro_2 = 62 
    device.shell(f'input tap {x_exit_pro_2} {y_exit_pro_2}')
    
    return id, name, power, kill_points,t4_kills, t4_kills_points, t5_kills, t5_kills_points,dead
def convert_img_to_string(screenshot, x, y, w, h):
    with open('image/screenshot.png', 'wb') as f:
        f.write(screenshot)
    img = Image.open('image/screenshot.png')
    cropped_image = img.crop((x, y, w, h))
    cropped_image.save('image/screenshot.png')
    text = pytesseract.image_to_string(cropped_image)
    if text == "":
        draw = ImageDraw.Draw(cropped_image)
        points = [(8, 7), (9, 7), (10, 7), (8, 8), (9, 8), (10, 8), (8, 9)]
        for point in points:
            x, y = point
            draw.ellipse((x-2, y-2, x+2, y+2), fill='black')
        cropped_image.save('image/screenshot.png')
        text = pytesseract.image_to_string(cropped_image)
    text_clean = re.sub(r'\D', '', text)
    print(text_clean)
    return text_clean

try:
    go_to_rank(device)
    x_pro1 = 470  # Thay đổi tọa độ X
    y_pro1 = 170
    list_rank =[]
    list_id = []
    list_name = []
    list_power = []
    list_kill_points = []
    list_t4_kills = []
    list_t4_kills_points = []
    list_t5_kills = []
    list_t5_kills_points = []
    list_dead = []
    input_records = int(config['data_craw'])
    for i in range(input_records):
        if i >=4:
            y_pro1=360
        device.shell(f'input tap {x_pro1} {y_pro1}')
        print("Đã nhấp vào profile")
        time.sleep(1)

        id, name, power, kill_points, t4_kills, t4_kills_points, t5_kills, t5_kills_points, dead = get_data_craw(device)
        list_rank.append(i+1)
        list_id.append(id)
        list_name.append(name)
        list_power.append(power)
        list_kill_points.append(kill_points)
        list_t4_kills.append(t4_kills)
        list_t4_kills_points.append(t4_kills_points)
        list_t5_kills.append(t5_kills)
        list_t5_kills_points.append(t5_kills_points)
        list_dead.append(dead)
        y_pro1 += 60
        time.sleep(2)
    export_excel(list_rank, list_id, list_name, list_power, list_kill_points,list_t4_kills, list_t4_kills_points, list_t5_kills, list_t5_kills_points,list_dead)
    end_time = datetime.now() 
    result_time = end_time - start_time
    print(f"THời gian hoàn thành {result_time}")
except Exception as e:
    export_excel(list_rank, list_id, list_name, list_power, list_kill_points,list_t4_kills, list_t4_kills_points, list_t5_kills, list_t5_kills_points,list_dead)
    print(f"Có lỗi xảy ra khi nhấp: {e}")