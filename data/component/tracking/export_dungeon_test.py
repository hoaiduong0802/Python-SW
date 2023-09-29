import sys
sys.path.append("./base")  

from _import import *

def activate_selected_window_and_run(nameActive):
    selected_app = nameActive  # Lấy giá trị được chọn trong danh sách
    app_windows = gw.getWindowsWithTitle(selected_app)

        # Lấy cửa sổ đầu tiên trong danh sách và kích hoạt nó
    app_window = app_windows[0]
    if not app_window.isActive:
        app_window.activate()

    # Chạy chương trình tìm kiếm ảnh
    search_result = search_image()
    if search_result:
        print("Tìm thấy ảnh, kết thúc vòng lặp.")
    else:
        print("Vòng lặp kết thúc mà không tìm thấy ảnh.")
def search_image():
    solan = 0
    source_image_path = 'data/img/battle/1920x1080/winAH_giant.png'
    
    while True:  # Sử dụng vòng lặp vô hạn
        # Các bước tìm kiếm ảnh giữ nguyên như trước
        app_window = gw.getActiveWindow()
        if app_window:
            app_left, app_top, app_width, app_height = app_window.left, app_window.top, app_window.width, app_window.height
            app_screenshot = pyautogui.screenshot(region=(app_left, app_top, app_width, app_height))
            app_screenshot = np.array(app_screenshot)
            source_image = cv2.imread(source_image_path)
            if source_image is not None:
                result = cv2.matchTemplate(app_screenshot, source_image, cv2.TM_CCOEFF_NORMED)
                threshold = 0.5
                min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
                if max_val >= threshold:
                    solan += 1
                    time.sleep(5)
                    print("Tìm thấy ảnh tại vị trí:", max_loc, "lần ", solan)
                    # return True  # Trả về True khi tìm thấy ảnh
            else:
                print(f"Không thể đọc tệp hình ảnh nguồn: {source_image_path}")
        time.sleep(1)  # Chờ 2 giây trước khi tìm kiếm lại
    return False  # Trả về False nếu không tìm thấy ảnh sau khi vòng lặp kết thúc (ít khi xảy ra)

activate_selected_window_and_run("Summoners War - MuMu Player")