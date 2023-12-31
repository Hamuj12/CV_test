from ultralytics import YOLO
import cv2
import math 
import serial

# Set up the serial port connection
ser = serial.Serial('/dev/tty.usbmodem0E22CF551', 115200)  # Change this to the correct COM port if needed

# start webcam
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

# model
model = YOLO("yolo-Weights/yolov8n.pt")

while True:
    success, img = cap.read()
    results = model(img, stream=True)

    human_count = 0  # Counter for detected humans
    centroids = []  # List to store centroids of detected humans

    # coordinates
    for r in results:
        boxes = r.boxes

        for box in boxes:
            if box.cls[0].item() == 0.:
                human_count += 1
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)  # convert to int values

                # put box in cam
                cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)

                # confidence
                confidence = math.ceil((box.conf[0]*100))/100
                print("Confidence --->", confidence)

                # centroid
                centroid_x = (x1 + x2) // 2
                centroid_y = (y1 + y2) // 2
                print("Centroid --->", (centroid_x, centroid_y))

                # Store centroid
                centroids.append((centroid_x, centroid_y))

                # draw a dot at the centroid
                cv2.circle(img, (centroid_x, centroid_y), 5, (0, 255, 0), -1)

                # put text
                org = [x1, y1]
                font = cv2.FONT_HERSHEY_SIMPLEX
                fontScale = 1
                color = (255, 0, 0)
                thickness = 2

                cv2.putText(img, "person", org, font, fontScale, color, thickness)

                if human_count >= 3:  # Break the loop after detecting 3 humans
                    break
        if human_count >= 3:  # Break the outer loop too
            break

    # Sort centroids based on x-coordinates
    centroids.sort(key=lambda c: c[0])

    # Send centroids of the first 3 humans detected (sorted by x-coordinate)
    if centroids:
        centroid_str = ",".join([f"{x},{y}" for x, y in centroids[:3]])
        ser.write(f"{centroid_str}\n\r".encode())

    cv2.imshow('Webcam', img)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
ser.close()
