from djitellopy import Tello


def setup_tello():
    tello = Tello()
    tello.connect()
    print(tello.get_battery())
    tello.streamon()
    return tello
