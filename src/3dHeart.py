#!/usr/bin/env python2
#coding:utf8

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

def implicitplot3d(fn,bbox=(-1.5,1.5)):
	xmin, xmax,ymin,ymax,zmin,zmax = bbox * 3
	fig = plt.figure()
	ax = fig.add_subplot(111,projection='3d')
	a1 = np.linspace(xmin,xmax,50)
	b1 = np.linspace(xmin,xmax,20)
	a11,a12 = np.meshgrid(a1,a1)

	for z in b1:
		x1,y1 = a11,a12
		z1 = fn(x1,y1,z)
		cset = ax.contour(x1,y1,z1+z,[z],zdir='z')
	for y in b1:
		x1,z1 = a11,a12
		y1 = fn(x1,y,z1)
		cset = ax.contour(x1,y1+y,z1,[y],zdir='y')
	for x in b1:
		y1,z1 = a11,a12
		x1 = fn(x,y1,z1)
		cset = ax.contour(x1+x,y1,z1,[x],zdir='x')

	ax.set_zlim3d(zmin,zmax)
	ax.set_xlim3d(xmin,xmax)
	ax.set_ylim3d(ymin,ymax)
	plt.show()

if __name__ == '__main__':
	implicitplot3d(lambda x,y,z: (x*x + 2*y*y+z*z-1)**3-(x**2)*(z**3)-y**2*z**3/10.0)
