import numpy as np
from PIL import Image
from numba import jit

#decorator for performance; numba
@jit
def mask_app(data, data_h, data_w, maska):
	out = np.zeros((data_w-2, data_h-2, 3))
	for z in range(3):
		for y in range(1, data_h-1):
			for x in range(1, data_w-1):
				vyrez = data[x-1:x+2, y-1:y+2, z]
				out[x-1, y-1, z] = (vyrez * maska).sum()
	return out

"""
Parameter of this function is an image opened by PIL.
"""
def sharpen(orig):
	data = np.asarray(orig, dtype=np.float64) 
	maska = np.array( [ 
				[-1, -1, -1],
				[-1, 9, -1], 
				[-1, -1, -1] ] )

	# stronger sharpen mask
	#maska = np.array( [
	#				[1, 1, 1],
	#				[1, -7, 1], 
	#				[1, 1, 1] ] )

	data_w, data_h, data_b = data.shape

	#aplikace masky
	sharp = mask_app(data, data_h, data_w, maska)
	sharp = np.clip(sharp, 0, 255)
	# save
	img_out = Image.fromarray(np.asarray(sharp, dtype=np.uint8), 'RGB')
	return img_out
