import tkinter as tk
import socket
from tkinter import filedialog
from PIL import Image, ImageTk, ImageOps  # 画像データ用
import serial

import cv2
class Application(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)

        self.ser = serial.Serial('/dev/tty.usbmodem111101',115200)
        self.master.title("ラジコン操作")     # ウィンドウタイトル
        #self.IPADDR = "192.168.10.152"
        #self.PORT = 5000

        self.scale_var1 = tk.IntVar()
        scale1 = tk.Scale( self.master, 
                    variable = self.scale_var1, 
                    command = self.slider_scroll1,
                    orient=tk.HORIZONTAL,   # 配置の向き、水平(HORIZONTAL)、垂直(VERTICAL)
                    length = 300,           # 全体の長さ
                    width = 20,             # 全体の太さ
                    sliderlength = 30,      # スライダー（つまみ）の幅
                    from_ = 0,            # 最小値（開始の値）
                    to = 255,               # 最大値（終了の値）
                    resolution=1,         # 変化の分解能(初期値:1)
                    tickinterval=50         # 目盛りの分解能(初期値0で表示なし)
                    )
        scale1.pack(side= tk.TOP)

        self.scale_var2 = tk.IntVar()
        scale2 = tk.Scale( self.master, 
                    variable = self.scale_var2, 
                    command = self.slider_scroll2,
                    orient=tk.HORIZONTAL,   # 配置の向き、水平(HORIZONTAL)、垂直(VERTICAL)
                    length = 300,           # 全体の長さ
                    width = 20,             # 全体の太さ
                    sliderlength = 30,      # スライダー（つまみ）の幅
                    from_ = 0,            # 最小値（開始の値）
                    to = 255,               # 最大値（終了の値）
                    resolution=1,         # 変化の分解能(初期値:1)
                    tickinterval=50         # 目盛りの分解能(初期値0で表示なし)
                    )
        scale2.pack(side= tk.TOP)

        self.scale_var3 = tk.IntVar()
        scale3 = tk.Scale( self.master, 
                    variable = self.scale_var3, 
                    command = self.slider_scroll3,
                    orient=tk.HORIZONTAL,   # 配置の向き、水平(HORIZONTAL)、垂直(VERTICAL)
                    length = 300,           # 全体の長さ
                    width = 20,             # 全体の太さ
                    sliderlength = 30,      # スライダー（つまみ）の幅
                    from_ = 0,            # 最小値（開始の値）
                    to = 255,               # 最大値（終了の値）
                    resolution=1,         # 変化の分解能(初期値:1)
                    tickinterval=50         # 目盛りの分解能(初期値0で表示なし)
                    )
        scale3.pack(side= tk.TOP)

        self.scale_var4 = tk.IntVar()
        scale4 = tk.Scale( self.master, 
                    variable = self.scale_var4, 
                    command = self.slider_scroll4,
                    orient=tk.HORIZONTAL,   # 配置の向き、水平(HORIZONTAL)、垂直(VERTICAL)
                    length = 300,           # 全体の長さ
                    width = 20,             # 全体の太さ
                    sliderlength = 30,      # スライダー（つまみ）の幅
                    from_ = 0,            # 最小値（開始の値）
                    to = 255,               # 最大値（終了の値）
                    resolution=1,         # 変化の分解能(初期値:1)
                    tickinterval=50         # 目盛りの分解能(初期値0で表示なし)
                    )
        scale4.pack(side= tk.TOP)
    def slider_scroll1(self, event=None):
        '''スライダーを移動したとき'''
        print_data1 = "!1<"
        print_data1 += str(self.scale_var1.get())
        print_data1 += ">."
        print(print_data1)
        #self.sock = socket.socket(socket.AF_INET)
        #self.sock.connect((self.IPADDR, self.PORT))
        self.data = print_data1

        #self.sock.send(self.data.encode("utf-8")) 

        self.ser.write(self.data.encode("utf-8"))
    def slider_scroll2(self, event=None):
        '''スライダーを移動したとき'''
        print_data2 = "!2<"
        print_data2 += str(self.scale_var2.get())
        print_data2 += ">."
        print(print_data2)
        #self.sock = socket.socket(socket.AF_INET)
        #self.sock.connect((self.IPADDR, self.PORT))
        self.data = print_data2

        #self.sock.send(self.data.encode("utf-8")) 

        self.ser.write(self.data.encode("utf-8"))
    def slider_scroll3(self, event=None):
        '''スライダーを移動したとき'''
        print_data3 = "!3<"
        print_data3 += str(self.scale_var3.get())
        print_data3 += ">."
        print(print_data3)
        #self.sock = socket.socket(socket.AF_INET)
        #self.sock.connect((self.IPADDR, self.PORT))
        self.data = print_data3

        #self.sock.send(self.data.encode("utf-8")) 

        self.ser.write(self.data.encode("utf-8"))
    def slider_scroll4(self, event=None):
        '''スライダーを移動したとき'''
        print_data4 = "!4<"
        print_data4 += str(self.scale_var4.get())
        print_data4 += ">."
        print(print_data4)
        #self.sock = socket.socket(socket.AF_INET)
        #self.sock.connect((self.IPADDR, self.PORT))
        self.data = print_data4

        #self.sock.send(self.data.encode("utf-8")) 

        self.ser.write(self.data.encode("utf-8"))
if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master = root)
    root.geometry("700x500")
    root.resizable(False, False)
    app.mainloop()