import cv2
import numpy as np
import matplotlib.pyplot as plt
x=[]
y=[]
z=[]
a=0
col=0
row=0
img1 = cv2.imread('testcase2.jpg')
img2 = cv2.imread('testcase2.jpg')


img_gray = cv2.cvtColor(img1,  cv2.COLOR_BGR2GRAY)
template1 = cv2.imread('temp.jpeg', 0)
template2 = cv2.imread('temp2.jpeg', 0)
template3 = cv2.imread('grid.jpg' , 0)

w1, h1 = template1.shape[::-1]
w2, h2 = template2.shape[::-1]
w3, h3 = template3.shape[::-1]

res1 = cv2.matchTemplate(img_gray, template1, cv2.TM_CCOEFF_NORMED)
res2 = cv2.matchTemplate(img_gray, template2, cv2.TM_CCOEFF_NORMED)
res3 = cv2.matchTemplate(img_gray, template3, cv2.TM_CCOEFF_NORMED)

threshold = 0.95
loc1 = np.where(res1>= threshold)
loc2 = np.where(res2>= threshold)
loc3 = np.where(res3>= threshold)

for pt1 in zip(*loc1[::-1]):
	 cv2.rectangle(img1, pt1, (pt1[0]+w1, pt1[1]+h1) , (0,0,255) , 2)
	 x.append(pt1)
for pt2 in zip(*loc2[::-1]):
	 cv2.rectangle(img1, pt2, (pt2[0]+w2, pt2[1]+h2) , (255,0,0) , 2)
	 y.append(pt2)
for pt3 in zip(*loc3[::-1]):
	 cv2.rectangle(img1, pt3, (pt3[0]+w3, pt3[1]+h3) , (0,255,0) , 2)
	 z.append(pt3)
	 a=a+1

#cv2.imshow('path1', img1)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

if a==0:	
	wi= img2.shape[1]
	hi= img2.shape[0]
	cv2.line(img2, (0,int(0.5*hi)), (int(wi),int(0.5*hi)), (255,0,0), 2)
	print(1)
	cv2.imshow('image', img2)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
	quit()	


for i in range(0, a):
    if z[i][0] == z[0][0] :
       	row = row+1
col = int(a/row) +1
row = row +1              
print (row)
print (col)
x.sort() 
y.sort()
z.sort()
print (x)
print (y)
print (z)
if row==0 and col==0:
	if a[0][0]==0:
		cv2.line(img2, (0,int(0.5*ht)), ())
if row !=0 and col!=0:
	leng = z[row][0]-z[0][0]
	ht = z[1][1]-z[0][1]
a=[[0]*col for r in range(row)]
print(leng)
print(ht)
for i in range(0,len(x)):
	d=int(x[i][0]/leng)
	c=int(x[i][1]/ht)
	a[c][d]=1
for i in range(0,len(y)):
    d=int(y[i][0]/leng)
    c=int(y[i][1]/ht)
    a[c][d]=-1
print (a)


def path (l1,l2,l3,l4):
	q=int((l2*leng)+(0.5*leng))
	r=int((l1*ht)+(0.5*ht))
	s=int((l4*leng)+(0.5*leng))
	t=int((l3*ht)+(0.5*ht))
	cv2.line(img2, (q,r), (s,t), (255,0,0), 2)

def call():
	cv2.imshow('image', img2)
	cv2.waitKey(0)
	cv2.destroyAllWindows()	

def samerow(x,i,j):
	if i == row-1:
		if j == col-1:
			if a[i][j]==0:
				cv2.line(img2, (int(j*leng+0.5*leng),int(i*ht+0.5*ht)), (int(j*leng+leng),int(i*ht+0.5*ht)), (255,0,0), 2)
				print(1)
				call()
				quit()
		if j!= col:
			if a[i][j] == 0:
				cv2.line(img2, (int(j*leng+0.5*leng),int(i*ht+0.5*ht)), (int(j*leng+leng),int(i*ht+0.5*ht)), (255,0,0), 2)
				print(-1)
				call()
				quit()
	if j == col-1:
		if i!= row-1:
			if a[i][j] == 0:
				cv2.line(img2, (int(j*leng+0.5*leng),int(i*ht+0.5*ht)), (int(j*leng+leng),int(i*ht+0.5*ht)), (255,0,0), 2)
				print(-1)
				call()
				quit()
	if i<=row and j<=col:
		if x == 1:
			if a[i][j+1]==0:
				path(i,j,i,j+1)
				j=j+1
				samerow(1,i,j)
			elif a[i][j+1]==1:
				path(i,j,i,j+1)
				j=j+1
				updown(3,i,j)
			elif a[i][j+1]==-1:
				path(i,j,i,j+1)
				j=j+1
				updown(4,i,j)	
		if x == 2:
			if a[i][j-1]==0:
				path(i,j,i,j-1)
				j=j-1
				samerow(2,i,j)
			elif a[i][j-1]==1:
				path(i,j,i,j-1)
				j=j-1
				updown(4,i,j)
			elif a[i][j]==-1:
				path(i,j,i,j-1)
				j=j-1
				updown(4,i,j)				

def updown(y,i,j):
	if i == row-1:
		if j == col-1:
			if a[i][j] == 0:
				cv2.line(img2, (int(j*leng+0.5*leng),int(i*ht+0.5*ht)), (int(j*leng+leng),int(i*ht+0.5*ht)), (255,0,0), 2)
				print(1)
				call()
				quit()
		if j!= col:
			if a[i][j] == 0:
				cv2.line(img2, (int(j*leng+0.5*leng),int(i*ht+0.5*ht)), (int(j*leng+leng),int(i*ht+0.5*ht)), (255,0,0), 2)
				print(-1)
				call()
				quit()
	if j == col-1:
		if i!= row-1:
			if a[i][j] == 0:
				cv2.line(img2, (int(j*leng+0.5*leng),int(i*ht+0.5*ht)), (int(j*leng+leng),int(i*ht+0.5*ht)), (255,0,0), 2)
				print(-1)
				call()
				exit()
	if i<=row and j<=col:
		if y ==3:
			if a[i+1][j]==0:
				path(i,j,i+1,j)
				i=i+1
				updown(3,i,j)
			if a[i+1][j]==1:
				path(i,j,i+1,j)
				i=i+1
				samerow(1,i,j)
			if a[i+1][j]==-1:
				path(i,j,i+1,j)
				i=i+1
				samerow(2,i,j)	

		elif y==4:
			if a[i-1][j]==0:
				path(i,j,i-1,j)
				i=i-1
				updown(4,i,j)
			if a[i-1][j]==1:
				path(i,j,i-1,j)
				i=i-1
				samerow(2,i,j)
			if a[i-1][j]==-1:
				path(i,j,i-1,j)
				i=i-1
				samerow(1,i,j)	
if a[0][0] == 0:
	cv2.line(img2, (0,int(0.5*ht)), (int(0.5*leng),int(0.5*ht)), (255,0,0), 2)
	samerow(1,0,0)
elif a[0][0] == 1:
	cv2.line(img2, (0,int(0.5*ht)), (int(0.5*leng),int(0.5*ht)), (255,0,0), 2)
	updown(3,0,0)
elif a[0][0] == -1:
	print(-1)
	cv2.line(img2, (0,int(0.5*ht)), (int(0.5*leng),int(0.5*ht)), (255,0,0), 2)
	cv2.line(img2, (int(0.5*leng),int(0.5*ht)), (int(0.5*leng),0), (255,0,0), 2)
