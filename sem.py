#!/usr/bin/python3

import sys
from PIL import Image, ImageTk
from tkinter import filedialog
import tkinter
import my_neg
import gray_np
import my_light
import my_dark
import my_edges
import my_sharp
import mot_blur
import my_emboss

global current_img

def inv(orig):
	""" 
	Funkce ocekava na vstupu obrazek a vytvori jeho inverzi pouzitim importovaneho modulu my_neg.
	Prepise se text ve 'status label'.
	Vysledny obrazek se zobrazi na canvas.
	Aktivuje se tlacitko pro ukladani.
	"""

	#zmena statusu obrazku
	statuslab.config(text='inverze')

	global canvas
	global photo
	global current_img

	#smazu dosavadni obrazek	
	canvas.delete(photo)
	
	#operace z import. skriptu
	img = my_neg.inverze(orig)
	photo = ImageTk.PhotoImage(img)
	canvas.itemconfigure(myimage, image=photo)
	current_img = img

	save_b.config(state = 'normal')

def gray(orig):
	statuslab.config(text='odstín šedi')

	global canvas
	global photo
	global current_img

	canvas.delete(photo)
	img = gray_np.grayscale(orig)
	photo = ImageTk.PhotoImage(img)
	canvas.itemconfigure(myimage, image=photo)
	current_img = img
	save_b.config(state = 'normal')

def light(orig):
	statuslab.config(text='zesvětlení')
	
	global canvas
	global photo
	global current_img

	canvas.delete(photo)
	img = my_light.lighten(orig)
	photo = ImageTk.PhotoImage(img)
	canvas.itemconfigure(myimage, image=photo)
	current_img = img
	save_b.config(state = 'normal')

def dark(orig):
	statuslab.config(text='ztmavení')

	global canvas
	global photo
	global current_img

	canvas.delete(photo)
	img = my_dark.darken(orig)
	photo = ImageTk.PhotoImage(img)
	canvas.itemconfigure(myimage, image=photo)
	current_img = img
	save_b.config(state = 'normal')

def edge(orig):
	statuslab.config(text='detekce hran')

	global canvas
	global photo
	global current_img

	canvas.delete(photo)
	img = my_edges.edge_detect(orig)
	#img2 = gray_np.grayscale(img) #grayscaled
	#photo = ImageTk.PhotoImage(img2)
	photo = ImageTk.PhotoImage(img)
	canvas.itemconfigure(myimage, image=photo)
	current_img = img
	save_b.config(state = 'normal')

def emboss(orig):
	statuslab.config(text='emboss')

	global canvas
	global photo
	global current_img

	canvas.delete(photo)
	img = my_emboss.emboss(orig)
	#img2 = gray_np.grayscale(img) #grayscaled bump map
	#photo = ImageTk.PhotoImage(img2)
	photo = ImageTk.PhotoImage(img) #RGB
	canvas.itemconfigure(myimage, image=photo)
	current_img = img
	save_b.config(state = 'normal')

def sharp(orig):
	statuslab.config(text='ostření')

	global canvas
	global photo
	global current_img

	canvas.delete(photo)
	img = my_sharp.sharpen(orig)
	photo = ImageTk.PhotoImage(img)
	canvas.itemconfigure(myimage, image=photo)
	current_img = img
	save_b.config(state = 'normal')

def motion(orig):
	statuslab.config(text='motion blur')

	global canvas
	global photo
	global current_img

	canvas.delete(photo)
	img = mot_blur.mb(orig)
	photo = ImageTk.PhotoImage(img)
	canvas.itemconfigure(myimage, image=photo)
	current_img = img
	save_b.config(state = 'normal')

def reset(orig):
	"""
	Funkce zobrazi vstupni obrazek bez jakekoliv modifikace.
	Deaktivuje se tlacitko pro ukladani.
	"""
	statuslab.config(text='originál')
	
	global canvas
	global photo

	canvas.delete(photo)
	photo = ImageTk.PhotoImage(orig)
	canvas.itemconfigure(myimage, image=photo)
	save_b.config(state = 'disabled')

def save_img():
	"""
	Funkce uklada aktualne zobrazeny obrazek na canvasu (current_img).
	Zobrazi se dialogove okno pro zvoleni mista ulozeni. 
	Implicitne se obrazek ulozi ve formatu '.png'.
	"""

	try:	
		name = filedialog.asksaveasfile(mode='bw',defaultextension='.png')
		current_img.save(name, format='PNG')
	except:
		...


""" 
Program ocekava cestu k obrazku, ktery ma otevrit a nadale upravovat.
Program skonci pri zadani neplatne (a nebo zadne) cesty k obrazku.
Kdyz je vice argumentu na vstupu, ignoruje vsechny krome prvniho.
"""

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
current_img = img
myimage = canvas.create_image((img_w,img_h), image=photo, anchor=tkinter.SE)
canvas.pack(side='left')

#stitek pod obrazkem (status label)
status_text = 'originál'
label_text = arg + '  ' + str(img_w) + 'x' + str(img_h)
lab = tkinter.Label(root, text=label_text)
statuslab = tkinter.Label(root, text=status_text, fg='blue', pady=10)
#lab.config(borderwidth=1, relief="solid")
lab.pack(side="top", anchor="center")
statuslab.pack(side='top')


"""
Program provadi operace nad obrazkem podle stisku jednotlivych tlacitek.
Do jednotlivych funkci se posila originalni obrazek, ktery byl vstupnim argumentem skriptu,
	jednotlive operace se nedaji na sebe 'vrstvit'.
"""

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

save_b = tkinter.Button(root, text="Uložit obrázek", width=17, height=1, command=lambda: save_img())
save_b.pack(padx=8, pady=10, side='bottom')
save_b.config(state = 'disabled')

reset_b = tkinter.Button(root, text="Reset", width=17, height=1, command=lambda: reset(img))
reset_b.pack(padx=8, pady=20, side='bottom')


root.mainloop()

