import numpy as np
from PIL import Image

"""
Parameter of this function is an image opened by PIL.
"""

def darken(orig):
	data = np.asarray(orig, dtype=np.uint8)
	dark = data * 0.5
	dark = np.asarray(dark, dtype=np.uint8)
	out = Image.fromarray(dark, 'RGB')
	return out
