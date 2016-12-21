#!/usr/bin/python3

#zesvetleni obrazku
import numpy as np
from PIL import Image

def lighten(orig):
	data = np.asarray(orig, dtype=np.uint16)
	light = data * 3
	light = np.clip(light, 0, 255)
	light = np.asarray(light, dtype=np.uint8)
	out = Image.fromarray(light, 'RGB')
	return out
