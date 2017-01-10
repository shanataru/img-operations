#!/usr/bin/python3

import numpy as np
from PIL import Image
from numba import jit

@jit
def mask_app(data, data_b, data_h, data_w, maska):
	mblur = np.zeros([data_w-2, data_h-2, data_b])
	for z in range(data_b): #pro kazdou slozku
		for y in range(1, data_h-1): #x y 
			for x in range(1, data_w-1):
				vyrez = data[x-1:x+2, y-1:y+2, z] #matice 3x3x1
				#uprava pro out matici.. od 0,0...
				mblur[x-1, y-1, z] = ((vyrez * maska).sum()) * 1/3
	return mblur	

"""
Funkce 'mb' vraci rozmazany obrazek (img_out).
Parametrem funkce je originalni obrazek (orig) otevreny pomoci PIL.
"""

def mb(orig):
	data = np.asarray(orig, dtype=np.float)
	#maska, matice
	maska = np.array( [ 
				[1, 0, 0],
				[0, 1, 0], 
				[0, 0, 1] ] )

	data_w, data_h, data_b = data.shape
#aplikace masky
	mblur = mask_app(data, data_b, data_h, data_w, maska)
	img_out = Image.fromarray(np.asarray(mblur, dtype=np.uint8), 'RGB')
	return img_out
