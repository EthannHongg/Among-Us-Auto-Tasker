# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api
import win32con


def pixel():
    interval = 1 * 10000

    try:
        if random.randint(0, interval) == 0:
            posXY = pyautogui.position()
            print(posXY, pyautogui.pixel(posXY[0], posXY[1]))
    except OSError:
        pass


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.005)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


def swipe(x1, y1, x2, y2, speed):
    win32api.SetCursorPos((x1, y1))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.1)
    win32api.SetCursorPos((x2, y2))
    time.sleep(speed)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


def hold(x, y, duration):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(duration)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


def pixel_color(x, y):
    try:
        return pyautogui.pixel(x, y)[0]
    except OSError:
        pass
    # [0] = R, [1] = G, [2] = B


def drag(x1, y1, x2, y2, speed):
    pyautogui.moveTo(x1, y1)
    pyautogui.dragTo(x2, y2, duration=speed)


def swipe_card():
    if pixel_color(1100, 195) == 20:
        click(785, 830)
        time.sleep(1)
        drag(557, 439, 1603, 439, 0.8)
        time.sleep(5)


def data():
    if pixel_color(1179, 463) == 241:
        click(919, 672)
        time.sleep(10)


def empty_garbage():
    if pixel_color(1231, 445) == 140:
        drag(1231, 445, 1215, 979, 4)
        time.sleep(5)


def align_engine_output():
    if pixel_color(1058, 929) == 41:
        initial_y = 0
        for y in range(198, 937, 20):
            if pixel_color(1201, y) == 202:
                initial_y = y
                break
            else:
                pass
        drag(1201, initial_y, 1201, 554, 0.2)
        time.sleep(5)


def divert_power_i():
    if pixel_color(1055, 518) == 253:
        switches = [632, 721, 812, 902, 992, 1082, 1172, 1262]
        y = 793
        real_x = 0
        for x in switches:
            if pixel_color(x, y) == 254:
                real_x = x

        drag(real_x, y, real_x, 600, 0.2)
        time.sleep(5)


def divert_power_ii():
    if pixel_color(908, 565) == 191:
        click(910, 572)
        time.sleep(5)


def caliberate_distributor():
    if pixel_color(956, 593) == 65:
        if pixel_color(1212, 778) == 111:
            click(1181, 840)
            time.sleep(5)
        elif pixel_color(1199, 524) == 83:
            click(1169, 604)
            time.sleep(0.2)
        elif pixel_color(1210, 275) == 255:
            click(1181, 348)
            time.sleep(0.2)


def stabilize_steering():
    if pixel_color(921, 566) == 255:
        click(921, 566)


def fuel_engine():
    if pixel_color(1394, 876) == 203:
        hold(1394, 876, 5)
        time.sleep(5)


while not keyboard.is_pressed("z"):
    pixel()
    swipe_card()
    data()
    empty_garbage()
    align_engine_output()
    divert_power_i()
    divert_power_ii()
    caliberate_distributor()
    stabilize_steering()
    fuel_engine()



