import numpy as np
from scipy.ndimage.filters import convolve
from numpy import uint8
import cv2

def myfunc(i):
    pass # do nothing

cv2.namedWindow('title') # create win with win name

cv2.createTrackbar('gamma', # name of value
                   'title', # win name
                   1, # min
                   100, # max
                   myfunc) # callback func
cv2.createTrackbar('red', # name of value
                   'title', # win name
                   1, # min
                   100, # max
                   myfunc) # callback func
cv2.createTrackbar('green', # name of value
                   'title', # win name
                   1, # min
                   100, # max
                   myfunc) # callback func
cv2.createTrackbar('blue', # name of value
                   'title', # win name
                   1, # min
                   100, # max
                   myfunc) # callback func
cv2.createTrackbar('on or off', # name of value
                   'title', # win name
                   0, # min
                   2, # max
                   myfunc) # callback func

                  



cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,  640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)


while(True):

    ret, frame = cap.read()
    if not ret: continue


    gamma = cv2.getTrackbarPos('gamma',  # get the value
    									   'title')  # of the win
    r = cv2.getTrackbarPos('red',  # get the value
    									   'title')  # of the win
    g = cv2.getTrackbarPos('green',  # get the value
    									   'title')  # of the win
    b = cv2.getTrackbarPos('blue',  # get the value
    									   'title')  # of the win
    switch = cv2.getTrackbarPos('on or off',  # get the value
    									   'title')  # of the win
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
 
    kernel = np.array([[1/16, 1/8, 1/16],
                                  [1/8, 1/4, 1/8],
                                  [1/16, 1/8, 1/16]])    

    ## do something by using v
    
    R = frame[:,:,2]
    G = frame[:,:,1]
    B = frame[:,:,0]
    R = R/255
    G = G/255
    B = B/255
    R = R**(gamma/100)
    G = G**(gamma/100)
    B = B**(gamma/100)
    R = R**(1/r)
    G = G**(1/g)
    B = B**(1/b)
    frame[:,:,2] = R*255
    frame[:,:,1] = G*255
    frame[:,:,0] = B*255
    
    if switch == 1:
        lframe = convolve(gray,kernel)
        frame = lframe
        frame = frame.astype(np.uint8)
        
    else :
        frame[:,:,2] = R*255
        frame[:,:,1] = G*255
        frame[:,:,0] = B*255

        
    
    cv2.imshow('title', frame)  # show in the win

    k = cv2.waitKey(1)
    if k == ord('q') or k == 27:
        break



cap.release()
cv2.destroyAllWindows()
