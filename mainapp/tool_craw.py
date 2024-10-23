
import time
from ppadb.client import Client as AdbClient

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
        print("Đã nhấp vào tọa độ:", x_coordinate, y_coordinate)

        x_rank = 300  # Thay đổi tọa độ X
        y_rank = 450
        device.shell(f'input tap {x_rank} {y_rank}')
        print("Đã nhấp vào tọa độ:", x_rank, y_rank)

        x_power_person = 160  # Thay đổi tọa độ X
        y_power_person = 300
        device.shell(f'input tap {x_power_person} {y_power_person}')
        print("Đã nhấp vào tọa độ:", x_power_person, y_power_person)
    except Exception as e:
        print(f"Có lỗi xảy ra khi nhấp: {e}")

#go_to_rank(device)


try:
    x_pro1 = 470  # Thay đổi tọa độ X
    y_pro1 = 170 
    device.shell(f'input tap {x_pro1} {y_pro1}')
    print("Đã nhấp vào tọa độ:", x_pro1, y_pro1)
    time.sleep(1)

    x_pro1_info1 = 670  # Thay đổi tọa độ X
    y_pro1_info1 = 190 
    device.shell(f'input tap {x_pro1_info1} {y_pro1_info1}')
    print("Đã nhấp vào tọa độ:", x_pro1_info1, y_pro1_info1)

    x_pro1_info2 = 210  # Thay đổi tọa độ X
    y_pro1_info2 = 450 
    device.shell(f'input tap {x_pro1_info2} {y_pro1_info2}')
    print("Đã nhấp vào tọa độ:", x_pro1_info2, y_pro1_info2)
except Exception as e:
    print(f"Có lỗi xảy ra khi nhấp: {e}")