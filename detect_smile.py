from keras.utils import img_to_array
from keras.models import load_model
import numpy as np
import argparse
import imutils
import cv2

ap = argparse.ArgumentParser()

ap.add_argument("-c", "--cascade", required=True, help="path of face cascade")
ap.add_argument("-m", "--model", required=True, help="path of trained model")
ap.add_argument("-v", "--video", help="path of video file")
args = vars(ap.parse_args())

detector = cv2.CascadeClassifier(args["cascade"])
model = load_model(args["model"])

if not args.get('video', False):
    camera = cv2.VideoCapture(0)
else :
    camera = cv2.VideoCapture(args["video"])

while True:
    (grapped, frame) = camera.read()

    if args.get("video") and not grapped:
        break

    frame = imutils.resize(frame, width=300)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frameClone = frame.copy()

    rects = detector.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30,30), flags=cv2.CASCADE_SCALE_IMAGE)
    for (fX, fY, fW, fH) in rects:
        roi = gray[fY:fY+fH, fX:fX+fW]
        roi = cv2.resize(roi, (28, 28))
        roi = roi.astype("float")/255.0
        roi = img_to_array(roi)
        roi = np.expand_dims(roi, axis=0)

        (notSmiling, smiling) = model.predict(roi)[0]
        label = "Smiling" if smiling > notSmiling else "Not Smiling"

        cv2.putText(frameClone, label , (fX-20, fY-20), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 1)
        cv2.rectangle(frameClone, (fX, fY), (fX + fW, fY+ fH), (0, 255, 0), 2)
    cv2.imshow("Face", frameClone)

    if cv2.waitKey(0) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()
