from DroneBlocksTelloSimulator.DroneBlocksSimulatorContextManager import DroneBlocksSimulatorContextManager


simulator_key = 'Get simulator_key and see visualization at https://coding-sim.droneblocks.io/'

with DroneBlocksSimulatorContextManager(simulator_key=simulator_key) as tello:
    tello.takeoff()
    tello.fly_forward(100, 'cm')
    tello.fly_left(100, 'cm')
    tello.fly_backward(100, 'cm')
    tello.fly_right(100, 'cm')
    tello.flip_backward()
    tello.land()
