import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def visualize_box_and_keypoints(keypoints_3d, box_dimensions, label_walls=True):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Offsets to center the origin on one face of the box
    x_offset = -box_dimensions[0] / 2
    z_offset = -box_dimensions[2] / 2

    # Drawing the box with the origin at the center of the XZ face
    for x in [x_offset, -x_offset]:
        for z in [z_offset, -z_offset]:
            ax.plot([x, x], [0, box_dimensions[1]], [z, z], color='b')

    for y in [0, box_dimensions[1]]:
        for z in [z_offset, -z_offset]:
            ax.plot([x_offset, -x_offset], [y, y], [z, z], color='b')

    for y in [0, box_dimensions[1]]:
        for x in [x_offset, -x_offset]:
            ax.plot([x, x], [y, y], [z_offset, -z_offset], color='b')

    
    # Define colors for each wall
    wall_colors = ['red', 'blue', 'green', 'brown', 'purple', 'orange']

    # Plotting keypoints for each wall in different colors
    for i, (x, y, z) in enumerate(keypoints_3d):
        color = wall_colors[i // 5 % len(wall_colors)]
        ax.scatter(x, y, z, color=color, depthshade=False)
        ax.text(x, y, z, f"{i}", color='black', fontsize=9)

    # Plotting origin
    ax.scatter(0, 0, 0, color='g', s=100)  # s is the size of the point

    if label_walls:
        # Adding labels for each face
        ax.text(0, 0, 0, "Wall 3", color='blue')
        ax.text(0, box_dimensions[1], 0, "Wall 1", color='blue')
        ax.text(0, box_dimensions[1]/2, box_dimensions[2]/2, "Top Wall", color='blue')
        ax.text(0, box_dimensions[1]/2, -box_dimensions[2]/2, "Bottom Wall", color='blue')
        ax.text(-box_dimensions[0]/2, box_dimensions[1]/2, 0, "Wall 2", color='blue')
        ax.text(box_dimensions[0]/2, box_dimensions[1]/2, 0, "Wall 4", color='blue')

    # Setting axes limits
    ax.set_xlim([x_offset, -x_offset])
    ax.set_ylim([0, box_dimensions[1]])
    ax.set_zlim([z_offset, -z_offset])

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

# save these keypoints as a numpy array
np.save('calib_box_v2.npy', keypoints_3d_example)

box_dimensions_example = (203, 203, 203)  # your box dimensions
visualize_box_and_keypoints(keypoints_3d_example, box_dimensions_example, label_walls=True)


# https://www.festi.info/boxes.py/ClosedBox?FingerJoint_angle=90.0&FingerJoint_style=rectangular&FingerJoint_surroundingspaces=2.0&FingerJoint_bottom_lip=0.0&FingerJoint_edge_width=1.0&FingerJoint_extra_length=0.0&FingerJoint_finger=2.0&FingerJoint_play=0.0&FingerJoint_space=2.0&FingerJoint_width=1.0&x=355&y=254&h=102&outside=0&outside=1&thickness=3.0&format=svg&tabs=0.0&qr_code=0&debug=0&labels=0&labels=1&reference=0&inner_corners=loop&burn=0.1&language=en&render=0