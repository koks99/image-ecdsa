
from tkinter import filedialog as fd
import numpy as np
import cv2
from tkinter import Text
import tkinter as tk


def write_slogan():
    filename1 = fd.askopenfilename()
    f2 = fd.askopenfilename()
    y = cv2.imread(f2)
    y = cv2.resize(y, (128, 60), interpolation=cv2.INTER_CUBIC)
    x = cv2.imread(filename1)
    x = cv2.resize(x, (128, 60), interpolation=cv2.INTER_CUBIC)

    def rgb2gray(rgb):
        return np.dot(rgb[..., :3], [0.2989, 0.5870, 0.1140])

    x = rgb2gray(x)
    y=rgb2gray(y)
    x = x.astype(str)
    y = y.astype(str)

    from ellipticcurve.ecdsa import Ecdsa
    from ellipticcurve.privateKey import PrivateKey
    privateKey = PrivateKey()
    publicKey = privateKey.publicKey()
    a = []
    for i in x:
        for j in i:
            m = j.encode(encoding='UTF-8', errors='strict')
            signature = Ecdsa.sign(m, privateKey)
            a.append(signature)
    n = 0
    f = 0
    for i in y:
        for j in i:
            m = j.encode(encoding='UTF-8', errors='strict')
            valid = Ecdsa.verify(m, a[n], publicKey)
            if (valid == False):
                f = 1
                break
            n += 1
    if (f == 0):
        T.insert(tk.END, "Succeessfully  Verified!"+'\n')
    else:
        T.insert(tk.END, "Verification Unsuccessful."+'\n')


root = tk.Tk()
frame = tk.Frame(root)
frame.pack()
T = Text(root)
T.focus_set(  )
T.pack(side=tk.LEFT, fill=tk.Y)
T.insert(tk.END, "Welcome to Elliptic Curve Digital Signature Verification "+'\n')
slogan = tk.Button(frame,
                   text="Upload Images",
                   command=write_slogan)
slogan.pack(side=tk.LEFT)
button = tk.Button(frame,
                   text="QUIT",
                   fg="red",
                   command=quit)
button.pack(side=tk.LEFT)

root.mainloop()
