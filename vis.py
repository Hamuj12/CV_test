import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def visualize_box_and_keypoints(keypoints_3d, box_dimensions, label_walls=True):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Offsets to center the origin
    y_offset = -box_dimensions[0] / 2
    x_offset = 0
    z_offset = -box_dimensions[2] / 2

    # Drawing the box with new orientation
    for y in [y_offset, -y_offset]:
        for z in [z_offset, -z_offset]:
            ax.plot([x_offset, box_dimensions[1]], [y, y], [z, z], color='b')

    for x in [x_offset, box_dimensions[1]]:
        for z in [z_offset, -z_offset]:
            ax.plot([x, x], [y_offset, -y_offset], [z, z], color='b')

    for x in [x_offset, box_dimensions[1]]:
        for y in [y_offset, -y_offset]:
            ax.plot([x, x], [y, y], [z_offset, -z_offset], color='b')


    
    # Define colors for each wall
    wall_colors = ['red', 'blue', 'green', 'brown', 'purple', 'orange']

    # Plotting keypoints for each wall in different colors
    for i, (x, y, z) in enumerate(keypoints_3d):
        color = wall_colors[i // 5 % len(wall_colors)]
        ax.scatter(x, y, z, color=color, depthshade=False)
        ax.text(x, y, z, f"{i}", color='black', fontsize=9)

    # Plotting origin
    ax.scatter(0, 74.5, 0, color='black', s=100)  # s is the size of the point

    if label_walls:
        # Assuming Wall 1 is now facing the positive X direction, etc.
        ax.text(0, 0, 0, "Wall 3", color='blue')  # Center of Wall 3
        ax.text(box_dimensions[1], 0, 0, "Wall 1", color='blue')  # Center of Wall 1
        ax.text(0, box_dimensions[0] / 2, 0, "Wall 2", color='blue')  # Center of Wall 2
        ax.text(0, -box_dimensions[0] / 2, 0, "Wall 4", color='blue')  # Center of Wall 4
        ax.text(0, 0, box_dimensions[2] / 2, "Top Wall", color='blue')  # Center of Top Wall
        ax.text(0, 0, -box_dimensions[2] / 2, "Bottom Wall", color='blue')  # Center of Bottom Wall


    # Setting axes limits
    ax.set_xlim([0, box_dimensions[1]])  # New X (inward)
    ax.set_ylim([-box_dimensions[0] / 2, box_dimensions[0] / 2])  # New Y (to the left)
    ax.set_zlim([-box_dimensions[2] / 2, box_dimensions[2] / 2])  # Z (upward)


    # Setting labels and title
    ax.set_xlabel('X Axis')
    ax.set_ylabel('Y Axis')
    ax.set_zlabel('Z Axis')
    ax.set_title('3D Visualization of Keypoints on a Box')

    plt.show()

# Old kps for rectangle box
# keypoints_3d_example = [(51, -10, -10),
#                         (51, -146.65, -96.15),
#                         (51, -146.65, 96.15),
#                         (51, 146.65, -96.15),
#                         (51, 146.65, 96.15),

#                         (-51, 10, 10),
#                         (-51, 146.65, 96.15),
#                         (-51, 146.65, -96.15),
#                         (-51, -146.65, 96.15),
#                         (-51, -146.65, -96.15),

#                         (-10, -30, 127),
#                         (30.25, 156.67, 127),
#                         (-30.25, 156.67, 127),
#                         (30.25, -156.67, 127),
#                         (-30.25, -156.67, 127),

#                         (-10, -30, -127),
#                         (30.25, -156.67, -127),
#                         (-30.25, -156.67, -127),
#                         (30.25, 156.67, -127),
#                         (-30.25, 156.67, -127),

#                         (0, 177.5, 0),
#                         (25.25, 177.5, 101.23),
#                         (-25.25, 177.5, 101.23),
#                         (25.25, 177.5, -101.23),
#                         (-25.25, 177.5, -101.23),

#                         (0, -177.5, 0),
#                         (25.25, -177.5, 101.23),
#                         (-25.25, -177.5, 101.23),
#                         (25.25, -177.5, -101.23),
#                         (-25.25, -177.5, -101.23),]  
    
# new kps for cub box, order is wall 3, wall 1, top wall, bottom wall, wall 2, wall 4
# keypoints for each face are in order of center, top left, top right, bottom right, bottom left, look at drawing to see positions of each face
keypoints_3d_example = [
                        # wall 1 (opposite wall 3, corners are offset 10mm from the edges)
                        (0, 203, 0),
                        (74.5, 203, 74.5),
                        (-74.5, 203, 74.5),
                        (-74.5, 203, -74.5),
                        (74.5, 203, -74.5),

                        # wall 2 (opposite wall 4, corners are offset 30mm from the edges)
                        (-101.5, 121.5, 0),
                        (-101.5, 156, 54.5),
                        (-101.5, 47, 54.5),
                        (-101.5, 47, -54.5),
                        (-101.5, 156, -54.5),

                        # wall 3 (dead center, corners are offset 10mm from the edges)
                        (0, 0, 0), 
                        (-74.5, 0, 74.5),
                        (74.5, 0, 74.5),
                        (74.5, 0, -74.5),
                        (-74.5, 0, -74.5),

                        # wall 4 (opposite wall 2, corners are offset 30mm from the edges)
                        (101.5, 121.5, 0),
                        (101.5, 47, 54.5),
                        (101.5, 156, 54.5),
                        (101.5, 156, -54.5),
                        (101.5, 47, -54.5),

                        # top wall (opposite bottom wall, corners are offset 20mm from the edges)
                        (10, 91.5, 101.5),
                        (-64.5, 166, 101.5),
                        (64.5, 166, 101.5),
                        (64.5, 37, 101.5),
                        (-64.5, 37, 101.5),

                        # bottom wall (opposite top wall, corners are offset 20mm from the edges)
                        (10, 91.5, -101.5),
                        (64.5, 166, -101.5),
                        (-64.5, 166, -101.5),
                        (-64.5, 37, -101.5),
                        (64.5, 37, -101.5),
                        ]

#keypoints_3d_example_transformed = [(y, -x, z) for x, y, z in keypoints_3d_example]

keypoints_3d_example_transformed =  [
                                    (203, 0, 0), 
                                    (203, -74.5, 74.5), 
                                    (203, 74.5, 74.5), 
                                    (203, 74.5, -74.5), 
                                    (203, -74.5, -74.5), 
                                    
                                    (121.5, 101.5, 0), 
                                    (156, 101.5, 54.5), 
                                    (47, 101.5, 54.5), 
                                    (47, 101.5, -54.5), 
                                    (156, 101.5, -54.5), 
                                    
                                    (0, 0, 0), 
                                    (0, 74.5, 74.5), 
                                    (0, -74.5, 74.5), 
                                    (0, -74.5, -74.5), 
                                    (0, 74.5, -74.5), 
                                    
                                    (121.5, -101.5, 0), 
                                    (47, -101.5, 54.5), 
                                    (156, -101.5, 54.5), 
                                    (156, -101.5, -54.5), 
                                    (47, -101.5, -54.5), 
                                    
                                    (91.5, -10, 101.5), 
                                    (166, 64.5, 101.5), 
                                    (166, -64.5, 101.5), 
                                    (37, -64.5, 101.5), 
                                    (37, 64.5, 101.5), 

                                    (91.5, -10, -101.5), 
                                    (166, -64.5, -101.5), 
                                    (166, 64.5, -101.5), 
                                    (37, 64.5, -101.5), 
                                    (37, -64.5, -101.5)
                                    ]

# save these keypoints as a numpy array
np.save('calib_box_v2.npy', keypoints_3d_example_transformed)

box_dimensions_example = (203, 203, 203)  # your box dimensions
visualize_box_and_keypoints(keypoints_3d_example_transformed, box_dimensions_example, label_walls=True)


# https://www.festi.info/boxes.py/ClosedBox?FingerJoint_angle=90.0&FingerJoint_style=rectangular&FingerJoint_surroundingspaces=2.0&FingerJoint_bottom_lip=0.0&FingerJoint_edge_width=1.0&FingerJoint_extra_length=0.0&FingerJoint_finger=2.0&FingerJoint_play=0.0&FingerJoint_space=2.0&FingerJoint_width=1.0&x=355&y=254&h=102&outside=0&outside=1&thickness=3.0&format=svg&tabs=0.0&qr_code=0&debug=0&labels=0&labels=1&reference=0&inner_corners=loop&burn=0.1&language=en&render=0