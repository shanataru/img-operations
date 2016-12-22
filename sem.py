#!/usr/bin/python3

import sys
from PIL import Image, ImageTk
import tkinter
import my_neg
import gray_np
import my_light
import my_dark
import my_edges
import my_sharp
import mot_blur

def inv(orig):
	#zmena statusu obrazku
	statuslab.config(text='inverze')
	
	#jde videt mimo funkci...
	global canvas
	global photo

	#smazu dosavadni obrazek	
	canvas.delete(photo)
	
	#operace z import. skriptu
	img = my_neg.inverze(orig)
	photo = ImageTk.PhotoImage(img)
	canvas.itemconfigure(myimage, image=photo)

def gray(orig):
	statuslab.config(text='odstín šedi')

	global canvas
	global photo

	canvas.delete(photo)
	img = gray_np.grayscale(orig)
	photo = ImageTk.PhotoImage(img)
	canvas.itemconfigure(myimage, image=photo)

def light(orig):
	statuslab.config(text='zesvětlení')
	
	global canvas
	global photo

	canvas.delete(photo)
	img = my_light.lighten(orig)
	photo = ImageTk.PhotoImage(img)
	canvas.itemconfigure(myimage, image=photo)

def dark(orig):
	statuslab.config(text='ztmavení')

	global canvas
	global photo

	canvas.delete(photo)
	img = my_dark.darken(orig)
	photo = ImageTk.PhotoImage(img)
	canvas.itemconfigure(myimage, image=photo)


def edge(orig):
	statuslab.config(text='detekce hran')

	global canvas
	global photo

	canvas.delete(photo)
	img = my_edges.edge_detect(orig)
	photo = ImageTk.PhotoImage(img)
	canvas.itemconfigure(myimage, image=photo)

def emboss():

	statuslab.config(text='emboss')

def sharp(orig):
	statuslab.config(text='ostření')

	global canvas
	global photo

	canvas.delete(photo)
	img = my_sharp.sharpen(orig)
	photo = ImageTk.PhotoImage(img)
	canvas.itemconfigure(myimage, image=photo)

def motion(orig):
	statuslab.config(text='motion blur')

	global canvas
	global photo

	canvas.delete(photo)
	img = mot_blur.mb(orig)
	photo = ImageTk.PhotoImage(img)
	canvas.itemconfigure(myimage, image=photo)

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
myimage = canvas.create_image((img_w,img_h), image=photo, anchor=tkinter.SE)
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
inv_b = tkinter.Button(root, text="Inverze", width=17, height=1, command=lambda: inv(img))
inv_b.pack(padx=8, pady=3)

gray_b = tkinter.Button(root, text="Odstín šedi", width=17, height=1, command=lambda: gray(img))
gray_b.pack(padx=8, pady=3)

light_b = tkinter.Button(root, text="Zesvětlení", width=17, height=1, command=lambda: light(img))
light_b.pack(padx=8, pady=3)

dark_b = tkinter.Button(root, text="Ztmavení", width=17, height=1, command=lambda: dark(img))
dark_b.pack(padx=8, pady=3)

edge_b = tkinter.Button(root, text="Detekce hran", width=17, height=1, command=lambda: edge(img))
edge_b.pack(padx=8, pady=3)
	
emboss_b = tkinter.Button(root, text="Emboss", width=17, height=1, command=lambda: emboss(img))
emboss_b.pack(padx=8, pady=3)

sharp_b = tkinter.Button(root, text="Ostření", width=17, height=1, command=lambda: sharp(img))
sharp_b.pack(padx=8, pady=3)

motion_b = tkinter.Button(root, text="Motion blur", width=17, height=1, command=lambda: motion(img))
motion_b.pack(padx=8, pady=3)

#save_b = tkinter.Button(root, text="Uložit obrázek", width=17, height=1, command=...)
#save_b.pack(padx=8, pady=10, side='bottom')
reset_b = tkinter.Button(root, text="Reset", width=17, height=1, command=reset)
reset_b.pack(padx=8, pady=20, side='bottom')



root.mainloop()

