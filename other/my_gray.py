import numpy as np
from PIL import Image

"""
Parameter of this function is an image opened by PIL.
"""

def grayscale(orig):
	data = np.asarray(orig, dtype=np.float64)
	gray = np.dot(data, [0.299, 0.587, 0.114])
	gray = np.asarray(gray, dtype=np.uint8)
	out = Image.fromarray(gray, 'L')
	return out
