#!/usr/bin/python3

import sys
from PIL import Image, ImageTk
import tkinter

def inv():
	#zmena statusu obrazku
	statuslab.config(text='inverze')

def gray():
	statuslab.config(text='odstín šedi')

def light():
	statuslab.config(text='zesvětlení')

def dark():
	statuslab.config(text='ztmavení')

def edge():
	statuslab.config(text='detekce hran')

def emboss():
	statuslab.config(text='emboss')

def sharp():
	statuslab.config(text='ostření')

def motion():
	statuslab.config(text='motion blur')

def reset():
	statuslab.config(text='originál')
	

if len(sys.argv) == 1:
	print('Zadejte cestu k obrazku jako argument skriptu.')
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
statuslab = tkinter.Label(root, text=status_text, fg='blue', pady=10)
#lab.config(borderwidth=1, relief="solid")
lab.pack(side="top", anchor="center")
statuslab.pack(side='top')

#tlacitka pro jednotlive operace
inv_b = tkinter.Button(root, text="Inverze", width=17, height=1, command=inv)
inv_b.pack(padx=8, pady=3)
gray_b = tkinter.Button(root, text="Odstín šedi", width=17, height=1, command=gray)
gray_b.pack(padx=8, pady=3)
light_b = tkinter.Button(root, text="Zesvětlení", width=17, height=1, command=light)
light_b.pack(padx=8, pady=3)
dark_b = tkinter.Button(root, text="Ztmavení", width=17, height=1, command=dark)
dark_b.pack(padx=8, pady=3)
edge_b = tkinter.Button(root, text="Detekce hran", width=17, height=1, command=edge)
edge_b.pack(padx=8, pady=3)
emboss_b = tkinter.Button(root, text="Emboss", width=17, height=1, command=emboss)
emboss_b.pack(padx=8, pady=3)
sharp_b = tkinter.Button(root, text="Ostření", width=17, height=1, command=sharp)
sharp_b.pack(padx=8, pady=3)
motion_b = tkinter.Button(root, text="Motion blur", width=17, height=1, command=motion)
motion_b.pack(padx=8, pady=3)

#save_b = tkinter.Button(root, text="Uložit obrázek", width=17, height=1, command=...)
#save_b.pack(padx=8, pady=10, side='bottom')
reset_b = tkinter.Button(root, text="Reset", width=17, height=1, command=reset)
reset_b.pack(padx=8, pady=20, side='bottom')

root.mainloop()

