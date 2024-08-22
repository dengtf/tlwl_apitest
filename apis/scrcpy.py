import os
from datetime import datetime
import subprocess

x = input("选择模式:\n1、普通\n2、普通息屏\n3、录屏\n4、录屏息屏\n")


def sendcommod(cmd):
    subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


def getfile():
    while (True):
        filename = input("请拖入你传输的文件：")
        segments = filename.split('\\')
        desired_content = segments[-1]
        cod = r".\adb.exe push " + filename + " /sdcard/Download/scrcpy/" + desired_content
        os.system(cod)


def get1():
    print("您已进行普通模式")
    # commond = "scrcpy"
    commond = "scrcpy --video-codec=h265 --max-size=3200 --max-fps=60 --no-audio --keyboard=uhid"
    sendcommod(commond)
    getfile()


def get2():
    print("您已进行普通息屏模式")
    commond = "scrcpy -S"
    sendcommod(commond)
    getfile()


def get3():
    print("您已进行录屏模式")
    # 获取当前日期和时间
    current_time = datetime.now().strftime("%Y年%m月%d日%H.%M.%S")
    commond = "scrcpy -r file/" + current_time + ".mp4"
    sendcommod(commond)
    getfile()


def get4():
    print("您已进行录屏息屏模式")
    # 获取当前日期和时间
    current_time = datetime.now().strftime("%Y年%m月%d日%H.%M.%S")
    commond = "scrcpy -S -r file/" + current_time + ".mp4"
    sendcommod(commond)
    getfile()


if (x == "" or x == "2"):
    get2()
elif (x == "1"):
    get1()
elif (x == "3"):
    get3()
elif (x == "4"):
    get4()

