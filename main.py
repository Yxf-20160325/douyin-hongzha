from pynput.keyboard import Key,Controller
import time
import messagebox
import tkinter as tk
import subprocess
import os
num = 0
error_num_big = 0
def error():
    messagebox.showwarning('警告','轰炸次数不能大于100')
    
    
def kill_python():
    subprocess.Popen('taskkill /f /im python.exe', shell=True)

    
keyboard = Controller()   #实例化该函数功能，创建键盘控制器
boom = input('请输入你想要轰炸的信息内容:') 
num = eval(input('请输入要轰炸的次数:')) 
print ("1秒后开始轰炸")
if num > 100:
    messagebox.showwarning('警告','轰炸次数不能大于100,请重新输入')
    num = eval(input('请输入要轰炸的次数:'))
time.sleep(1)
messagebox.showwarning('开始','开始轰炸,在4秒后开始轰炸,请确认以下信息是否正确:')
messagebox.showwarning('信息：','轰炸内容:'+boom+'\n轰炸次数:'+str(num)+'\n开始轰炸,如错误请在弹出窗口内点击取消，正确请点击确定')
root = tk.Tk()
root.geometry('500x500')
root.title('是否轰炸')
label = tk.Label(root,text="如果点击确定时未响应，是正常情况,会在4秒后开始轰炸(请不要关闭窗口)")
label.pack()
entry1 = tk.Entry(root)
entry1.pack()
def debug1():
    boom = input('请输入你想要轰炸的信息内容:') 
    num = eval(input('请输入要轰炸的次数:')) 
def debug():
    if entry1.get() == "debug:on":
        debug = "on"
        button4 = tk.Button(root,text="更改次数",command=debug1)
        button4.pack()   
if debug == "on":
    button = tk.Button(root,text='确定',command=root.quit)
    button.pack()
    button2 = tk.Button(root,text='取消',command=kill_python)
    button2.pack()
elif num >= 100:
    button = tk.Button(root,text='确定',command=error)
    button.pack()
    button2 = tk.Button(root,text='取消',command=kill_python)
    button2.pack()
else:
     button = tk.Button(root,text='确定',command=root.quit)
     button.pack()
     button2 = tk.Button(root,text='取消',command=kill_python)
     button2.pack()
root.mainloop()
time.sleep(4)
print ("开始轰炸")
if num > 100:
    messagebox.showwarning('警告','轰炸次数不能大于100')
    kill_python()
else:
    for i in range(num):       #循环num次
      time.sleep(0.6)      #每次循环间隔0.6秒，防止轰炸太快
      keyboard.type(boom)     #模拟输入轰炸信息boom内容
      keyboard.press(Key.enter)    #模拟按下回车键
      keyboard.release(Key.enter)  #模拟松开回车键
