import cv2

im1=cv2.imread('C:/Users/kckck/Documents/workspace/rackspace/res/original.jpg',1)
im2=cv2.imread('C:/Users/kckck/Documents/workspace/rackspace/res/mod.jpg',1)
im1_gray=cv2.cvtColor(im1,cv2.COLOR_BGR2GRAY)
im2_gray=cv2.cvtColor(im2,cv2.COLOR_BGR2GRAY)

frameDelta=cv2.absdiff(im1_gray,im2_gray)
thresh=cv2.threshold(frameDelta,25,255,cv2.THRESH_BINARY)[1]

#thresh=cv2.dilate(thresh,None,iterations=2)
(_,cnts,_)=cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

for c in cnts:
	if cv2.contourArea(c)< 300:
		continue
	(x,y,w,h)=cv2.boundingRect(c)
	cv2.imwrite("empty.jpg",im2[y:y+h,x:x+w])
	cv2.rectangle(im2,(x,y),(x+w,y+h),(0,255,0),2)
	text="Needs replenishment"
	cv2.putText(im2,text,(10,20),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0),2)
cv2.imshow("original",im1)
cv2.imshow("changed",im2)
cv2.imwrite("detected2.jpg",im2)
cv2.waitKey(0)
cv2.destroyAllWindows()
