# -*- coding: utf-8 -*- from sys import *
import numpy as np
import unicodedata,matplotlib,math
matplotlib.use('agg')
import matplotlib.pyplot as plt
import time,importlib,subprocess,sys,random

conv=False
n=4
a=[]
w=[0,0]
z=[False,False,True,True]
#False = 0
#True = 1
#for i in range(n):
x=[0.22,0.25,0.20,0.18]
y=[0.30,0.37,0.18,0.15]
for i in range(len(x)):
	a.append([x[i],y[i]])
print('x',x,'y',y)
print()
print('a',a)
print()
dotprd=0.0
while not conv:
	p=0
	for i in range(n):
		print('a',i,a[i])
		dotprd=np.dot(w,a[i])
		print('Dot prod: ',dotprd)
		print()
		if z[i] and dotprd < 0:
			w=np.add(w,a[i])
			print('wrong', dotprd, z[i])
			print(w, 'is w')
			print()
		elif not z[i] and dotprd >= 0:
			w=np.subtract(w,a[i])
			print('wrong', dotprd, z[i])
			print(w, 'is w')
			print()
		else:
			print('correct', dotprd, z[i])
			p=p+1
			if p==4:
				print('converged!', p)
				plt.ylim(-1,1)
				plt.xlim(-1,1)
				pts=np.linspace(-1,1,70)
				f=w[0]+w[1]*pts
				plt.plot(pts,f)
				plt.scatter(x,y)
				plt.savefig('fig.pdf',transparent=True)
				print(w[0],w[1],z[i],dotprd,p)
				exit()
#			print('converged! ',w)
		
