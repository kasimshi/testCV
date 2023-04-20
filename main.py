<<<<<<< HEAD
import os
import subprocess
import cv2
import time

# 获取 PATH 环境变量的值
path = os.environ.get("PATH")

# 将新目录添加到 path 末尾，并用 ; 分隔
path = path + ";D:\\Share\\SynologyDrive\\testCv\\Adb"

# 将修改后的 path 变量设置回系统环境变量
os.environ["PATH"] = path

# 连接手机
subprocess.call('adb connect 127.0.0.1:7555')

# 获取屏幕截图
subprocess.call("adb shell /system/bin/screencap -p /sdcard/screenshot.png")
subprocess.call("adb pull /sdcard/screenshot.png ./screenshot.png")

# 读取模板和屏幕截图
template = cv2.imread("./tmp/browser.png", cv2.IMREAD_GRAYSCALE)
img = cv2.imread("./screenshot.png", cv2.IMREAD_GRAYSCALE)

# 进行模板匹配
res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
if max_val > 0.8:
    # 点击匹配区域
    h, w = template.shape
    center_x = max_loc[0] + w // 2
    center_y = max_loc[1] + h // 2
    cmd = "adb shell input tap {} {}".format(center_x, center_y)
    subprocess.call(cmd)

    # 等待浏览器打开
    time.sleep(5)

# 清除屏幕截图
=======
import os
import subprocess
import cv2
import time

# 获取 PATH 环境变量的值
path = os.environ.get("PATH")

# 将新目录添加到 path 末尾，并用 ; 分隔
path = path + ";D:\\Share\\SynologyDrive\\testCv\\Adb"

# 将修改后的 path 变量设置回系统环境变量
os.environ["PATH"] = path

# 连接手机
subprocess.call('adb connect 127.0.0.1:7555')

# 获取屏幕截图
subprocess.call("adb shell /system/bin/screencap -p /sdcard/screenshot.png")
subprocess.call("adb pull /sdcard/screenshot.png ./screenshot.png")

# 读取模板和屏幕截图
template = cv2.imread("./tmp/browser.png", cv2.IMREAD_GRAYSCALE)
img = cv2.imread("./screenshot.png", cv2.IMREAD_GRAYSCALE)

# 进行模板匹配
res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
if max_val > 0.8:
    # 点击匹配区域
    h, w = template.shape
    center_x = max_loc[0] + w // 2
    center_y = max_loc[1] + h // 2
    cmd = "adb shell input tap {} {}".format(center_x, center_y)
    subprocess.call(cmd)

    # 等待浏览器打开
    time.sleep(5)

# 清除屏幕截图
>>>>>>> ff549c1 (first commit)
os.remove("screenshot.png")