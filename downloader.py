# -*- coding: utf-8 -*-
# 作者：Zerlaer
# 创建时间：2020/11/8 0:27
# 文件名：Downloader.py
# 编辑器：PyCharm
from tkinter import *
import wget
root = Tk()
root.title("Wget下载器")


def download():
    wget.download(my_entry.get())


Label(root, text="请输入链接地址:").pack(side=LEFT)
my_entry = Entry(root)
my_entry.pack(side=LEFT)
Button(root, text='开始下载', command=download).pack(side=LEFT)
root.mainloop()
