from  djitellopy import tello
import cv2
from time import sleep
drone = tello.Tello()
drone.connect()
print(drone.get_battery())

#Cam_on
drone.streamon()

while True:
    img = drone.get_frame_read().frame
    img = cv2.resize(img,(720,1080))
    cv2.imshow("Image from drone", img)
    cv2.waitKey(1)