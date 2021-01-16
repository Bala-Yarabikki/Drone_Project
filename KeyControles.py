from djitellopy import tello
import KeypressModule as kp
from time import sleep

# initializing keyboardmodule and drone
kp.init()
drone = tello.Tello()
drone.connect()
print(drone.get_battery())

drone.takeoff()


def getkeyinput():
    lr, fb, ud, yv = 0, 0, 0, 0
    if kp.getkey("LEFT"):
        lr = -50
    elif kp.getkey("RIGHT"):
        lr = 50

    if kp.getkey("UP"):
        fb = 50
    elif kp.getkey("DOWN"):
        fb = -50

    if kp.getkey("w"):
        ud = 50
    elif kp.getkey("s"):
        ud = -50

    if kp.getkey("a"):
        yv = 50
    elif kp.getkey("d"):
        yv = -50

    if kp.getkey('e'): drone.takeoff()
    if kp.getkey('q'): drone.land()  # INCASE DRONE GOES MAD

    return [lr, fb, ud, yv]


while True:
    vals = getkeyinput()
    # sending keyinputs to drone
    drone.send_rc_control(vals[0], vals[1], vals[2], vals[3])

    sleep(0.05)  # INCASE THE DRONE CREATES HAVOC