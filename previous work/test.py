# -*- coding: utf-8 -*-
import pythoncom
import pyHook
import win32api
import win32con
 
def onMouseEvent(event):
	# 监听鼠标事件
	# print "MessageName:", event.MessageName
	# print "Message:", event.Message
	# print "Time:", event.Time
	# print "Window:", event.Window
	# print "WindowName:", event.WindowName
	# print "Position:", event.Position
	# print "Wheel:", event.Wheel
	# print "Injected:", event.Injected
    a = event.Message
    if a == 513:
        print "<--"
    elif a == 516:
        print "-->"
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 600, 600)
        time.sleep(0.05)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 600, 600)
 
    return True
 
def main():
	# 创建一个“钩子”管理对象
	hm = pyHook.HookManager()
 
	# # 监听所有键盘事件
	# hm.KeyDown = onKeyboardEvent
	# 设置键盘“钩子”
	# hm.HookKeyboard()
 
	# 监听所有鼠标事件
	hm.MouseAll = onMouseEvent
	# 设置鼠标“钩子”
	hm.HookMouse()
 
	# 进入循环，如不手动关闭，程序将一直处于监听状态
	pythoncom.PumpMessages()
 
if __name__ == "__main__":
	main()