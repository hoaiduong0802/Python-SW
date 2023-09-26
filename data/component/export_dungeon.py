import sys
sys.path.append("./base")  

from _import import *

def search_image():
    source_image_path = 'data/img/battle/1366x768/winAH_giant.png'
    app_name = 'Summoners War - MuMu Player'

    endP_1 = False  # Biến đánh dấu xem vòng lặp đã kết thúc chưa

    while not endP_1:
        app_window = gw.getWindowsWithTitle(app_name)
        if app_window:
            app_window[0].activate()  
            app_left, app_top, app_width, app_height = app_window[0].left, app_window[0].top, app_window[0].width, app_window[0].height
            app_screenshot = pyautogui.screenshot(region=(app_left, app_top, app_width, app_height))
            app_screenshot = np.array(app_screenshot)
            try:
                source_image = cv2.imread(source_image_path)
                if source_image is not None:
                    result = cv2.matchTemplate(app_screenshot, source_image, cv2.TM_CCOEFF_NORMED)
                    threshold = 0.5
                    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
                    if max_val >= threshold:
                        print("Tìm thấy ảnh tại vị trí:", max_loc)
                        endP_1 = True  # Kết thúc vòng lặp
                    else:
                        print("Không tìm thấy ảnh.")
                else:
                    print(f"Không thể đọc tệp hình ảnh nguồn: {source_image_path}")
            except Exception as e:
                print(f"Lỗi khi thực hiện so sánh hình ảnh: {e}")
        else:
            print(f"Không tìm thấy cửa sổ ứng dụng: {app_name}")

        time.sleep(2)  # Chờ 2 giây trước khi tìm kiếm lại

    return endP_1

# Gọi hàm để thực hiện tìm kiếm
search_result = search_image()
if search_result:
    print("Tìm thấy ảnh, kết thúc vòng lặp.")
else:
    print("Vòng lặp kết thúc mà không tìm thấy ảnh.")
