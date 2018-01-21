import numpy as np
import math
import random

class NoiseCircle():

	def __init__(self, seed=20180118, dim=64):
		self.seed = seed
		self.dim  = dim

		self.min_circle_width = int(dim/8)
		self.num_circle_dots  = 500
		self.circle_width_px = 3
		self.darkness = .5

	def create_dataset(self, rows):
	    labels  = []
	    samples = []
	    for i in range(rows):
	        data, label = self.create_dataset_row()
	        labels.append(label)
	        samples.append(data)
	    return (np.array(samples).astype(np.float32), np.array(labels).astype(np.float32))


	# Create random noise and draw circles in it
	def create_dataset_row(self):
	    data = np.random.random((self.dim, self.dim)).astype(np.float32)
	    label = self._add_circles(data)
	    label = np.array(label).astype(np.float32)
	    return (data, label)


	def _add_circles(self, data):
	    radius = int((random.random() * (self.dim/2 - self.min_circle_width)) + self.min_circle_width)
	    xpos = random.random()*self.dim
	    ypos = random.random()*self.dim
	    
	    self._draw_circle(data, xpos, ypos, radius, self.darkness, self.min_circle_width)

	    return [xpos, ypos, radius+self.circle_width_px/2]


	def _draw_circle(self, data, xpos, ypos, radius, darkness, width):
	    for i in range(self.num_circle_dots):
	        for r in range(radius, radius+width):
	            rad = 2 * math.pi * i/self.num_circle_dots
	            x = int(round( r*math.cos(rad)+xpos))
	            y = int(round(-r*math.sin(rad)+ypos))
	            if x >= 0 and x < self.dim and y >= 0 and y < self.dim:
	                data[x,y] = data[x,y] - self.darkness


