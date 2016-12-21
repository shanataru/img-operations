#!/usr/bin/python3

import numpy as np
from PIL import Image

def darken(orig):
	data = np.asarray(orig, dtype=np.uint8)
	dark = data * 0.5
	dark = np.asarray(dark, dtype=np.uint8)
	out = Image.fromarray(dark, 'RGB')
	return out
