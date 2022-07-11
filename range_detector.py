import cv2
import argparse


def callback(value):
    pass


def setup_trackbars():
    cv2.namedWindow("Trackbars", 0 )
    for i in ["MIN", "MAX"]:
        v = 0 if i == "MIN" else 255
        for j in 'HSV':
            cv2.createTrackbar("%s_%s" % (j,i), "Trackbars", v, 255, callback)

def get_trackbar_values():
    values = []
    for i in ["MIN", "MAX"]:
        for j in 'HSV':
            v = cv2.getTrackbarPos("%s_%s"%(j,i), "Trackbars")
            values.append(v)
    return values

def main():
    #camera = cv2.VideoCapture(0)
    image = cv2.imread('redcarpet.jpg')
    setup_trackbars()
    while True:
       # ret, image = camera.read()
       # if not ret:
       #     break
        frame_to_thresh = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        v1_min, v2_min, v3_min, v1_max, v2_max, v3_max = get_trackbar_values()
        thresh = cv2.inRange(frame_to_thresh, (v1_min, v2_min, v3_min), (v1_max, v2_max, v3_max))

        preview = cv2.bitwise_and(image,image, mask=thresh)
        cv2.imshow("Preview", preview)
        cv2.imshow("Thresh", thresh)
        if cv2.waitKey(1) & 0xFF is ord('q'):
            break

if __name__ == "__main__":
    main()