#!/usr/bin/python3

import sys
from PIL import Image, ImageTk
import tkinter

def inv():
	statuslab.config(text='inverze')

if len(sys.argv) == 1:
	print('Zadejte obrazek jako argument skriptu.')
	exit()

#obrazek predan argumentem skriptu
arg = sys.argv[1]
#vytvorim si hlavni okno
root = tkinter.Tk()
root.title("Semestralni prace")

#otevru obrazek
try:
	img = Image.open(arg)
except:
	print('Obrazek nelze otevrit nebo neexistuje.')
	exit()

img_w, img_h = img.size

#zavedeni canvasu jako potomek hl. okna
canvas = tkinter.Canvas(root, width=img_w, height=img_h)
photo = ImageTk.PhotoImage(img)
image = canvas.create_image((img_w,img_h), image=photo, anchor=tkinter.SE)
canvas.pack(side='left')

#stitek pod obrazkem
status_text = 'originál'
label_text = arg + '  ' + str(img_w) + 'x' + str(img_h)
lab = tkinter.Label(root, text=label_text)
statuslab = tkinter.Label(root, text=status_text)
#lab.config(borderwidth=1, relief="solid")
lab.pack(side="bottom", anchor="center")
statuslab.pack(side='bottom')

#tlacitka pro jednotlive operace
inv_b = tkinter.Button(root, text="Inverze", width=17, height=1, command=inv)
inv_b.pack( padx=8, pady=3)
gray_b = tkinter.Button(root, text="Odstín šedi", width=17, height=1, command=...)
gray_b.pack(padx=8, pady=3)
light_b = tkinter.Button(root, text="Zesvětlení", width=17, height=1, command=...)
light_b.pack( padx=8, pady=3)
dark_b = tkinter.Button(root, text="Ztmavení", width=17, height=1, command=...)
dark_b.pack( padx=8, pady=3)
edge_b = tkinter.Button(root, text="Detekce hran", width=17, height=1, command=...)
edge_b.pack( padx=8, pady=3)
emboss_b = tkinter.Button(root, text="Emboss", width=17, height=1, command=...)
emboss_b.pack( padx=8, pady=3)
sharp_b = tkinter.Button(root, text="Ostření", width=17, height=1, command=...)
sharp_b.pack( padx=8, pady=3)
motion_b = tkinter.Button(root, text="Motion blur", width=17, height=1, command=...)
motion_b.pack( padx=8, pady=3)

root.mainloop()

