import cv2 as cv
from cv2 import aruco

marker_dict = aruco.Dictionary_get(aruco.DICT_4X4_100)

param_markers = aruco.DetectorParameters_create()

cap = cv.VideoCapture('markers.mov')

while True:
	ret,frame = cap.read()
	if not ret:
		break
	gray_frame = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
	marker_corners,marker_IDs,reject = aruco.detectMarkers(gray_frame,marker_dict,parameters = param_markers)
	print(marker_IDs)	
	cv.imshow('frame',frame)
	Key = cv.waitKey(1)
	if Key == ord('q'):
		break

cap.release()
cv.destroyAllWindows()					
