import sys
from PIL import Image, ImageTk
from tkinter import filedialog
import tkinter
from other import my_neg
from other import my_gray
from other import my_light
from other import my_dark
from kernel import my_edges
from kernel import my_sharp
from kernel import my_mot_blur
from kernel import my_emboss


def operation(orig, op):
	""" 
	The function awaits input image and performs and operation defined in 'op'.
	Text in 'status label' is updated.
	The image is then displayed on canvas.
	Save button is activated.
	"""
	global canvas
	global photo
	global current_img
	
	if (op == 0): #inverse
		#zchange img status
		statuslab.config(text='inverse')
		img = my_neg.inverze(orig)
	elif (op == 1): 
		statuslab.config(text='greyscale')
		img = my_gray.grayscale(orig)
	elif (op == 2): 
		statuslab.config(text='lighten')
		img = my_light.lighten(orig)
	elif (op == 3): 
		statuslab.config(text='darken')
		img = my_dark.darken(orig)
	elif (op == 4):
		statuslab.config(text='edge detection')
		img = my_edges.edge_detect(orig)
		#img2 = my_gray.grayscale(img) #grayscaled
		#photo = ImageTk.PhotoImage(img2)
	elif (op == 5): #emboss
		statuslab.config(text='emboss')
		img = my_emboss.emboss(orig)
		#img2 = my_gray.grayscale(img) #grayscaled
		#photo = ImageTk.PhotoImage(img2)
	elif (op == 6): #sharpen
		statuslab.config(text='sharpen')
		img = my_sharp.sharpen(orig)
	else: #motion blur
		statuslab.config(text='motion blur')
		img = my_mot_blur.mb(orig)
	
	canvas.delete(photo)	
	photo = ImageTk.PhotoImage(img)
	canvas.itemconfigure(myimage, image=photo)
	current_img = img
	save_b.config(state = 'normal')


def reset(orig):
	"""
	The function displays input image without any modification.
	Save button is deactivated.
	"""
	statuslab.config(text='original')
	
	global canvas
	global photo

	canvas.delete(photo)
	photo = ImageTk.PhotoImage(orig)
	canvas.itemconfigure(myimage, image=photo)
	save_b.config(state = 'disabled')

def save_img():
	"""
	The function saves the displayed image on canvas (current_img).
	Opens a dialogue window for selecting where to save.
	Saves in '.png' by default.
	"""
	global current_img

	try:	
		name = filedialog.asksaveasfile(mode='bw',defaultextension='.png')
		current_img.save(name, format='PNG')
	except:
		...

""" 
The script expects one arg, the directory to an image, which is supposed to be edited.
The program ends if invalid directory is given.
More than one arguments will be ignored.
"""

if len(sys.argv) == 1:
	print('Input the image name or directory as an argument of the script.\nE.g. \'./img_ops.py lenna.png\'')
	sys.exit()

# image as an arg
arg = sys.argv[1]
# create main window
root = tkinter.Tk()
root.title("BI-PYT 2016 - Semestral work")

# open image
try:
	img = Image.open(arg)
except:
	print('Cannot open image or it does not exist.')
	sys.exit()

img_w, img_h = img.size

# canvas as descendant of main window
canvas = tkinter.Canvas(root, width=img_w, height=img_h)
photo = ImageTk.PhotoImage(img)
current_img = img
myimage = canvas.create_image((img_w,img_h), image=photo, anchor=tkinter.SE)
canvas.pack(side='left')

# img status label
status_text = 'original'
label_text = arg + '  ' + str(img_w) + 'x' + str(img_h)
lab = tkinter.Label(root, text=label_text)
statuslab = tkinter.Label(root, text=status_text, fg='blue', pady=10)
#lab.config(borderwidth=1, relief="solid")
lab.pack(side="top", anchor="center")
statuslab.pack(side='top')


"""
Operations on the image when pressing a button.
Each function takes in the original img (input arg of the script) and the number id of the operation.
Cannot layer each operation on one image.
"""

inv_b = tkinter.Button(root, text="Inverse", width=17, height=1, command=lambda: operation(img, 0))
inv_b.pack(padx=8, pady=3)

gray_b = tkinter.Button(root, text="Greyscale", width=17, height=1, command=lambda: operation(img, 1))
gray_b.pack(padx=8, pady=3)

light_b = tkinter.Button(root, text="Lighten", width=17, height=1, command=lambda: operation(img, 2))
light_b.pack(padx=8, pady=3)

dark_b = tkinter.Button(root, text="Darken", width=17, height=1, command=lambda: operation(img, 3))
dark_b.pack(padx=8, pady=3)

edge_b = tkinter.Button(root, text="Edge Detection", width=17, height=1, command=lambda: operation(img, 4))
edge_b.pack(padx=8, pady=3)
	
emboss_b = tkinter.Button(root, text="Emboss", width=17, height=1, command=lambda: operation(img, 5))
emboss_b.pack(padx=8, pady=3)

sharp_b = tkinter.Button(root, text="Sharpen", width=17, height=1, command=lambda: operation(img, 6))
sharp_b.pack(padx=8, pady=3)

motion_b = tkinter.Button(root, text="Motion Blur", width=17, height=1, command=lambda: operation(img, 7))
motion_b.pack(padx=8, pady=3)


save_b = tkinter.Button(root, text="Save Image", width=17, height=1, command=lambda: save_img())
save_b.pack(padx=8, pady=10, side='bottom')
save_b.config(state = 'disabled')

reset_b = tkinter.Button(root, text="Reset", width=17, height=1, command=lambda: reset(img))
reset_b.pack(padx=8, pady=20, side='bottom')


root.mainloop()

