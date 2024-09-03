import numpy as np
from PIL import Image
from numba import jit

@jit
def mask_app(data, data_b, data_h, data_w, maska):
	edges = np.zeros((data_w-4, data_h-4, data_b))
	for z in range(data_b): #for each dir
		for y in range(2, data_h-3): #x y 
			for x in range(2, data_w-3):
				vyrez = data[x-2:x+3, y-2:y+3, z] #matrix 3x3x1
				edges[x-2, y-2, z] = (vyrez * maska).sum()
	return edges

"""
Parameter of this function is an image opened by PIL.
"""

def edge_detect(orig):
	data = np.asarray(orig, dtype=np.float64) #i want to operate on floats
	print (data.shape)
	maska = np.array( [ 
				[0, 0, -1, 0, 0],
				[0, 0, -1, 0, 0], 
				[0, 0, 2, 0, 0],
				[0, 0, 0, 0, 0],
				[0, 0, 0, 0, 0] ] )

	data_w, data_h, data_b = data.shape
	# mask application
	edges = mask_app(data, data_b, data_h, data_w, maska)
	edges = np.clip(edges, 0, 255)
	img_out = Image.fromarray(np.asarray(edges, dtype=np.uint8), 'RGB')
	return img_out

