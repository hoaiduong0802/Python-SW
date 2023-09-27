import sys
sys.path.append("base")
from _import import *
from tracking.export_dungeon import search_image

def action_mouseclick():
    autoit_exe_path = "C:\Program Files (x86)\AutoIt3\AutoIt3.exe"
    autoit_script = r"C:\Users\User\Desktop\Python-SW\data\component\handle_mouse\actionM.au3"

if search_image():
    action_mouseclick()
else:
    print("Fail")
