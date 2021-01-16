from  djitellopy import tello
import cv2
from time import sleep
drone = tello.Tello()
drone.connect()
print(drone.get_battery())

#controls
# left_right_velocity, forward_backward_velocity, up_down_velocity, yaw_velocity
drone.send_rc_control(0,0,0,0)
sleep(2)
drone.send_rc_control(0,0,0,0)
sleep(2)
drone.send_rc_control(0,0,0,0)
sleep(2)
drone.land()
# ImageCapture
