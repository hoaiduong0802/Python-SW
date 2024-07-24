import sys
sys.path.append("./base")  

from _import import *

def activate_selected_window_and_run():
    selected_app = app_listbox.get()  # Lấy giá trị được chọn trong danh sách
    app_windows = gw.getWindowsWithTitle(selected_app)
    
    if app_windows:
        # Lấy cửa sổ đầu tiên trong danh sách và kích hoạt nó
        app_window = app_windows[0]
        if not app_window.isActive:
            app_window.activate()
        app_label.config(text=f"Đã kích hoạt cửa sổ: {selected_app}")
        
        # Tắt cửa sổ select box
        root.withdraw()
        
        # Chạy chương trình tìm kiếm ảnh
        search_result = search_image()
        if search_result:
            print("Tìm thấy ảnh, kết thúc vòng lặp.")
        else:
            print("Vòng lặp kết thúc mà không tìm thấy ảnh.")
    else:
        app_label.config(text=f"Không tìm thấy cửa sổ: {selected_app}")

def search_image():
    source_image_path = 'data/img/battle/1366x768/winAH_giant.png'
    
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
                    print("Tìm thấy ảnh tại vị trí:", max_loc)
                    action_mouseclick()
                    return True  # Trả về True khi tìm thấy ảnh
            else:
                print(f"Không thể đọc tệp hình ảnh nguồn: {source_image_path}")
        else:
            print("Không có cửa sổ ứng dụng nào đang hoạt động.")

        time.sleep(2)  # Chờ 2 giây trước khi tìm kiếm lại

    return False  # Trả về False nếu không tìm thấy ảnh sau khi vòng lặp kết thúc (ít khi xảy ra)

def action_mouseclick():
    autoit_exe_path = "C:\\Program Files (x86)\\AutoIt3\\AutoIt3.exe"
    autoit_script = r"C:\Users\User\Desktop\Python-SW\data\component\handle_mouse\progrEle.au3"
    
    # Thực thi mã AutoIt bằng subprocess
    subprocess.run([autoit_exe_path, autoit_script])



# Tạo cửa sổ giao diện
root = tk.Tk()
root.title("Chọn cửa sổ ứng dụng")
root.geometry("300x200")

# Tạo danh sách chọn
app_label = tk.Label(root, text="Chọn cửa sổ ứng dụng:")
app_label.pack(pady=10)

# Lấy danh sách các cửa sổ đang mở
open_windows = [win.title for win in gw.getAllWindows() if win.title]

# Tạo danh sách chọn từ danh sách các cửa sổ đang mở
app_listbox = ttk.Combobox(root, values=open_windows)
app_listbox.pack(pady=10)

# Đặt giá trị mặc định nếu có cửa sổ đang mở
if open_windows:
    app_listbox.set(open_windows[0])

# Tạo nút kích hoạt
activate_button = tk.Button(root, text="Kích hoạt cửa sổ và chạy", command=activate_selected_window_and_run)
activate_button.pack()

# Khởi động giao diện
root.mainloop()