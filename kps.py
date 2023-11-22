import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Keypoints information 
keypoints_info = [
    # Face 1 (Left)
    {'face_id': 1, 'center_x': 0, 'center_y': 0},  
    {'face_id': 1, 'center_x': 101.23, 'center_y': 25.25},   # TR
    {'face_id': 1, 'center_x': 101.23, 'center_y': -25.25},  # BR
    {'face_id': 1, 'center_x': -101.23, 'center_y': 25.25},  # TL
    {'face_id': 1, 'center_x': -101.23, 'center_y': -25.25}, # BL
    # Face 2 (Front)
    {'face_id': 2, 'center_x': 10, 'center_y': 10},  
    {'face_id': 2, 'center_x': 146.65, 'center_y': 96.15},   # TR
    {'face_id': 2, 'center_x': 146.65, 'center_y': -96.15},  # BR
    {'face_id': 2, 'center_x': -146.65, 'center_y': 96.15},  # TL
    {'face_id': 2, 'center_x': -146.65, 'center_y': -96.15}, # BL
    # Face 3 (Bottom)
    {'face_id': 3, 'center_x': -30, 'center_y': -30},   
    {'face_id': 3, 'center_x': 156.67, 'center_y': 30.25},   # TR
    {'face_id': 3, 'center_x': 156.67, 'center_y': -30.25},  # BR
    {'face_id': 3, 'center_x': -156.67, 'center_y': 30.25},  # TL
    {'face_id': 3, 'center_x': -156.67, 'center_y': -30.25}, # BL
]

# Dimensions of the box (LxWxH in mm)
box_dimensions = (102, 355, 254)

# Function to convert 2D keypoints to 3D
def convert_to_3d(keypoints, dimensions):
    keypoints_3d = []
    half_length, half_width, half_height = [dim / 2 for dim in dimensions]

    for point in keypoints:
        face_id = point['face_id']
        x, y = point['center_x'], point['center_y']

        if face_id == 1:  # Left face
            keypoints_3d.append((-half_length, x, y))
        elif face_id == 2:  # Front face
            keypoints_3d.append((x, half_width, y))
        elif face_id == 3:  # Bottom face
            keypoints_3d.append((x, y, -half_height))

    return keypoints_3d

# Convert keypoints to 3D
keypoints_3d = convert_to_3d(keypoints_info, box_dimensions)

# Visualization using Matplotlib
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Drawing the box
for x in [-box_dimensions[0]/2, box_dimensions[0]/2]:
    for y in [-box_dimensions[1]/2, box_dimensions[1]/2]:
        ax.plot([x, x], [y, y], [-box_dimensions[2]/2, box_dimensions[2]/2], color='b')

for x in [-box_dimensions[0]/2, box_dimensions[0]/2]:
    for z in [-box_dimensions[2]/2, box_dimensions[2]/2]:
        ax.plot([x, x], [-box_dimensions[1]/2, box_dimensions[1]/2], [z, z], color='b')

for y in [-box_dimensions[1]/2, box_dimensions[1]/2]:
    for z in [-box_dimensions[2]/2, box_dimensions[2]/2]:
        ax.plot([-box_dimensions[0]/2, box_dimensions[0]/2], [y, y], [z, z], color='b')

# Adding keypoints
xs, ys, zs = zip(*keypoints_3d)
ax.scatter(xs, ys, zs, color='r')

# Setting labels and title
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')
ax.set_title('3D Visualization of Keypoints on a Box')

plt.show()
