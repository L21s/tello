import time
import cv2
import keyboard as kb


def use_keyboard_control(drone, image):
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 50

    if kb.get_key("LEFT"):
        lr = -speed
    if kb.get_key("RIGHT"):
        lr = speed
    if kb.get_key("UP"):
        fb = speed
    if kb.get_key("DOWN"):
        fb = -speed
    if kb.get_key("w"):
        ud = speed
    if kb.get_key("s"):
        ud = -speed
    if kb.get_key("d"):
        yv = speed
    if kb.get_key("a"):
        yv = -speed
    if kb.get_key("l"):
        drone.land()
        drone.streamoff()
    if kb.get_key("k"):
        drone.takeoff()
    if kb.get_key("p"):
        cv2.imwrite(f'resources/images/{time.time()}.jpg', image)
        time.sleep(0.3)

    return [lr, fb, ud, yv]


def show_image(drone):
    image = drone.get_frame_read().frame
    image = cv2.resize(image, (360, 240))
    cv2.imshow("Image", image)
    cv2.waitKey(1)
    return image


def use_keyboard_control_and_get_image(drone):
    kb.init()
    while True:
        image = show_image(drone)
        keyboard_input = use_keyboard_control(drone, image)
        drone.send_rc_control(
            keyboard_input[0],
            keyboard_input[1],
            keyboard_input[2],
            keyboard_input[3],
        )
