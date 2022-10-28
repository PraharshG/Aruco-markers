#importing packages
import numpy as np
import cv2 as cv
from cv2 import aruco

#getting the aruco marker dictionary
marker_dict = aruco.Dictionary_get(aruco.DICT_4X4_100) 

#creating the marker parameter
param_markers = aruco.DetectorParameters_create()

#accessing the webcam
cap = cv.VideoCapture(0)

#reading each frame of the webcam
while True:
	ret,frame = cap.read()
	if not ret:
		break
		
	#converting frame to grayscale
	gray_frame = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
	
	#detecting the markers
	marker_corners,marker_IDs,reject = aruco.detectMarkers(gray_frame,marker_dict,parameters = param_markers)
	
	#if marker is present on real time
	if marker_corners:
		
		#iterating through marker objects
		for ids,corners in zip(marker_IDs,marker_corners):
			
			#drawing a box around the detected marker
			cv.polylines(frame,[corners.astype(np.int32)],True,(0,255,255),4,cv.LINE_AA)
			
			#getting the list of corner ids and assigning the top right corner
			corners = corners.reshape(4,2)
			corners = corners.astype(int)
			top_right = corners[0].ravel()
			
			#displaying the marker id
			cv.putText(frame,f"ID: {ids[0]}",top_right,cv.FONT_HERSHEY_PLAIN,1.3,(200,100,0),2,cv.LINE_AA)
			
			#printing the marker id along with corner ids
			print(ids," ",corners)	
			
	#displaying the video		
	cv.imshow('frame',frame)
	
	#holding the video
	Key = cv.waitKey(1)
	
	#escaping the video
	if Key == ord('q'):
		break

#destroying the objects
cap.release()
cv.destroyAllWindows()
