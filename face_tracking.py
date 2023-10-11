import cv2


IMAGE_WIDTH = 360
IMAGE_HEIGHT = 240
FORWARD_BACKWARD_RANGE = [6200, 6800]
DISTANCE_THRESHOLD = 3000


def get_image(drone, image_width, image_height):
    image = drone.get_frame_read().frame
    image = cv2.resize(image, (image_width, image_height))
    return image


def find_face(image):
    cascade = cv2.CascadeClassifier("resources/frontal_face_cascade.xml")
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = cascade.detectMultiScale(image_gray, 1.2, 8)

    face_center_coordinates = []
    face_areas = []

    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
        center_x_coordinate = x + w // 2
        center_y_coordinate = y + h // 2
        area = w * h
        cv2.circle(image, (center_x_coordinate, center_y_coordinate), 5, (0, 255, 0), cv2.FILLED)
        face_center_coordinates.append([center_x_coordinate, center_y_coordinate])
        face_areas.append(area)

    if len(face_areas) != 0:
        biggest_area_index = face_areas.index(max(face_areas))
        return image, [face_center_coordinates[biggest_area_index], face_areas[biggest_area_index]]
    else:
        return image, [[0, 0], 0]


def track_face(drone, face_coordinates_and_area, forward_backward_range, image_width, image_height):
    face_coordinates = face_coordinates_and_area[0]
    face_area = face_coordinates_and_area[1]
    face_x, face_y = face_coordinates
    image_center_x = image_width // 2
    image_center_y = image_height // 2

    forward_backward_speed = 0
    if face_area < forward_backward_range and face_area != 0:
        forward_backward_speed = 25
    if face_area > forward_backward_range and face_area != 0:
        forward_backward_speed = -25

    rotation = 0
    if face_x < image_center_x and face_x != 0:
        rotation = -50
    if face_x > image_center_x and face_x != 0:
        rotation = 50

    up_down_speed = 0
    if face_y < image_center_y and face_y != 0:
        up_down_speed = 25
    if face_y > image_center_y and face_y != 0:
        up_down_speed = -25

    drone.send_rc_control(0, forward_backward_speed, up_down_speed, rotation)


def follow_face(drone):
    while True:
        image = get_image(drone, IMAGE_WIDTH, IMAGE_HEIGHT)
        image, face_coordinates_and_area = find_face(image)
        track_face(drone, face_coordinates_and_area, DISTANCE_THRESHOLD, IMAGE_WIDTH, IMAGE_HEIGHT)
        cv2.imshow("Image", image)
        if cv2.waitKey(1) & 0xFF == ord('l'):
            drone.land()
            break
