#!/usr/bin/python3

import numpy as np
from PIL import Image

def inverze(orig):
	data = np.asarray(orig, dtype=np.uint8)
	negativ = 255 - data
	out = Image.fromarray(negativ, 'RGB')
	return out
