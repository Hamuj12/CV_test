import cv2, os
import numpy as np

# Load image
dir     = '/Users/hamuj2/Documents/repos/CV_test/'
fn      = 'laser3.jpg'
path    = os.path.join(dir, fn)
image   = cv2.imread(path)
# Convert to grayscale
gray    = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Blur the image to reduce noise
gray_blurred        = cv2.medianBlur(gray, 5)
# Apply Hough transform on the blurred image
detected_circles    = cv2.HoughCircles(gray_blurred 
                    ,cv2.HOUGH_GRADIENT # method used for detecting circles
                    ,1 # dp - the inverse ratio of the accumulator resolution to the image resolution 
                    ,150 # minDist - minimum distance between the centers of the detected circles, units of pixels
                    ,param1 = 50 # higher threshold of the two passed to the Canny() edge detector, units of pixels
                    ,param2 = 30 # lower threshold of the two passed to the Canny() edge detector, units of pixels
                    ,minRadius = 1 # minRadius - limits for detected circles, units of pixels
                    ,maxRadius = 100 # maxRadius - limits for detected circles, units of pixels
                    )
# Draw circles that are detected
circle_centers  = []
plot_centers    = True
if detected_circles is not None:
    detected_circles = np.uint16(np.around(detected_circles))
    for pt in detected_circles[0, :]:
        a, b, r = pt[0], pt[1], pt[2]
        # Draw the circumference of the circle
        cv2.circle(image, (a, b), r, (0, 255, 0), 2)
        # Draw a small circle (of radius 1) to show the center
        cv2.circle(image, (a, b), 1, (0, 0, 255), 3)
        if plot_centers: # plot centers in pixel coordinates onto image
            cv2.putText(image, f'({a},{b})', (a+70, b), cv2.FONT_HERSHEY_SIMPLEX, 
                        1.0, (255, 0, 0), 3, cv2.LINE_AA)

        circle_centers.append([a, b]) # append the center of the circle to the list
out_fn      = os.path.splitext(fn)[0] + '_detected_circles.png'
out_path    = os.path.join(dir, out_fn)
cv2.imwrite(out_path, cv2.cvtColor(image, cv2.COLOR_RGB2BGR))
print('The number of detected circles is:',detected_circles.shape[1])
print('The image height and width are {} and {}, respectively.'.format(image.shape[0],image.shape[1]))
print('The centers of the detected circles are:',np.array(circle_centers))