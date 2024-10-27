
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
import subprocess
start_time =datetime.now()

# Đường dẫn đến tesseract.exe (chỉ cần cho Windows)
with open('input.json', 'r') as f:
    config = json.load(f)
path_adb = config["adb_path"]
tesseract_path = config['tesseract_path']
pytesseract.pytesseract.tesseract_cmd = tesseract_path
def export_excel(list_rank, list_id, list_name, list_power, list_kill_points, list_t1_kills, list_t1_kills_points, list_t2_kills, list_t2_kills_points, list_t3_kills, list_t3_kills_points,list_t4_kills, list_t4_kills_points, list_t5_kills, list_t5_kills_points,list_dead):
    data = {
    'Rank': [],
    'ID': [],
    'Name': [],
    'Power': [],
    'Kill Points': [],
    'T1 Kills': [],
    'T1 Kills Points': [],
    'T2 Kills': [],
    'T2 Kills Points': [],
    'T3 Kills': [],
    'T3 Kills Points': [],
    'T4 Kills': [],
    'T4 Kills Points': [],
    'T5 Kills': [],
    'T5 Kills Points': [],
    'Dead': []
    }
    df = pd.DataFrame(data)
    new_data = pd.DataFrame({'Rank': list_rank, 'ID': list_id, 'Name': list_name, 'Power': list_power, 'Power': list_power, 'Kill Points': list_kill_points,  'T1 Kills': list_t1_kills, 'T1 Kills Points': list_t1_kills_points, 'T2 Kills': list_t2_kills, 'T2 Kills Points': list_t2_kills_points, 'T3 Kills': list_t3_kills, 'T3 Kills Points': list_t3_kills_points, 'T4 Kills': list_t4_kills, 'T4 Kills Points': list_t4_kills_points, 'T5 Kills': list_t5_kills, 'T5 Kills Points': list_t5_kills_points, 'Dead': list_dead})
    df = pd.concat([df, new_data], ignore_index=True)
    df.to_excel('./result.xlsx', index=False)

# Kết nối đến BlueStacks
try:
    subprocess.run([path_adb, "kill-server"], check=True)
    subprocess.run([path_adb, "start-server"], check=True)
    adb = AdbClient(host='127.0.0.1', port=5037)  # Đảm bảo sử dụng port 5037 cho ADB
    devices = adb.devices()  # Lấy danh sách thiết bị
    if devices:
        print("Thiết bị đã kết nối:", devices)
    else:
        print("Không tìm thấy thiết bị.")
except Exception as e:
    print(f"Có lỗi xảy ra: {e}")
    time.sleep(100)
device = devices[config["device"]]
 # Thay đổi ID thiết bị nếu cần
# Thời gian chờ để ứng dụng tải

# Đặt tọa độ mà bạn muốn nhấp
 # Thay đổi tọa độ Y

def go_to_rank(device,choice):
    try:
        time.sleep(1)
        x_coordinate = 37  # Thay đổi tọa độ X
        y_coordinate = 37 
        device.shell(f'input tap {x_coordinate} {y_coordinate}')
        
        time.sleep(1)
        x_rank = 300  # Thay đổi tọa độ X
        y_rank = 450
        device.shell(f'input tap {x_rank} {y_rank}')
        
        time.sleep(1)
        x_power_person = choice  # Thay đổi tọa độ X
        y_power_person = 300
        device.shell(f'input tap {x_power_person} {y_power_person}')
        time.sleep(1)
    except Exception as e:
        print(f"Có lỗi xảy ra khi nhấp: {e}")




def get_data_craw(device, rank):

    screenshot_id = device.screencap()  # Chụp ảnh màn hình 
    #(442, 116, 442 + 59, 116 + 18)
    id = convert_img_to_string(screenshot_id, 442, 116, 442+58, 116+18, "id",rank)
    power = convert_img_to_string(screenshot_id, 520, 197, 520+130, 197+25, "power", rank)
    kill_points = convert_img_to_string(screenshot_id, 670, 195, 670+140, 195+25, "kill_points", rank)
    next_profile =False
    if power =="" and kill_points =="":
        next_profile =True
        return "", "", "", "", "", "", "", "", "", "", "", "", "", "","", next_profile
    x_pro1_info1 = 670  # Thay đổi tọa độ X
    y_pro1_info1 = 190 
    device.shell(f'input tap {x_pro1_info1} {y_pro1_info1}')
    time.sleep(1.55)
    screenshot_ask_button = device.screencap()
    t1_kills = convert_img_to_string(screenshot_ask_button, 518, 258, 518+150, 258+15, "t1_kills", rank)
    t1_kills_points = convert_img_to_string(screenshot_ask_button, 755, 258, 750+100, 258+15, "t1_kills_points", rank)
    t2_kills = convert_img_to_string(screenshot_ask_button, 518, 283, 518+150, 283+15, "t2_kills", rank)
    t2_kills_points = convert_img_to_string(screenshot_ask_button, 755, 283, 750+100, 283+15, "t2_kills_points", rank)
    t3_kills = convert_img_to_string(screenshot_ask_button, 518, 311, 518+150, 311+15, "t3_kills", rank) 
    t3_kills_points = convert_img_to_string(screenshot_ask_button, 755, 311, 750+100, 311+15, "t3_kills_points", rank)
    t4_kills = convert_img_to_string(screenshot_ask_button, 518, 337, 518+150, 337+15, "t4_kills", rank)
    t4_kills_points = convert_img_to_string(screenshot_ask_button, 755, 337, 750+104, 337+17, "t4_kills_points", rank)
    t5_kills = convert_img_to_string(screenshot_ask_button, 518, 365, 518+100, 365+15, "t5_kills", rank)
    t5_kills_points = convert_img_to_string(screenshot_ask_button, 755, 365, 750+100, 365+15, "t5_kills_points", rank)
    x_pro1_info2 = 210  # Thay đổi tọa độ X
    y_pro1_info2 = 450
    device.shell(f'input tap {x_pro1_info2} {y_pro1_info2}')
   
    x_copy_name = 225  # Thay đổi tọa độ X
    y_copy_name = 93 
    time.sleep(1.5)
    device.shell(f'input tap {x_copy_name} {y_copy_name}')
    time.sleep(1.5)
    name = pyperclip.paste()
    print(name)
    pyperclip.copy('')
    screenshot_detail = device.screencap()
    dead = convert_img_to_string(screenshot_detail, 675, 265, 675+110, 265+21, "dead", rank)
    x_exit_pro_1 = 836  # Thay đổi tọa độ X
    y_exit_pro_1 = 32 
    device.shell(f'input tap {x_exit_pro_1} {y_exit_pro_1}')
    
    time.sleep(1.5)
    x_exit_pro_2 = 819  # Thay đổi tọa độ X
    y_exit_pro_2 = 62 
    device.shell(f'input tap {x_exit_pro_2} {y_exit_pro_2}')
    
    return id, name, power, kill_points,  t1_kills, t1_kills_points, t2_kills, t2_kills_points ,t3_kills, t3_kills_points, t4_kills, t4_kills_points, t5_kills, t5_kills_points,dead,next_profile
def convert_img_to_string(screenshot, x, y, w, h, identify, rank):
    with open('image/screenshot.png', 'wb') as f:
        f.write(screenshot)
    img = Image.open('image/screenshot.png')
    cropped_image = img.crop((x, y, w, h))
    cropped_image.save('image/screenshot.png')
    text = pytesseract.image_to_string(cropped_image)
    list_identity_kills = ["t1_kills","t2_kills","t3_kills","t4_kills","t5_kills"]
    if text == "":
        draw = ImageDraw.Draw(cropped_image)
        points = [(8, 7), (9, 7), (10, 7), (8, 8), (9, 8), (10, 8), (8, 9)]
        if identify in list_identity_kills:
            points = [(90, 8), (90, 7), (90, 6), (91, 8), (91, 7), (91, 6), (92, 8), (92, 7), (92, 6)]    
        for point in points:
            x, y = point
            draw.ellipse((x-2, y-2, x+2, y+2), fill='black')
        cropped_image.save('image/screenshot.png')
        text = pytesseract.image_to_string(cropped_image)
    if text =="":
        path =identify + str(rank)
        cropped_image.save(f'image/{path}.png')
        with open("./err.txt", 'a+', encoding='utf-8') as output_file:
                output_file.write(identify + str(rank))
    text_clean = re.sub(r'\D', '', text)
    print(text_clean)
    return text_clean
def move_to_stat_craw():
    x1, y1, x2, y2, duration = 340, 384.7, 340, 324.1, 3000
    device.shell(f"input swipe {x1} {y1} {x2} {y2} {duration}")
    #device.shell(f"input touchscreen  swipe {x2} {y2} {x2} {y2} 1000")
    time.sleep(2)
try:
    print("Tool By Nguyen Khac Hieu")
    print("Starting Tool....")
    
    specific_date = datetime(2060, 10, 26)
    today = datetime.now()
    if today > specific_date:
            print(f"This tool is expired!! Contact owner! telegram: https://t.me/hieunguyenkhac")
            raise Exception("This tool is expired!! Contact owner! telegram: https://t.me/hieunguyenkhac")
    
    input_choice = input("Nhập 1 để craw sức mạnh cá nhân \nNhập 2 để craw kĩ năng cá nhân \nNhập 3 để craw từ 1 vị trí trrong bảng xếp hạng \nLựa chọn:")
    if int(input_choice) == 1:
        choice=160
        go_to_rank(device,choice)
    elif int(input_choice) == 2:
        choice = 405
        go_to_rank(device,choice)
    elif int(input_choice) == 3:
        print("Tiến anh craw từ bảng xếp hạng hiện tại")    
    x_pro1 = 470  # Thay đổi tọa độ X
    y_pro1 = 170
    list_rank =[]
    list_id = []
    list_name = []
    list_power = []
    list_kill_points = []
    list_t1_kills = []
    list_t1_kills_points = []
    list_t2_kills = []
    list_t2_kills_points = []
    list_t3_kills = []
    list_t3_kills_points = []
    list_t4_kills = []
    list_t4_kills_points = []
    list_t5_kills = []
    list_t5_kills_points = []
    list_dead = []
    input_records = int(config['data_craw'])
   
    skip_profile_set = list(set(config["skip_profile"]))
    if int(input_choice) ==1 or int(input_choice) ==2:
        for i in range(input_records): 
            rank=i+1
            if i+1 in skip_profile_set and i <4:
                y_pro1 += 60
                continue
            if i >=4:
                y_pro1=360
                if i+1 in skip_profile_set:
                    move_to_stat_craw()
                    rank=i+1
                    continue   
            device.shell(f'input tap {x_pro1} {y_pro1}')
            print("Đã nhấp vào profile")
            time.sleep(1.5)
            
            id, name, power, kill_points, t1_kills, t1_kills_points, t2_kills, t2_kills_points ,t3_kills, t3_kills_points, t4_kills, t4_kills_points, t5_kills, t5_kills_points, dead,next_profile = get_data_craw(device,rank)
            if next_profile:
                move_to_stat_craw()
                rank+=1
                continue    
            list_rank.append(rank)
            list_id.append(id)
            list_name.append(name)
            list_power.append(power)
            list_kill_points.append(kill_points)
            list_t1_kills.append(t1_kills)
            list_t1_kills_points.append(t1_kills_points)
            list_t2_kills.append(t2_kills)
            list_t2_kills_points.append(t2_kills_points)
            list_t3_kills.append(t3_kills)
            list_t3_kills_points.append(t3_kills_points)
            list_t4_kills.append(t4_kills)
            list_t4_kills_points.append(t4_kills_points)
            list_t5_kills.append(t5_kills)
            list_t5_kills_points.append(t5_kills_points)
            list_dead.append(dead)
            y_pro1 += 60
            time.sleep(2)
    elif int(input_choice) ==3:
        start_rank = input("Nhập vị trí rank bắt đầu\nLựa chọn:")
        for i in range(int(start_rank),input_records): 
            rank=i
            y_pro1=360
            if i in skip_profile_set:
                move_to_stat_craw()
                rank=i+1
                continue    
            device.shell(f'input tap {x_pro1} {y_pro1}')
            print("Đã nhấp vào profile")
            time.sleep(1.5)
            
            id, name, power, kill_points, t1_kills, t1_kills_points, t2_kills, t2_kills_points ,t3_kills, t3_kills_points, t4_kills, t4_kills_points, t5_kills, t5_kills_points, dead, next_profile = get_data_craw(device, rank)
            if next_profile:
                move_to_stat_craw()
                rank+=1
                continue
            list_rank.append(rank)
            list_id.append(id)
            list_name.append(name)
            list_power.append(power)
            list_kill_points.append(kill_points)
            list_t1_kills.append(t1_kills)
            list_t1_kills_points.append(t1_kills_points)
            list_t2_kills.append(t2_kills)
            list_t2_kills_points.append(t2_kills_points)
            list_t3_kills.append(t3_kills)
            list_t3_kills_points.append(t3_kills_points)
            list_t4_kills.append(t4_kills)
            list_t4_kills_points.append(t4_kills_points)
            list_t5_kills.append(t5_kills)
            list_t5_kills_points.append(t5_kills_points)
            list_dead.append(dead)
            y_pro1 += 60
            time.sleep(2)
    export_excel(list_rank, list_id, list_name, list_power, list_kill_points, list_t1_kills, list_t1_kills_points, list_t2_kills, list_t2_kills_points, list_t3_kills, list_t3_kills_points,list_t4_kills, list_t4_kills_points, list_t5_kills, list_t5_kills_points,list_dead)
    end_time = datetime.now() 
    result_time = end_time - start_time
    print(f"THời gian hoàn thành {result_time}")
    time.sleep(100)
except Exception as e:
    print(e)
    time.sleep(100)